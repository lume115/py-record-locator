# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

DEFAULT_BASE_CHARACTERS = "234679ACDEFGHJKLMNPRTUVWXYZ"


class ChecksumException(Exception):
    pass


class RecordLocator:
    _base_characters = DEFAULT_BASE_CHARACTERS
    _mapped_integers = None
    _has_check_digit = False
    _prime = 0

    def __init__(self, base_characters=None, has_check_digit=False):
        if base_characters is not None:
            self._base_characters = base_characters

        self._has_check_digit = has_check_digit
        self._mapped_integers = {v: k for k, v in enumerate(self._base_characters)}
        self._prime = len(self._base_characters) + 1

    def encode(self, id_num):
        ints = []
        id_num_mod = id_num
        while id_num_mod != 0:
            ints.insert(0, id_num_mod % len(self._base_characters))
            id_num_mod //= len(self._base_characters)
        rec = ""
        for i in ints:
            rec += self._base_characters[i]

        if self._has_check_digit:
            rec += self._generate_check_digit(ints)

        return rec

    def decode(self, rec):
        id_num = 0
        end = -1 if self._has_check_digit else None
        for i in rec.upper()[:end]:
            id_num = (id_num * len(self._base_characters)) + self._mapped_integers[i]

        if self._has_check_digit:
            if not self._is_valid_checksum(rec):
                raise ChecksumException("Incorrect checksum for {}".format(rec))

        return id_num

    def _generate_check_digit(self, ints):
        checksum = 0
        for i, v in enumerate(ints):
            checksum+=v*(i+1)

        return self._base_characters[checksum % len(self._base_characters)]

    def _is_valid_checksum(self, rec):
        ints = [self._mapped_integers[r] for r in rec[:-1]]
        return self._generate_check_digit(ints) == rec[-1:]
