import time

Money = 20
Pet = 'N/A'
Hunger = 100
Health = 100
Thirst = 100
T = 1
Start = 0

print (f'Select a pet: Dog / Cat / Hamster')
select = input()
if select == 'Dog':
    Pet = 'Dog'
    print(f'Your pet = {Pet}')
    Pet_name = input()
    if Pet_name == Pet_name:
        print(f'Your name pet = {Pet_name}')
        while T == 1:
            Start = 1
            stats = input()
            if stats == 'Stats':
                print(f'Stats: Hunger: {Hunger} | Thirst: {Thirst} | Health: {Health} | Name: {Pet_name} | Pet: {Pet}')
        
if select == 'Cat':
    Pet = 'Cat'
    print(f'Your pet = {Pet}')
    Pet_name = input()
    if Pet_name == Pet_name:
        print(f'Your name pet = {Pet_name}')
        while T == 1:
            Start = 1
            stats = input()
            if stats == 'Stats':
                print(f'Stats: Hunger: {Hunger} | Thirst: {Thirst} | Health: {Health} | Name: {Pet_name} | Pet: {Pet}')
        
if select == 'Hamster':
    Pet = 'Hamster'
    print(f'Your pet = {Pet}')
    Pet_name = input()
    if Pet_name == Pet_name:
        print(f'Your name pet = {Pet_name}')
        while T == 1:
            Start = 1
            stats = input()
            if stats == 'Stats':
                print(f'Stats: Hunger: {Hunger} | Thirst: {Thirst} | Health: {Health} | Name: {Pet_name} | Pet: {Pet}')

while T == 1:
    if Start == 1:
        Hunger = Hunger - 1
        Thirst = Thirst - 1
        time.sleep(1)