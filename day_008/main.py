# Project - 8 caesar cipher
# link - https://en.wikipedia.org/wiki/Caesar_cipher
# link : http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
# eg : decode - ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl | shift = 5

from day_008 import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cipher_text = ""
plain_text = ""
quit_the_app = False

print(art.logo)


def encrypt(text, shift):
    encoded_word = ''
    for index in range(0, len(text)):

        letter = text[index]

        if letter in alphabet:
            letter_current_index = alphabet.index(letter)
            letter_new_index = letter_current_index + shift

            if letter_new_index > 25:
                letter_new_index -= 26
            encoded_word += alphabet[letter_new_index]

        else:
            encoded_word += letter

    return encoded_word


def decrypt(text, deshift):
    decoded_text = ""
    for index in range(0, len(text)):

        letter = text[index]

        if letter in alphabet:
            letter_current_index = alphabet.index(letter)
            letter_new_index = letter_current_index - deshift

            if letter_new_index < 0:
                letter_new_index += 26
            decoded_text += alphabet[letter_new_index]


        else:
            decoded_text += letter

    return decoded_text


while not quit_the_app:

    direction = input("Type 'encode'(right shift) to encrypt, type 'decode'(left shift) to decrypt:\n").lower()

    if direction == 'encode' or direction == 'decode':
        input_text = input("Type your message:\n").lower()
        input_shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            cipher_text += encrypt(text=input_text, shift=input_shift)
            print(f"Here's the encoded result : {cipher_text}")
            cipher_text = ""

        else:
            plain_text += decrypt(text=input_text, deshift=input_shift)
            print(f"Here's the encoded result : {plain_text}")
            plain_text = ""
    else:
        print("Choice is incorrect. Choose the correct one")
        continue

    should_continue = True
    while should_continue:
        status = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").upper()

        if status == "NO":
            quit_the_app = True
            print("Goodbye")

        elif status == "YES":
            should_continue = False

        else:
            print("Choice is incorrect. Choose the correct one")
