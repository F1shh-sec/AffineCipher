"""
Author: George Link
"""

def main():
    print("Welcome! Do you want to encode, decode, or get a quick cypher conversion string?")
    print('1. Encode')
    print('2. Decode')
    print('3. Cypher String')
    choice = input("> ")
    a = int(input('Please Enter A: '))
    b = int(input('Please Enter B: '))

    if choice == '1':
        z = input('Enter Encoded String: ').replace(" ", "")
        print(encode(a, b, z))
    elif choice == '2':
        z = input('Enter Encoded String: ').replace(" ", "")
        print(decode(a, b, z))
    elif choice == '3':
        print(getCipher(a, b).upper())
    else:
        print("Invalid choice.")
"""
Encodes a string using the Keys A and B
"""
def encode(a, b, string):
    charsnew = to_number(list(string.lower()))
    encoded = []
    for elm in charsnew:
        encoded.append(((a*(elm)+b)%26))
    return ''.join(to_letter(encoded))

"""
Decodes a string using the Keys A and B
"""
def decode(a,b, string):
    formatted_string = to_number(list(string.lower()))
    decoded = []
    for elm in formatted_string:
        decoded.append((pow(a, -1, 26)*(elm-b))%26)
    return ''.join(to_letter(decoded))

"""
Prints out a nice and pretty quick cipher for any two keys. 
"""
def getCipher(a, b):
    charsnew = []
    for i in range(0, 26):
        charsnew.append(i)
    Encoded = []
    for elm in charsnew:
        Encoded.append(((a*(elm)+b)%26))
    return ''.join(to_letter(Encoded))

"""
A0Z25 encodes a string
"""
def to_number(list):
    return [(ord(elm) - 97) for elm in list]
"""
A0Z25 decodes a string
"""
def to_letter(list):
    return [(chr(elm + 97)) for elm in list]



if __name__ == "__main__":
    main()