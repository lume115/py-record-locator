# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

DEFAULT_BASE_CHARACTERS = "234679ACDEFGHJKLMNPRTUVWXYZ"


class RecordLocator:
    _base_characters = DEFAULT_BASE_CHARACTERS
    _mapped_integers = None

    def __init__(self, base_characters=None):
        if base_characters is not None:
            self._base_characters = base_characters

        self._mapped_integers = {v: k for k, v in enumerate(self._base_characters)}

    def encode(self, id_num):
        ints = []
        while id_num != 0:
            ints.insert(0, id_num % len(self._base_characters))
            id_num //= len(self._base_characters)
        rec = ""
        for i in ints:
            rec += self._base_characters[i]

        return rec

    def decode(self, rec):
        id_num = 0
        for i in rec.upper():
            id_num = (id_num * len(self._base_characters)) + self._mapped_integers[i]

        return id_num
