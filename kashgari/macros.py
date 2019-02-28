# encoding: utf-8
"""
@author: BrikerMan
@contact: eliyar917@gmail.com
@blog: https://eliyar.biz

@version: 1.0
@license: Apache Licence
@file: macros.py
@time: 2019-01-19 09:58

"""
import bz2
import os
import pathlib
from enum import Enum
from pathlib import Path

import download

PAD = "[PAD]"
BOS = "[BOS]"
EOS = "[EOS]"
UNK = "[UNK]"

MARKED_KEYS = [PAD, BOS, EOS, UNK]

NO_TAG = 'O'

home = str(Path.home())

DATA_PATH = os.path.join(home, '.kashgari')
STORAGE_HOST = 'http://storage.eliyar.biz/'
PROCESSED_CORPUS_PATH = os.path.join(DATA_PATH, 'pre_processed')

pathlib.Path(PROCESSED_CORPUS_PATH).mkdir(parents=True, exist_ok=True)


class _Config(object):
    def __init__(self):
        self.use_CuDNN_cell = False


config = _Config()


class TaskType(Enum):
    classification = 'classification'
    tagging = 'tagging'


class DataSetType(Enum):
    train = 'train'
    test = 'test'
    validate = 'validate'


class SegmenterType(Enum):
    space = 'space'
    jieba = 'jieba'
    char = 'char'


URL_MAP = {
    'w2v.sgns.weibo.bigram': 'embedding/word2vev/sgns.weibo.bigram.bz2'
}


if __name__ == "__main__":
    from kashgari.utils.logger import init_logger
    init_logger()
