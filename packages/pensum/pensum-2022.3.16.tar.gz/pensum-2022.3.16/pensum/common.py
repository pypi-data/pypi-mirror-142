#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Docstring!
"""

# Imports ===============================================================#

import importlib.resources as pkg_resources

from pathlib import Path

from typing import Union, Optional

import pensum.topics as topics

# Variables globales ====================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

PathOrString = Union[Path, str]
StringOrNone = Optional[str]

# Fonctions =============================================================#


def load_topic(name: str) -> str:
    """
    Load Pensum help topic from markdown source in Pensum package.
    """
    return pkg_resources.read_text(topics, f"{name}.md")


# vim:set shiftwidth=4 softtabstop=4:
