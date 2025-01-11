alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser_cipher(string, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % len(alphabet)]
                  if sym in alphabet else sym)
                  for sym in string]
    new_str = ''.join(char_list)
    return new_str

user_text = input('Please input your text: ')
user_shift = int(input('Please input your shift: '))
processed_text = caeser_cipher(user_text, user_shift)
print('Your new text: ', processed_text)