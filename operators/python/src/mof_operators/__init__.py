import abc
import argparse
import json
import pathlib


class Operator(abc.ABC):
    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("input", type=pathlib.Path)
        parser.add_argument("--secrets", type=pathlib.Path)
        args = parser.parse_args()

        input_ = read_data(args.input)
        secrets = read_data(args.secrets)

        self.operate(input_, secrets)

    @abc.abstractmethod
    def operate(self, input_, secrets):
        pass


def read_data(p: pathlib.Path):
    if not p:
        return None
    content = p.read_text()
    match p.suffix:
        case ".json":
            return json.loads(content)
        case ".yaml" | ".yml":
            try:
                import yaml
            except:
                assert False, "YAML not supported"
            return yaml.load(content, Loader=yaml.SafeLoader)
        case _:
            assert False, f"unknown suffix {p.suffix}"
