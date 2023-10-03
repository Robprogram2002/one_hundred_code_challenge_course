alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text.

def encrypt(message: str, shift_number: int, direction: str):
    if direction == "decode":
        shift_number = shift_number * (-1)

    mess_list = list(message)
    for n in range(len(mess_list)):
        char = mess_list[n]
        if char in alphabet:
            index = alphabet.index(char)
            index = (index + shift_number) % len(alphabet)
            mess_list[n] = alphabet[index]

    print(f"Here's the {direction}d result: {''.join(mess_list)}")


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt(text, shift, direction)


should_end = False
while not should_end:
    caesar_cipher()

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
