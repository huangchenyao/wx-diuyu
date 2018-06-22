# -*- coding:utf-8 -*-
# ! /usr/bin/ env python

import time
import threading
import random
from diuer import *
from yumou import *
from wxpy import *
import constant

class Diu:
    __yumou = None
    __diuers = None
    __group = None
    __start = False
    __start_time = 0

    def __init__(self, yumou: Yumou, diuers: [], group: Group):
        self.__yumou = yumou
        self.__diuers = diuers
        self.__group = group

    def reset(self):
        self.__yumou.reset(constant.YU_MOU_HP_MAX)
        for diuer in self.__diuers:
            diuer.reset(1, 0)

    def start(self):
        self.reset()
        self.__start = True
        self.__start_time = int(time.time())
        threading.Thread(target=Diu.__count_down, args=(self,)).start()
        self.__group.send_msg(constant.START_GAME_MSG)

    def is_started(self):
        return self.__start

    def __count_down(self):
        hits = False
        while int(time.time()) < self.__start_time + constant.DIU_GAME_TIME:
            if self.__start_time + constant.DIU_GAME_TIME - int(time.time()) < 60 and not hits:
                hits = True
                self.__group.send_msg('游戏结束还剩1分钟')
            if self.__yumou.is_dead():
                break

        self.__start = False
        if self.__yumou.is_dead():
            self.__group.send_msg('游戏结束，恭喜大家丢死鱼某')
        else:
            self.__group.send_msg('游戏结束，这都没丢死？')

        rank_msg = '排行榜：\n'
        max_diuer1 = self.__find_max_dmg_diuer(float('inf'))
        rank_msg += (f'{1}. {max_diuer1.get_member().name:s}，共计{max_diuer1.get_total_damage():d}伤害\n')
        max_diuer2 = self.__find_max_dmg_diuer(max_diuer1.get_total_damage())
        if max_diuer2:
            rank_msg += (f'{2}. {max_diuer2.get_member().name:s}，共计{max_diuer2.get_total_damage():d}伤害\n')
            max_diuer3 = self.__find_max_dmg_diuer(max_diuer2.get_total_damage())
            if max_diuer3:
                rank_msg += (f'{3}. {max_diuer3.get_member().name:s}，共计{max_diuer3.get_total_damage():d}伤害\n')
        self.__group.send_msg(rank_msg)

    def __find_diuer(self, member: Member):
        for diuer in self.__diuers:
            if diuer.get_member() == member:
                return diuer

    def save_yu(self, msg: Message):
        if msg.text == constant.YU_MOU_HEAL_MSG:
            heal_hp = constant.YUMOU_HEAL_HP + int(pow(constant.YU_MOU_HP_MAX - self.__yumou.get_hp(), 0.5))
            rest_hp = self.__yumou.heal(heal_hp)
            self.__group.send_msg(f'吨吨吨，鱼某HP +{heal_hp:d}，剩余HP {rest_hp:d}')

    def diu_yu_mou(self, msg: Message):
        if msg.text == constant.DIU_SKILL_NAME:
            if self.__yumou.is_dead():
                self.__group.send_msg('鱼某已死')
                return

            diuer = self.__find_diuer(msg.member)
            yi_dao_dmg = diuer.use_skill()
            if yi_dao_dmg:
                rest_hp = self.__yumou.injure(yi_dao_dmg)
                self.__group.send_msg(f'{msg.member.name:s}一刀鱼某，HP -{yi_dao_dmg:d}，剩余HP {rest_hp:d}')
            else:
                self.__group.send_msg(f'{msg.member.name:s}还没有获得一刀斩')

        diu_dmg = Diu.__diu_yu_time(msg.text)
        if diu_dmg > 0:
            if self.__yumou.is_dead():
                self.__group.send_msg('鱼某已死')
                return

            diuer = self.__find_diuer(msg.member)
            diu_dmg *= diuer.get_attack()
            diu_dmg %= (constant.DIU_MAX * diuer.get_attack())
            rest_hp = self.__yumou.injure(diu_dmg)
            diuer.add_total_damage(diu_dmg)
            res_msg = f'{msg.member.name:s}丢鱼某，HP -{diu_dmg:d}(MAX{(constant.DIU_MAX * diuer.get_attack())})，剩余HP {rest_hp:d}'
            if random.randint(0, 100) < (1 - pow(1 - constant.UPDATE_RATE, constant.DIU_MAX)) * 100:
                diuer.upgrade()
                res_msg += f'，升级了，攻击力+1，当前 {diuer.get_attack():d}'
            if random.randint(0, 100) < (1 - pow(1 - constant.SKILL_RATE, constant.DIU_MAX)) * 100:
                diuer.add_skill()
                res_msg += f'，获得了技能鱼某一刀斩（消耗性），剩余{diuer.get_skill():d}刀'
            self.__group.send_msg(res_msg)

    @staticmethod
    def __diu_yu_time(text: str):
        count = 0
        for i in constant.DIU_YU_MSG:
            count += text.count(i)
        return count

    def __find_max_dmg_diuer(self, up):
        max_dmg = 0
        max_dmg_diuer = None
        for diuer in self.__diuers:
            if max_dmg < diuer.get_total_damage() < up:
                max_dmg = diuer.get_total_damage()
                max_dmg_diuer = diuer
        return max_dmg_diuer