from pathlib import Path
from typing import Any, Dict, List, Optional

import toml

from setuptools.build_meta import _BuildMetaBackend

from . import setup


ROOT = Path(".")
PYPROJECT_TOML = ROOT / "pyproject.toml"


class BuildBackend(_BuildMetaBackend):
    compile_: Optional[bool] = None

    def run_setup(self, setup_script: str = "setup.py") -> None:
        compile_ = self.compile_
        if compile_ is None:
            cfg: dict = toml.loads(PYPROJECT_TOML.read_text())
            compile_ = cfg.get("tool", {}).get("sbuild", {}).get("compile", True)
            if not isinstance(compile_, bool):
                raise Exception(f"invalid option \"{compile_}\" for tool.sbuild.compile. Must be either true or false")
        if compile_:
            setup.create()
        else:
            setup.create_no_compile()

    def build_wheel(self, wheel_directory: str, config_settings: Optional[Dict[str, List[str]]] = None,
            metadata_directory: Optional[str] = None) -> Any:
        if config_settings is not None:
            if "--no-compile" in config_settings:
                self.compile_ = False
                if "--compile" in config_settings:
                    raise Exception("got two contradicting build parameters --compile and --no-compile")
            if "--compile" in config_settings:
                self.compile_ = True
        return super().build_wheel(wheel_directory, config_settings, metadata_directory)


default = BuildBackend()


build_sdist                      = default.build_sdist
build_wheel                      = default.build_wheel
get_requires_for_build_sdist     = default.get_requires_for_build_sdist
get_requires_for_build_wheel     = default.get_requires_for_build_wheel
prepare_metadata_for_build_wheel = default.prepare_metadata_for_build_wheel
