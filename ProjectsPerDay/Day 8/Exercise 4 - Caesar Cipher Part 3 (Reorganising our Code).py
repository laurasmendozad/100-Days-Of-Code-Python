alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(direction,text,shift):
    t = []
    for l in text:
        if l != ' ':
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
            t.append(' ')

    print(f"Here's the {direction}d result: {''.join(t)}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction,text,shift)