#import Special_power

class Character:

    def __init__(self, name="Player1", level=1, max_life=100, now_life=100, ACK=10, DEF=0, SPD=0, CRS=0.0,
                 ARC=0.0, ARD=0, DDR=0, AP=0):
        #显示的属性
        self.__name = name
        self.__level = level      #等级
        self.__max_life = max_life        #最大生命值
        self.__now_life = now_life        #当前生命值
        self.__MAX_ACK = ACK      #白字攻击力
        self.__ACK = ACK          #当前攻击力
        self.__MAX_DEF = DEF      #白字防御力
        self.__DEF = DEF  # 当前防御力
        self.__MAX_SPD = SPD  # 白字速度
        self.__SPD = SPD  # 当前速度
        self.__MAX_CRS = CRS  # 白字暴击率
        self.__CRS = CRS  # 暴击率
        self.__MAX_ARC = ARC  # 白字攻击吸血倍率
        self.__ARC = ARC  # 攻击吸血倍率
        self.__MAX_ARD = ARD  # 白字暴击伤害倍率
        self.__ARD = ARD  # 暴击伤害倍率
        self.__MAX_DDR = DDR  # 白字闪避率
        self.__DDR = DDR  # 闪避率
        self.__AP = AP          #属性点

        #异常状态
        self.__ArmourStatus = 0
        self.__Poison_number = 0
        self.__Burning_number = 0
        self.__Frozen_number = 0
        self.__Paralysis_number = 0
        self.__Binding_number = 0
        self.__Dark_damage = 0

    def Get_name(self):
        return self.__name
    def Get_level(self):
        return self.__level
    def Get_maxlife(self):
        return self.__max_life
    def Get_nowlife(self):
        return self.__now_life
    def Get_MAX_ACK(self):
        return self.__MAX_ACK
    def Get_ACK(self):
        return self.__ACK
    def Get_MAX_DEF(self):
        return self.__MAX_DEF
    def Get_DEF(self):
        return self.__DEF
    def Get_MAX_SPD(self):
        return self.__MAX_SPD
    def Get_SPD(self):
        return self.__SPD
    def Get_MAX_CRS(self):
        return self.__MAX_CRS
    def Get_CRS(self):
        return self.__CRS
    def Get_MAX_ARC(self):
        return self.__MAX_ARC
    def Get_ARC(self):
        return self.__ARC
    def Get_MAX_ARD(self):
        return self.__MAX_ARD
    def Get_ARD(self):
        return self.__ARD
    def Get_MAX_DDR(self):
        return self.__MAX_DDR
    def Get_DDR(self):
        return self.__DDR
    def Get_AP(self):
        return self.__AP


    def Get_ArmourStatus(self):
        return self.__ArmourStatus
    def Get_PoisonStatus(self):
        return self.__Poison_number
    def Get_BurningStatus(self):
        return self.__Burning_number
    def Get_FrozenStatus(self):
        return self.__Frozen_number
    def Get_ParalysisStatus(self):
        return self.__Paralysis_number
    def Get_BindingStatus(self):
        return self.__Binding_number
    def Get_DarkStatus(self):
        return self.__Dark_damage


    def reset_chatacter(self):
        self.__max_life += 30
        self.__now_life = self.__max_life
        self.__ACK += 1
        self.__DEF += 1
        self.__SPD = 0
        self.__CRS = 0
        self.__ARC = 0
        self.__ARD = 0
        self.__DDR = 0
        self.__AP = 0

    def show_property(self):
        print("NAME             " + self.__name)
        print("LEVEL            " + str(self.__level))
        print("LIFE/MAX LIFE    " + str(round(self.__now_life, 0)) + '/' + str(self.__max_life))
        print("ACK              " + str(self.__ACK))
        print("DEF              " + str(self.__DEF))
        print("SPD              " + str(self.__SPD))
        print("CRS              " + str(self.__CRS))
        print("ARC              " + str(self.__ARC))
        print("ARD              " + str(self.__ARD))
        print("DDR              " + str(self.__DDR))
        print("AP               " + str(self.__AP) + "\n")

    def level_up(self):
        self.__level += 1
        self.__AP += 1

    def power_up(self):
        k = 1
        while k:
            print("Please choose your atribute to promote :")
            print("1: max_life + 50; 2: ACK + 5; 3: DEF + 5; 4: SPD + 1; 5: CRS + 0.1(nonlinearity); 6: ARC + 0.1")
            n = int(input())
            if n==1:
                self.__max_life += 50
                self.__now_life += 50
                k=0
            elif n==2:
                self.__MAX_ACK += 5
                self.ACK = self.__MAX_ACK
                k=0
            elif n==3:
                self.__MAX_DEF += 5
                self.DEF = self.__MAX_DEF
                k=0
            elif n==4:
                self.__MAX_SPD += 1
                self.SPD = self.__MAX_SPD
                k=0
            elif n==5:
                if self.__CRS == 0:
                    self.__CRS += 0.1
                else:
                    self.__CRS += (1-self.__CRS)*0.1
                k=0
            elif n==6:
                self.__ARC += 0.1
                k=0
            else:
                print("Please input the right number(like 1)")
                k=0
        self.__AP -= 1

    def win_recover(self):
        #战斗结束，防御力、速度、攻击力变为原来的值
        self.__DEF = self.__MAX_DEF
        self.__SPD = self.__MAX_SPD
        self.__ACK = self.__MAX_ACK
        self.__CRS = self.__MAX_CRS
        self.__ARC = self.__MAX_ARC
        self.__ARD = self.__MAX_ARD
        self.__DDR = self.__MAX_DDR

        #异常状态恢复
        self.__Poison_number = 0
        self.__burning_number = 0
        self.__frozen_number = 0
        self.__paralysis_number = 0
        self.__binding_number = 0

        self.health_recover(self.__max_life*0.3)
        self.health_correction()

    def health_recover(self, recover_number):
        self.__now_life += recover_number
        self.health_correction()

    def health_correction(self):
        if self.__now_life > self.__max_life:
            self.__now_life = self.__max_life

    def taked_damage(self, damage):
        self.__now_life -= damage
        self.ld_judement()

    def ld_judement(self):
        if self.__now_life < 0:
            self.__now_life = 0
