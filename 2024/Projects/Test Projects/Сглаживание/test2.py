import random
import time

HP = 10 # Player Health
En_HP = 10 # Enemy Health
Min_damage = 2 # Minimum damage
Max_damage = 5 # Maximum damage
Heal_items = 3 # Items Count
Heal = 3 # How do Items you heal

def loop(HP,En_HP,Min_damage,Max_damage,Heal_items,Heal):
    while HP > 0 or En_HP > 0:
        if HP > 0:
            if En_HP > 0:
                x = input()
                if x == "punch":
                    En_HP = En_HP - random.randint(Min_damage, Max_damage)
                    print(f'Your HP = {HP} | Enemy HP = {En_HP} | Items = {Heal_items}')
                    time.sleep(random.randint(1,3))
                    HP = HP - random.randint(Min_damage, Max_damage)
                    print(f'Your HP = {HP} | Enemy HP = {En_HP} | Items = {Heal_items}')
                if x == "heal" and Heal_items > 0:
                    HP = HP + 3
                    if HP > 10:
                        HP = 10
                    Heal_items = Heal_items - 1
                    print(f'Your HP = {HP} | Enemy HP = {En_HP} | Items = {Heal_items}')
            else:
                print(f'[ You Won! ]')
                break
        else:
            print(f'[ Game Over! ]') 
            break
        

loop(HP,En_HP,Min_damage,Max_damage,Heal_items,Heal)

print(f'Your HP = {HP} | Enemy HP = {En_HP} | Items = {Heal_items}')