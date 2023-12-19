from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    t = []
    for l in text:      
        if l in alphabet:
            i = alphabet.index(l)
            if direction == 'encode':
                s0 = i + shift
                s1 = i + shift - 26
            elif direction == 'decode':
                s0 = i - shift
                s1 = i - shift + 26           
            try:
                t.append(alphabet[s0])
            except:
                t.append(alphabet[s1])
        else:
            t.append(l)
    print(f"Here's the {direction}d result: {''.join(t)}")

print(logo)
c = 'yes'

while c == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(direction,text,shift)
    c = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
