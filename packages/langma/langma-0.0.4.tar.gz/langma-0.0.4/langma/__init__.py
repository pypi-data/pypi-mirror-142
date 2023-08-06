# *_*coding:utf-8 *_*

from .__version__ import version, __version__
from typing import Any, Dict

custom_objects: Dict[str, Any] = {}

from langma import corpus, embeddings, layers, macros, processors, tasks, utils
from langma.macros import config

custom_objects = layers.resigter_custom_layers(custom_objects)
