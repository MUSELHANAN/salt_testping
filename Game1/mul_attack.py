import time
import random
from Character import Character

#全局变量，用于在一个线程结束时，停止另外一个线程
life_judgment = 1

def judgement_recover(Character1, recover_numbers):
    name1 = Character1.Get_name()
    nowlife1 = Character1.Get_nowlife()
    Character1.health_recover(recover_numbers)
    print(name1 + " recovers " + str(recover_numbers) + " health points. Now " + name1 + " has " + nowlife1 +
          " health points")

def Attack_Damage(Character1, Character2):

    name1 = Character1.Get_name()
    name2 = Character2.Get_name()

    nowlife1 = Character1.Get_nowlife()
    nowlife2 = Character2.Get_nowlife()

    ACK1 = Character1.Get_ACK()
    ACK2 = Character2.Get_ACK()
    DEF1 = Character1.Get_DEF()
    DEF2 = Character2.Get_DEF()
    CRS1 = Character1.Get_CRS()
    CRS2 = Character2.Get_CRS()
    ARC1 = Character1.Get_ARC()
    ARC2 = Character2.Get_ARC()
    ARD1 = Character1.Get_ARD()
    ARD2 = Character2.Get_ARD()
    DDR1 = Character1.Get_DDR()
    DDR2 = Character2.Get_DDR()

    #判断是否闪避
    Is_dodge = random.random()
    if DDR2 >= Is_dodge:
        print(name1 + " is attacking! But " + name2 + " dodges this attck!")
    else:
        #判断是否暴击
        Is_critical = random.random()
        if CRS1 > Is_critical:
            damage = (ACK1 - DEF2) * ARD1
            print(name1 + " makes a critical hit! ")
        else:
            damage = ACK1 - DEF2
            print(name1 + " is attacking! ")

        if damage > 1:
            nowlife2 -= damage
            Character2.taked_damage(damage)
            #战斗流程、伤害、剩余血量显示
            if nowlife2 > 0:
                print(name2 + " takes " + str(damage) + " damage!" + name2 + " still has " +
                      str(round(nowlife2, 0)) + " health poits.")
            else:
                print(name2 + " takes " + str(damage) + " damage!" + name2 +
                      " still has 0 health poits.")
        else:
            #攻击力小于敌人防御力的场景下，该次伤害强制为1
            nowlife2 -= 1
            Character2.taked_damage(1)
            print(name2 + " takes 1 damage!"+ name2 + " still has " +
                  str(nowlife2) + " health poits.")

        if ARC1 != 0:
            judgement_recover(Character1, damage*ARC1)

    return 0

def Battle(a,b):

    nowlife1 = a.Get_nowlife()
    nowlife2 = b.Get_nowlife()

    life_judgment = 1
    delay = speed_judge(a)
    time.sleep(delay)
    while nowlife1 > 0 and nowlife2 > 0:
        if life_judgment == 1:
            Attack_Damage(a, b)
            delay = speed_judge(a)
            time.sleep(delay)
            nowlife1 = a.Get_nowlife()
            nowlife2 = b.Get_nowlife()
        else:
            break

def speed_judge(Character):

    SPD = Character.Get_SPD()

    if SPD == 0:
        interval = 2
    elif SPD > 0:
        interval = 1/SPD + 0.8
    else:
        interval = 1/SPD + 3.2
    return interval

def WoL_judge(Character1,Character2):
    name1 = Character1.Get_name()
    name2 = Character2.Get_name()

    nowlife1 = Character1.Get_nowlife()
    nowlife2 = Character2.Get_nowlife()

    if nowlife1 <= 0:
        print(name1 + " is defeated!")
        life_judgment = 0
    else:
        print(name2 + " is defeated!")
        life_judgment = 0
    pass
