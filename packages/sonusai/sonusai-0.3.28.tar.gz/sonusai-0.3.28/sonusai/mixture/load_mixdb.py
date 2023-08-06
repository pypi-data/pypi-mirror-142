import json
from os.path import exists

from sonusai import SonusAIError
from sonusai import logger


def load_mixdb(name: str) -> dict:
    if not exists(name):
        logger.error(f'{name} does not exist')
        raise SonusAIError

    with open(name, encoding='utf-8') as f:
        mixdb = json.load(f)

    return mixdb
