# -*- coding:utf-8 -*-
# ! /usr/bin/ env python

from wxpy import *
import time
import random
import threading
import constant
from diuer import *
from yumou import *
from diu import *

if __name__ == '__main__':
    bot = Bot(console_qr=False)
    diu_yu_group = list(filter(lambda x: x.self.name == 'FFGM', bot.groups()))[0]
    diu_yu_group.send_msg(constant.BOOT_MSG)
    yu_mou = Yumou(bot.friends().search('余凯欢')[0])
    while True:
        princess_index = random.randint(0, len(diu_yu_group.members))
        if diu_yu_group.members[princess_index] not in [yu_mou.get_member(), bot.self]:
            princess = diu_yu_group.members[princess_index]
            break
    diuers = []
    for member in diu_yu_group.members:
        if member != yu_mou:
            diuers.append(Diuer(member))
    diu_game = Diu(yu_mou, diuers, diu_yu_group)
    diu_yu_group.send_msg(constant.BOOT_FIN_MSG)

    @bot.register(diu_yu_group)
    def diu_ni_yu(msg: Message):
        if constant.PRINT_ALL:
            print(msg)
        if diu_game.is_started():
            if msg.member == yu_mou.get_member() or msg.member == princess:
                diu_game.save_yu(msg)
            else:
                diu_game.diu_yu_mou(msg)
        else:
            if msg.text == constant.START_GAME_MSG:
                diu_game.start()
                diu_yu_group.send_msg(f'本轮公主为：@{princess.name:s}')

    embed()
