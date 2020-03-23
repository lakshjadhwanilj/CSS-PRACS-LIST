import numpy as np
choice = 1
while choice != 0:
	print("\n**TRANSPOSITION TECHNIQUE - RAIL FENCE**")
	choice = int(input("\nChoose One Method:\n1. Keyless\n2. Keyed\n3. Quit\nEnter Your Choice: "))
	if choice == 1:
		#Keyless Rail Fence
		ch = 1
		while ch != 0:
			ch = input("Enter e for ENCRYPTION & d for DECRYPTION OR b to GO BACK: ")
			if ch == 'e':		
				print("\n**PERFORMING ENCRYPTION**")
				inp = input("Enter Plain Text: ")
				plainText = np.array(list(inp))				
				lenPT = len(plainText)
				temp = lenPT
				if (lenPT % 2 == 0):
					pass
				else:
					plainText = np.append(plainText,'x')
					temp = lenPT + 1
				row1 = []
				row2 = []
				for i in range(0,temp,2):
					row1.append(plainText[i])
				for j in range(1,temp,2):
					row2.append(plainText[j])
				cipher = row1 + row2
				print("Cipher Text: " , end="")	
				print(''.join(cipher))
				print()
			elif ch == 'd':
				print("\n**PERFORMING DECRYPTION**")
				inp = input("Enter Cipher Text: ")
				cipher = np.array(list(inp))
				lenPT = len(cipher)
				quo = int(lenPT / 2)
				temp = 0
				lstEven = []
				for i in range(0,lenPT):
					lstEven.append(cipher[i])
					temp = temp + 1					
					lstEven.append(cipher[i+quo])
					temp = temp + 1
					if temp == lenPT:
						break
				print("Plain Text: ", end="")
				print(''.join(lstEven))
				print()
			elif ch == 'b':
				break
			else:
				print("Enter A Valid Choice!")
	elif choice == 2:
		#Keyed Rail Fence
		ch = 1
		while ch != 0:
			ch = input("Enter e for ENCRYPTION & d for DECRYPTION OR b to GO BACK: ")
			if ch == 'e':		
				print("\n**PERFORMING ENCRYPTION**")
				inp = input("Enter Plain Text: ")
				plainText = np.array(list(inp))
				lenPT = len(plainText)
				key = int(input("Enter Key: "))
				if (lenPT % key == 0):
					if lenPT != key:
						noExtra = (key * key) - lenPT
						extra = np.array('')
						for i in range(0,noExtra):
							extra = np.append(extra,'x')
						extra = np.delete(extra,0)
						plainText = np.append(plainText,extra)
				else:
					noExtra = (key * key) - lenPT
					extra = np.array('')
					for i in range(0,noExtra):
						extra = np.append(extra,'x')
					extra = np.delete(extra,0)
					plainText = np.append(plainText,extra)
				cipher = plainText.reshape(key,key)
				cipherList = []
				for j in range(key):
					for i in range(key):
						cipherList.append(cipher[i][j])
				print("Cipher Text is: ", end="")
				print(''.join(cipherList))
				print()
			elif ch == 'd':
				print("\n**PERFORMING DECRYPTION**")
				inp = input("Enter Cipher Text: ")
				cipher = np.array(list(inp))
				lenPT = len(cipher)
				key = int(input("Enter Key: "))
				quo = int(lenPT / key)
				temp = 0
				lstEven = []
				for i in range(0,lenPT):
					times = 0
					while times < key:
						lstEven.append(cipher[i + (quo * times)])
						times = times + 1
						temp = temp + 1					
					if temp == lenPT:
						break
				print("Plain Text: ", end="")
				print(''.join(lstEven))
				print()
			elif ch == 'b':
				break
			else:
				print("Enter A Valid Choice!")
	elif choice == 3:
		print("\n**THANK YOU**")
		choice = 0
	else:
		print("Enter A Valid Choice!")