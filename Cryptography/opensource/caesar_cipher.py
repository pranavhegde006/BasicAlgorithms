
def encryptCaesar(plainText, key):
    cipherStr = ''
    plainText = plainText.lower()
    for i in range(len(plainText)):
        temp = ord(plainText[i]) - ord('a')
        cipherStr += chr((temp + key)% 26 + ord('a'))
    return cipherStr


def decryptCaesar(cipherText, key):
    messageStr = ''
    cipherText = cipherText.lower()
    for i in range(len(cipherText)):
        temp = ord(cipherText[i]) - ord('a')
        messageStr += chr((temp - key)% 26 + ord('a'))
    return messageStr

print("Welcome to CAESAR CIPHER!")
choice = int(input("\nEnter 1 if you want to encrypt. \nEnter 2 if you want to decrypt. \nEnter 0 to exit:    "))

while choice != 0:
    message = input("\nEnter your message:  ")
    key = int(input("Enter your secret key:   "))
    print()
    if choice == 1:
        output = encryptCaesar(message, key)
        print("Your secret message is:  ", output)
    elif choice == 2:
        output = decryptCaesar(message, key)
        print("Your message is:     ", output)
    
    print('-------------------------------------------------------------------')
    choice = int(input("\nEnter 1 if you want to encrypt. \nEnter 2 if you want to decrypt. \nEnter 0 to exit:    "))


print("\nThank you for choosing Caesar cipher by Pranav!")
print("Find more stuff at https://github.com/pranavhegde006 \n")
