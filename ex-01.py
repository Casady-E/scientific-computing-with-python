#text = 'Hello World'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#index = alphabet.find(text[0].lower())
#print(index)
#shifted = alphabet[index + shift]
#print(shifted)

#encrypted_text = ''

#for char in text.lower():
#    if char == ' ':
#       encrypted_text += char
#    index = alphabet.find(char)
#    new_index = index + shift
#    encrypted_text += alphabet[new_index]
#    print('char:', char, 'encrypted text:', encrypted_text)

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 13)