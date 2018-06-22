# -*- coding:utf-8 -*-
# ! /usr/bin/ env python

import constant
from wxpy import *


class Diuer:
    __member = None
    __total_damage = 0
    __attack = 1
    __skill = 0

    def __init__(self, member: Member):
        self.__member = member

    def __str__(self):
        member = self.__member
        total_damage = self.__total_damage
        attack = self.__attack
        skill = self.__skill
        return f'<Diuer: member: {member}, total_damage: {total_damage}, attack: {attack}, skill: {skill}>'

    def get_member(self):
        return self.__member

    def upgrade(self):
        self.__attack += 1

    def get_attack(self):
        return self.__attack

    def add_skill(self):
        self.__skill += 1

    def get_skill(self):
        return self.__skill

    def use_skill(self):
        if self.__skill > 0:
            self.__skill -= 1
            dmg = constant.DIU_MAX * self.__attack
            self.__total_damage += dmg
            return dmg
        else:
            return 0

    def add_total_damage(self, damage):
        self.__total_damage += damage

    def get_total_damage(self):
        return self.__total_damage

    def reset(self, attack, skill):
        self.__attack = attack
        self.__skill = skill
        self.__total_damage = 0
