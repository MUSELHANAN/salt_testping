import time
from Character import *
from mul_attack import *

def Armour_reduction(Character):        #破甲，敌人防御减半，在攻击判定后、伤害判定前结算
    Character.DEF = Character.DEF/2

def Continuous_attack(Character1, Character2):      #连续攻击，在攻击判定后结算
    print(Character1.name + " attacks again!")
    #Attack_Damage(Character1, Character2)

def poison_damage(Character):       #异常状态：中毒，每层造成10点伤害，无视防御、护甲、闪避，在敌人行动前进行伤害判定
    Character.now_life -= Character.Poison_number*10

def burning(Character):     #异常状态：灼烧，每层造成5%当前生命值的伤害，无视防御、闪避，不无视护甲，在敌人行动前进行伤害判定
    Character.now_life -= Character.now_life*Character.burning_number*0.05

def frozen(Character):      #异常状态，冰冻，每层降低10%攻击速度，叠满5层给予攻击者攻击力3倍伤害，并眩晕6s，叠满5层的效果在叠满时结算
    if Character.frozen_number > 0 and Character.frozen_number <5:
        Character.SPD = Character.MAX_SPD - Character.MAX_SPD * Character.frozen_number * 0.1
    elif Character.frozen_number == 5:
        Character.frozen_number = 0
        time.sleep(3)

def paralysis(Character1,Character2):       #异常状态：麻痹，每层降低10%攻击力
    # 叠满5层后清空该debuff，给予攻击者6倍攻击力的伤害，并眩晕3s，叠满5层的效果在叠满时结算
    if Character2.paralysis_number > 0 and Character2.paralysis_number < 5:
        Character2.ACK = Character2.MAX_ACK - Character2.MAX_ACK * Character2.paralysis_number * 0.1
    elif Character2.paralysis_number == 5:
        Character2.paralysis_number = 0
        Character2.now_life -= Character1.ACK*10
        time.sleep(3)

def Blinding(Character):        #光属性异常状态：致盲，降低敌人的命中率，在伤害判定后结算
    pass

def dark_attack(Character1,Character2):     #暗属性伤害，无视防御、护甲、闪避的真实伤害，在伤害判定后结算
    Character2.now_life -= Character1.dark_damage


