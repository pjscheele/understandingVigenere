#vigenere2.py

#define character-base
BASE=[
"A","B","C","D","E","F","G","H","I","J",
"K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z"," ","a","b","c",
"d","e","f","g","h","i","j","k","l","m",
"n","o","p","q","r","s","t","u","v","w",
"x","y","z","0","1","2","3","4","5","6",
"7","8","9",".",",","!","@","-","_","+",
"=","(",")","*","&","^","%","$","#","~",
"`","|","\\","{","}","[","]","\'","\"",":",
";","?","/",">","<"
]
ph1=0
ph2=0
ph3=0


def ENCRYPT(array0,array1):
	print("mod used: %s \n formula used: Plain+Key=Crypt" % len(BASE))
	message = []
	messagenr = []
	i=0
	for char in array0:
		ph1=BASE.index(char)
		if i > len(array1)-1:
			i=0
	
		ph2=BASE.index(array1[i])
		ph3=ph1+ph2
		if ph3 >= len(BASE)-1:
			ph3 = ph3-(len(BASE))
	
		messagenr.append(ph3)
		print("%3s + %3s = %3s , %3s = %3s" % (ph1, ph2, ph3, ph3, BASE[ph3]))
		i +=1

	for nr in messagenr:
		message.append(BASE[nr])

	return ''.join(message)

def DECRYPT(array0,array1):
	print("mod used: %s \n formula used: Plain+Key=Crypt" % len(BASE))
	message = []
	messagenr = []
	i=0
	for char in array0:
		ph1=BASE.index(char)
		if i > len(array1)-1:
			i=0
	
		ph2=BASE.index(array1[i])
		ph3=ph1-ph2
		if ph3 >= len(BASE)-1:
			ph3 = ph3-(len(BASE))
	
		messagenr.append(ph3)
		print("%s + %s = %s" % (ph1, ph2, ph3))
		i +=1

	for nr in messagenr:
		message.append(BASE[nr])

	return ''.join(message)
	
print("Welcome to crypt, what is it that you want to do?\n")
usr_input = ''
while usr_input not in ['1', '2']:
	usr_input = input('type 1 for encrypt, type 2 for decrypt:')

message = input('enter message:')
message.split()
key = input('enter key:')
key.split()

if usr_input == '1':
	print("encrypting message...\n")
	encrypted=ENCRYPT(message,key)
	print("your encrypted message = %s" % encrypted)
else:
	print("decrypting message...\n")
	decrypted =DECRYPT(message,key)
	print("your decrypted message = %s" % decrypted)
