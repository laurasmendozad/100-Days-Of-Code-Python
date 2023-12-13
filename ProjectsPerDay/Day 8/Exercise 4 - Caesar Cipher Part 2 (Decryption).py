alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = []
    for l in text: 
        if l != ' ':
            i = alphabet.index(l)
            try:
                encrypted_text.append(alphabet[i+shift])
            except:
                encrypted_text.append(alphabet[i+shift-26])
        else:
            encrypted_text.append(' ')
    print(f"{''.join(encrypted_text)}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text,shift):

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    decrypted_text = []
    for l in text: 
        if l != ' ':
            i = alphabet.index(l)
            try:
                decrypted_text.append(alphabet[i-shift])
            except:
                decrypted_text.append(alphabet[i-shift+26])
        else:
            decrypted_text.append(' ')
    print(f"{''.join(decrypted_text)}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text,shift)