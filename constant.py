BOOT_MSG = '''>>>>>>>>>>>>>>>>>>
    丢鱼v2.4版
    i. 技能统一改成技能点形式
   ii. "鱼某一刀斩"消耗1点
  iii. 新增技能"命运的抉择"消耗5点
   iv. 鱼某新增被动，血量低于30%会进入狂怒状态，免疫部分伤害
玩法介绍：
1. 输入"开始丢鱼"开始一局丢鱼游戏
2. 倒计时10分钟
3. 输入"丢鱼等字眼"可以丢鱼
4. 连击有可能升级，以及获得技能点
5. 鱼某和公主可以输入秘籍（求丢）给自己治疗
<<<<<<<<<<<<<<<<<<
启动中......
'''
BOOT_FIN_MSG = '启动完毕！'
YU_MOU_HP_MAX = pow(10, 5)
DIU_GAME_TIME = 60 * 10
START_GAME_MSG = '开始丢鱼'
DIU_YU_MSG = ['丢鱼', '丢🐟', '丢🐠', '丢🎣',
              '丢你鱼', '丢你🐟', '丢你🐠', '丢你🎣',
              '草泥鱼', '草泥🐟', '草泥🐠', '草泥🎣']
SKILL_NAME = {
    'YIDAO': '鱼某一刀斩',
    'FATE': '命运的抉择'
}
SKILL_COST = {
    'YIDAO': 1,
    'FATE': 5
}
YU_MOU_HEAL_MSG = '求丢'
DIU_MAX = 100
UPDATE_RATE = 0.003
SKILL_RATE = 0.0015
YUMOU_HEAL_HP = 10
PRINT_ALL = False
