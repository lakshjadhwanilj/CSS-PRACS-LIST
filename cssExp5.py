a, b = input("Enter 2 Prime Numbers: ").split()
a = int(a)
b = int(b)

n = a * b
print("Value of n: ", n)
phiN = (a - 1) * (b - 1)
print("Value of Phi(n): ", phiN)
e = int(input("Enter A Public Key: "))

def gcd(e, phiN):
	r1 = e
	r2 = phiN
	q = 0
	r = r1
	while(r2 > 0):
	    q = int(r1 / r2)
	    r = r1 - (q * r2)
	    r1 = r2
	    r2 = r
	if r1 == 1:
		return True
	else:
		return False

def inversed(e, phiN):
	r1 = phiN
	r2 = e
	t1 = 0
	t2 = 1
	t = 0
	q = 0
	r = r1

	while(r2 > 0):
	    q = int(r1 / r2)
	    r = r1 - (q * r2)
	    r1 = r2
	    r2 = r
	    t = t1 - (q * t2)
	    t1 = t2
	    t2 = t
	if (r1 == 1):		
	    if (t1 < 0):
	    	return 26 + t1
	    else:
	    	return t1

if gcd(e, phiN):
	if 1 < e and e < phiN:
		d = inversed(e, phiN)
print("Publc Key: ({}, {})".format(e,n))
print("Private Key: ({}, {})".format(d,n))	

choice = 'e'
while choice != 'q':
	choice = input("\nEnter e for ENCRYPTION & d for DECRYPTION OR q to QUIT: ")
	if choice == 'e':
		p = int(input("\nEnter Plain Text: "))
		print("** COMPUTING CIPHER TEXT **")
		c = pow(p, e, n)
		print("Cipher Text: ", c)		
	elif choice == 'd':
		c = int(input("\nEnter Cipher Text: "))
		print("** Computing Plain Text **")
		p = pow(c, d, n)
		print("Plain Text: ", p)
	elif choice == 'q':
		print("\n** THANK YOU **")
		break
	else:
		print("Enter A Valid Choice!")


