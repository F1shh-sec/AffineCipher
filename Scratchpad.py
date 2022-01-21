def main():
   decode()

def decode():
    # z = list(input('Enter Encoded String'))
    # a = int(input('Please Enter A: '))
    # b = int(input('Please Enter B: '))
    z = list('zuqtqgsytqvrsdqztwvaoyajramjazi')
    a = 7
    b = 22
    print(f'Split: {z}')
    charsnew = to_number(z)
    print(f'To Letters: {charsnew}')
    afterMod = []
    for elm in charsnew:
        afterMod.append(((a * (elm) + b) % 26))
    print(f'After Mod: {afterMod}')
    print(f'back to letter: {to_letter(afterMod)}')

def getCipher(a, b):
    chars = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    charsnew = []
    for elm in chars:
        charsnew.append(elm - 1)
    print(charsnew)
    afterMod = []
    for elm in charsnew:
        afterMod.append(((a*(elm)+b)%26))
    print(afterMod)
    print(to_letter(afterMod))

def to_number(list):
    return [(ord(elm) - 97) for elm in list]

def to_letter(list):
    return [(chr(elm + 97)) for elm in list]

def printNewCipher():
    a = 'placeholder'



if __name__ == "__main__":
    main()