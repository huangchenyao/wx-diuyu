# -*- coding:utf-8 -*-
# ! /usr/bin/ env python

from wxpy import *


class Yumou:
    __member = None
    __hp = 0

    def __init__(self, member: Member):
        self.__member = member

    def __str__(self):
        member = self.__member
        hp = self.__hp
        return f'<Yumou: member: {member}, hp: {hp}>'

    def injure(self, num):
        self.__hp -= num
        if self.__hp < 0:
            self.__hp = 0
        return self.__hp

    def heal(self, num):
        self.__hp += num

    def get_hp(self):
        return self.__hp

    def is_dead(self):
        return self.__hp <= 0

    def reset(self, hp):
        self.__hp = hp

    def get_member(self):
        return self.__member