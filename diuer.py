# -*- coding:utf-8 -*-
# ! /usr/bin/ env python

import constant
from wxpy import *
import random


class Diuer:
    __member = None
    __total_damage = 0
    __attack = 1
    __skill_point = 0

    def __init__(self, member: Member):
        self.__member = member

    def __str__(self):
        member = self.__member
        total_damage = self.__total_damage
        attack = self.__attack
        __skill_point = self.__skill_point
        return f'<Diuer: member: {member}, total_damage: {total_damage}, attack: {attack}, skill: {__skill_point}>'

    def get_member(self):
        return self.__member

    def upgrade(self):
        self.__attack += 1

    def get_attack(self):
        return self.__attack

    def add_skill_point(self):
        self.__skill_point += 1

    def get_skill_point(self):
        return self.__skill_point

    def use_yidao(self):
        if self.__skill_point >= constant.SKILL_COST['YIDAO']:
            self.__skill_point -= constant.SKILL_COST['YIDAO']
            dmg = random.randint(0, self.__attack) * constant.DIU_MAX
            self.__total_damage += dmg
            return dmg
        else:
            return 0

    def use_fate(self):
        if self.__skill_point >= constant.SKILL_COST['FATE']:
            self.__skill_point -= constant.SKILL_COST['FATE']
            dmg = random.randint(-self.__attack, self.__attack) * constant.DIU_MAX * 10 + 1
            self.__total_damage += dmg
            return dmg
        else:
            return 0

    def use_suoha(self):
        suoha_dmg = 0
        suoha_dmg += self.__skill_point * self.__attack * constant.DIU_MAX
        self.__skill_point = -9999
        self.__attack = 0
        return suoha_dmg

    def add_total_damage(self, damage):
        self.__total_damage += damage

    def get_total_damage(self):
        return self.__total_damage

    def reset(self, attack, skill):
        self.__attack = attack
        self.__skill_point = skill
        self.__total_damage = 0
