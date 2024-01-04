from pult_program import *

print("""----Pult Menu----
1. TV Power ON/Off
2. TV Info
3. Channels Amount
4. Add Channel
5. Random Channel
6. Change Volume

`-1` -> EXIT,bro!""")

pult = Pult()

while True:
 	choice = input("Choose: ")
 	if choice == '-1':
 		print("GoodBye!")
 	if choice == '1':
 		pult.position()
 	elif choice == '2':
 		print(pult)
 	elif choice == '3':
 		print("Channels Amount: ",len(pult))
 	elif choice == '4':
 		pult.add_newChannel()
 	elif choice == '5':
 		pult.random_channel()
 	elif choice == '6':
 		pult.volume_upDown()
 	else:
 		print("Enter Correctly 1-7")

