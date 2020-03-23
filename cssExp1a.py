i = 1
alphabet = []
alpha = 'a'
for i in range(0,26):
    alphabet.append(alpha)
    alpha = chr(ord(alpha)+1)
while i != 0:
	choice = input("Enter e for ENCRYPTION & d for DECRYPTION OR q to QUIT: ")
	if choice == 'e':		
		print("\n**PERFORMING ENCRYPTION**")
		key = int(input("Enter Key: "))
		inp = input("Enter Plain Text: ")
		cipher = []
		for i in range(0,len(inp)):
		    temp = inp[i]
		    for j in range(0,26):
		        if(temp == alphabet[j]):
		            encrypt = (j + key)%26
		            cipher.append(alphabet[encrypt])
		print("Cipher Text is: ", end="")
		print(''.join(cipher))
		print()
		i = 1
	elif choice == 'd':
		print("\n**PERFORMING DECRYPTION**")
		key = int(input("Enter Key: "))
		inp = input("Enter Cipher Text: ")
		plainText = []
		for i in range(0,len(inp)):
		    temp = inp[i]
		    for j in range(0,26):
		        if(temp == alphabet[j]):
		            decrypt = (j - key)%26
		            plainText.append(alphabet[decrypt])
		print("Plain Text is: ", end="")
		print(''.join(plainText))
		print()
		i = 2
	elif choice == 'q':
		print("\n**THANK YOU**")
		i = 0
	else:
		print("Enter A Valid Choice!")