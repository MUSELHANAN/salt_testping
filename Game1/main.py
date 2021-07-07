import threading

from Character import *
from mul_attack import *

if __name__=='__main__':
    player_name = input("Please input your player's name :")
    player = Character(player_name, 1, 150, 150, 15, 0, 1, 0.3, 0.3, 2, 0.5, 0)
    player.show_property()

    enemy1 = Character("skeleton")
    enemy1.show_property()

    player_nowlife = player.Get_nowlife()
    enemy1_nowlife = enemy1.Get_nowlife()

    while player_nowlife > 0:

        thread1 = threading.Thread(target=Battle, args=(player, enemy1))
        thread2 = threading.Thread(target=Battle, args=(enemy1, player))

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        WoL_judge(player, enemy1)
        player_nowlife = player.Get_nowlife()
        enemy1_nowlife = enemy1.Get_nowlife()

        if player_nowlife > 0 and enemy1_nowlife <= 0:
            print("CONGRATULATIONS! YOU WIN!")
            player.win_recover()
            player.level_up()
            player.show_property()
            player.power_up()
            player.show_property()

            enemy1.level_up()
            enemy1.reset_chatacter()
            enemy1.show_property()
        else:
            print("SORRY, YOU LOSE")
            break