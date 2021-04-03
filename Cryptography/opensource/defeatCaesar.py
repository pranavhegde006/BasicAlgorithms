print("This is a simple brute force technique to defeat Caesar cipher!")
print("Try it just by entering the cipher text you wanna decrypt!")

cipherText = input("Enter your cipher text:     ")
key = int(input("Enter your key:    "))

def decryptCaesar(cipherText, key):
    messageStr = ''
    cipherText = cipherText.lower()
    for i in range(len(cipherText)):
        temp = ord(cipherText[i]) - ord('a')
        messageStr += chr((temp - key)% 26 + ord('a'))
    return messageStr

def defeatCaesarBrute(cipherText):
    for i in range(26):
        message = decryptCaesar(cipherText, i)
        print(message)

defeatCaesarBrute(cipherText)

print("\n\n This code is courtesy Pranav R. Hegde. https://github.com/pranavhegde006")
