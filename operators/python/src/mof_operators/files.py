import pathlib

import jinja2

import mof_operators


class FilesOperator(mof_operators.Operator):
    def operate(self, input_, secrets):
        env = jinja2.Environment(undefined=jinja2.StrictUndefined, keep_trailing_newline=True)
        vars = input_["variables"] | ( secrets or {})
        for path, template in input_["files"].items():
            pathlib.Path(path).write_text(env.from_string(template).render(**vars))

def main():
    FilesOperator().run()
