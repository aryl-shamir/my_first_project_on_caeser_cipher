from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    out_put = ""
    if encode_or_decode == "decode":
        shift_amount *= -1


    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            out_put += new_letter
        else:
            out_put += letter

    print(f"here is the {encode_or_decode} results: {out_put}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:")
    shift = int(input("Type the shift number:"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again, otherwise type 'no'").lower()

    if restart == "no":
        should_continue = False
        print("Good bye")









