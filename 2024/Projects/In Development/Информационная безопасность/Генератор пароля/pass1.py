import random
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special=['_', '-', '{','}','[',']','_','@','(',')','$','%','+','.', '*', '?', '"', '<', '>', '|']

def pass_gen(alphabets=alphabets,special=special):
    result = ''
    for i in range(0,18):
        randoms = random.randint(1,6)
        if randoms <= 3:
            id = random.randint(0, len(alphabets)-1)
            result += str(alphabets[id])
        if randoms >= 4:
            id = random.randint(0, len(alphabets)-1)
            result += str(alphabets[id]).lower()
        if randoms == 5:
            id = random.randint(0, len(special)-1)
            result += str(special[id])
        if i == 17:
            return result

password = pass_gen(alphabets,special)

print(f'Your Password: {password} | len={len(password)}')
