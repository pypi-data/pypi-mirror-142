import importlib.util
from configparser import ConfigParser

from pathlib import Path
from types import ModuleType
from typing import List, Optional, Tuple
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


ROOT_PATH = Path(".")

PACKAGE_BLACKLIST = {"tests",}

SOURCE_DIRECTORY = "src"
SOURCE_PATH = ROOT_PATH / SOURCE_DIRECTORY

SETUP_CFG = ROOT_PATH / "setup.cfg"


def get_packages(src_directory: str = SOURCE_DIRECTORY) -> Tuple[List[str], List[str]]:
    all_packages = find_packages(where=src_directory)
    packages = [package for package in all_packages if "." not in package]
    assert len(packages) > 0, "no modules found"
    return all_packages, list(set(packages) - PACKAGE_BLACKLIST)


def load_module(package: str, src_directory: Path = SOURCE_PATH) -> ModuleType:
    module_init_path = src_directory / package / "__init__.py"
    spec = importlib.util.spec_from_file_location(package, str(module_init_path))
    assert spec is not None and spec.loader is not None, f"error importing module '{package}'"
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ImportError:
        pass
    return module


def create_no_compile(src_dir: str = SOURCE_DIRECTORY) -> None:
    all_packages, packages = get_packages(src_dir)
    name, version, author, desc = load_setup_meta(SETUP_CFG, packages)

    setup(
        name=name,
        author=author,
        version=version,
        description=desc,
        packages=all_packages,
        package_data={package: ["py.typed"] for package in packages},
        package_dir={"": src_dir},
    )


def create(src_dir: str = SOURCE_DIRECTORY) -> None:
    try:
        import nuitka.distutils.DistutilCommands as NuitkaDistutilCommands  # type: ignore[import]
        from mypy import stubgen
    except ImportError:
        return create_no_compile(src_dir)

    all_packages, packages = get_packages(src_dir)
    name, version, author, desc = load_setup_meta(SETUP_CFG, packages)

    class BuildPy(build_py):
    
        def run(self) -> None:
            cmdclasses = self.distribution.cmdclass
            if not self.dry_run and "build" in cmdclasses and cmdclasses["build"] == NuitkaDistutilCommands.build:
                options = stubgen.parse_options(["-o", str(self.build_lib), str(SOURCE_PATH)])
                stubgen.generate_stubs(options)
            return super().run()

    setup(
        name=name,
        author=author,
        version=version,
        description=desc,
        packages=all_packages,
        cmdclass={"build_py": BuildPy},
        package_data={package: ["py.typed"] for package in packages},
        package_dir={"": src_dir},
        command_options={
            "nuitka": {
                "lto": "yes",  # type: ignore[dict-item]
                "no-pyi-file": True,  # type: ignore[dict-item]
                "python-flag": "-OO",  # type: ignore[dict-item]
                "warn-implicit-exceptions": True,  # type: ignore[dict-item]
                "warn-unusual-code": True,  # type: ignore[dict-item]
            },
        },
        build_with_nuitka=True,
    )


def load_setup_meta(config: Path, modules: List[str]) -> Tuple[str, str, str, str]:
    assert config.exists()
    
    cfg = ConfigParser()
    cfg.read(config)
    
    name = None
    if cfg.has_option("metadata", "name"):
        name = cfg.get("metadata", "name")
    else:
        assert len(modules) == 1, "package name cannot be determined"
        name, = modules
    
    version = ""
    author = ""
    desc = ""
    if name in modules:
        module = load_module(name)
    
        if not cfg.has_option("metadata", "version"):
            version = getattr(module, "__version__", "")
        
        if not cfg.has_option("metadata", "author"):
            author = getattr(module, "__author__", "")
        
        if not cfg.has_option("metadata", "description"):
            desc = getattr(module, "__desc__", getattr(module, "__doc__", ""))
    else:
        assert cfg.has_option("metadata", "version"), f"version could not be determined"

    return name, version, author, desc

