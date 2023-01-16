"""
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
"""

try:
    import pyperclip # to copy text to clipboard
except ImportError:
    pass # if pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher')

print('The Caesar Cipher encrypts letters by shifting them over by a key number.')
print('For example, a key of 2 means the letter A is encrypted into C,')
print('the letter B encrypted into D, and so on.')
print()

# Let the user enter if they encrypting or decrypting:
while True: # Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input("> ").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter the key to use:
while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Enter the message to encrypt/decrypt:
print('Enter the message to {}'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol) # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of 
        # symbols or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)

        elif num < 0:
            num = num + len(SYMBOLS)

        # add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]

    else:
        # Just add the symbol without encrypting/decrypting
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipboard.".format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed.

