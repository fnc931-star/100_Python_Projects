# Here i write the main logic of secret_shift -> ceaser cipher


def encryption(text,shift):
    encoded_text = ""
    print(f"Here's the encoded result: {encoded_text}")


def decryption(text,shift):
    decoded_text = ""
    print(f"Here's the encoded result: {decoded_text}")


flag = True

while flag:

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:'\n   ").lower()
    message = input("Type your message:'\n   ").lower()
    shift_number = int(input("Type the shift number:'\n   "))


    if choice == 'encode':
        encryption(message,shift_number)

    elif choice == 'decode':
        decryption(message,shift_number)

    else:
        print("Type wrong, Please enter correct input.")

    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.'\n   ")

    if run_again == 'yes':
        continue
    else:
        flag = False


print("GoodBye")