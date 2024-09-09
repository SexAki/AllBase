import random




def function():
    max = 1
    pos = 0
    var = 0.5
    rand = 0
    rand=loop()
   

    while pos != rand:
        if rand < pos:
            pos = pos - var
            if pos > rand:
                print(f'{pos-rand}')
                pos = int(pos)

            if var <= max:
                var = var * 1.1
            else:
                var = var * 0.9
        else:
            pos = pos + var
            if pos < rand:
                print(f'{pos-rand}')
                pos = int(pos)

            if var <= max:
                var = var * 1.1
            else:
                var = var * 0.9



def loop():
    rand = random.randint(-10,10)
    return rand


function()