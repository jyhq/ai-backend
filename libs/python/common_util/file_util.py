import base64
import json
from functools import lru_cache
from io import BytesIO
from pathlib import Path
from PIL import Image
from ruamel.yaml import YAML


def get_ancestor_dir(caller_file: str, depth: int = 3) -> str:
    path = Path(caller_file).resolve()
    if depth >= len(path.parents):
        depth = len(path.parents) - 1
    return str(path.parents[depth])


def load_json_conf(path, use_cache=True):
    def _load():
        try:
            with open(path) as f:
                return json.load(f)
        except Exception as e:
            raise EnvironmentError(
                f"load json file '{path}' failed: {str(e)}"
            )
    if use_cache:
        @lru_cache(maxsize=10)
        def cached_load(path):
            return _load()
        return cached_load(path)
    return _load()


def load_yaml_conf(path, use_cache=True):
    def _load():
        try:
            yaml = YAML(typ='rt')
            with open(path, encoding="utf8") as f:
                return yaml.load(f)
        except Exception as e:
            raise EnvironmentError(
                f"load yaml file '{path}' failed: {str(e)}"
            )
    if use_cache:
        @lru_cache(maxsize=10)
        def cached_load(path):
            return _load()
        return cached_load(path)
    return _load()


def base64_to_image(image_b64, path):
    image_binary = base64.b64decode(image_b64)
    img = Image.open(BytesIO(image_binary))
    img.save(open(path, "wb"))
    return path
