import json
from os.path import exists
from typing import List

from sonusai import SonusAIError
from sonusai import logger


def load_mixid(name: str, mixdb: dict) -> List[int]:
    if not name:
        mixid = list(range(len(mixdb['mixtures'])))
    else:
        if not exists(name):
            logger.exception(f'{name} does not exist')
            raise SonusAIError

        with open(name, encoding='utf-8') as f:
            mixid = json.load(f)
            if not isinstance(mixid, dict) or 'mixid' not in mixid.keys():
                logger.exception(f'Could not find ''mixid'' in {name}')
                raise SonusAIError
            mixid = mixid['mixid']

    return mixid
