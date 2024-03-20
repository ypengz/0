def encode(password):
    encoded = ''
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded

def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Quit")
        
        option = input("Please enter an option: ")
        
        if option == '1':
            pw = input("Please enter your password to encode: ")
            encoded_pw = encode(pw)
            print("Your password has been encoded and stored!")
            print(f"The encoded password is {encoded_pw}.")
        
        elif option == '2':
            print("bye!")
            break
        else:
            print("error.")

if __name__ == "__main__":
    main()
