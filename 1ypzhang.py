def encode(password):
    encoded = ''
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded

def decode(encoded_password):
    decoded = ''
    for char in encoded_password:
        decoded += str((int(char) - 3) % 10)
    return decoded

def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        option = input("Please enter an option: ")
        
        if option == '1':
            pw = input("Please enter your password to encode: ")
            encoded_pw = encode(pw)
            print("Your password has been encoded and stored!")
            print(f"The encoded password is {encoded_pw}.")
    
        elif option == '2':
            encoded_pw = input("Please enter your encoded password to 
decode: ")
            original_pw = decode(encoded_pw)
            print(f"The encoded password is {encoded_pw} and the original 
password is {original_pw}.")
        
        elif option == '3':
            print("bye!")
            break
        else:
            print("error.")

if __name__ == "__main__":
    main

