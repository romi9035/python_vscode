from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# encrypt_str = ''
# decrypt_str = ''


# def encrypt(text, shift):
#     global encrypt_str
#     for i in text:
#         pos = alphabet.index(i)
#         indx = pos + shift
#         if indx >= len(alphabet):
#             indx = indx - len(alphabet)
#         encrypt_str += alphabet[indx]
#     print(f"The encoded text is {encrypt_str}")


# def decrypt(text, shift):
#     global decrypt_str
#     for i in text:
#         pos = alphabet.index(i)
#         indx = pos - shift
#         # if indx >= len(alphabet):
#         #     indx = indx - len(alphabet)
#         decrypt_str += alphabet[indx]
#     print(f"The decoded text is {decrypt_str}")


# if direction.lower() == 'decode':
#     decrypt(text, shift)
# elif direction.lower() == 'encode':
#     encrypt(text, shift)
# else:
#     print("Wrong input direction")

def caesar(text, shift, direction):
    final_str = ''
    if shift >= len(alphabet):
        shift = shift % len(alphabet)
    if direction.lower() == 'decode':
        shift *= -1

    for i in text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if i.isalpha() == True:
            pos = alphabet.index(i)
            indx = pos + shift
            if direction.lower() == 'encode' and indx >= len(alphabet):
                indx = indx - len(alphabet)
            final_str += alphabet[indx]
        else:
            final_str += i
    print(f"The {direction} text is {final_str}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
ans = 'yes'
while ans.lower() == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ans = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
