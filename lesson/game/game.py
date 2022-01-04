#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @file: game.py
# @time: 2022/1/4 18:55
# @author: leepy cham

class Game:
    def __init__(self):
        self.hp=1000
        self.power=200

    def fight(self,enemy_hp,enemy_power):
        my_final_hp = hp-enemy_power
        enemy_final_hp=enemy_hp-enemy_power
        if(my_final_hp>enemy_final_hp):
            print("我赢了")
        elif(my_final_hp == enemy_final_hp):
            print("打平了")
        else:
            print("对方赢了")
