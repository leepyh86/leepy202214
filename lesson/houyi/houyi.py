#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_houyi.py
# @time: 2022/1/4 18:54
# @author: leepy cham
from leepy202214.lesson.game.game import Game
class Houyi(Game):
    def __init__(self):
        super().__init__()
        self.defense = 99

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            if self.hp<=0:
                print("我输了")
                break;
            elif enemy_hp<=0:
                print("我赢了")
                break;
            else:
                print("对战中....")

hy = Houyi()
hy.houyi_fight(1000,100)



