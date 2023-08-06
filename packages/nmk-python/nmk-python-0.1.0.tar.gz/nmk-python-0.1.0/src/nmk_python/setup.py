import shutil
from configparser import ConfigParser
from pathlib import Path
from typing import List

from jinja2 import Environment, Template, meta
from nmk.model.builder import NmkTaskBuilder
from nmk.model.keys import NmkRootConfig


class PythonSetupBuilder(NmkTaskBuilder):
    def relative_path(self, v: str) -> str:
        # Make it project relative if possible
        v_path = Path(str(v))
        if v_path.is_absolute():
            try:
                return v_path.relative_to(self.model.config[NmkRootConfig.PROJECT_DIR].value).as_posix()
            except ValueError:  # pragma: no cover
                # Simply ignore, non project -relative
                pass
        return v

    def config_value(self, config_name: str):
        # Get value
        v = self.model.config[config_name].value

        # Value processing depends on type
        if isinstance(v, str):
            # Single string
            return self.relative_path(v)
        elif isinstance(v, list):
            # Potentially a list of string
            return [self.relative_path(p) for p in v]

        # Probably nothing to do with path, use raw value
        return v

    def build(self, setup_py_template: str, setup_cfg_files: List[str]):
        # Copy setup.py
        setup_py_output = self.outputs[0]
        shutil.copyfile(Path(setup_py_template), setup_py_output)

        # Merge setup fragments to generate final setup
        setup_cfg_output = self.outputs[1]
        c = ConfigParser()
        for f_path in map(Path, setup_cfg_files):
            # Consider any fragment as a template
            with f_path.open("r") as f:
                setup_source = f.read()

            # Look for required config items
            required_items = meta.find_undeclared_variables(Environment().parse(setup_source))
            unknown_items = list(filter(lambda x: x not in self.model.config, required_items))
            assert len(unknown_items) == 0, f"Unknown config items referenced from python setup fragment {f_path}: {', '.join(unknown_items)}"

            # Finally update config with rendered template
            c.read_string(Template(setup_source).render({c: self.config_value(c) for c in required_items}))
        with setup_cfg_output.open("w") as f:
            c.write(f)
