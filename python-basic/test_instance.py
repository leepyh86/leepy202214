#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: test_instance.py.py
# @time: 2022/1/4 16:27
# @author: leepy cham


class Houyi(Game):
    def __int__(self):
        self.defense=100
        super().__init__(1000,200)

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            if self.hp<=0:
                print("我输了")
            else:
                print("我赢了")







