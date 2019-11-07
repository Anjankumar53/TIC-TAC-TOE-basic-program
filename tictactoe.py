#Simple tic tac toe program
#Using only basic selection and looping statements
#Using some predefined functions from class str
#Program is based on three functions..
import random
a=['1','2','3','4','5','6','7','8','9']
#player number
count=0#number of turns taken
n=0#while loop iterative variable
game=True#another while loop variable relative to check() function

print("WELCOME to tic tac toe")
name1=input("PLAYER 1 ,ENTER YOUR NAME: ")
name2=input("PLAYER 2 ,ENTER YOUR NAME: ")
if(name1==name2):
	print("\nBOTH THE NAMES CANNOT BE THE SAME!")
	name2=input("\nPlayer 2,ENTER YOUR NAME: ")

symbol1=input("\n%s, SELECT a 'X' or 'O': "%(name1))
if(symbol1=='X' or symbol1=='x'):
	print("%s,YOU HAVE TO PLAY AS 'O'"%(name2))
	symbol2='O'
	symbol1='X'
elif(symbol1=='O' or symbol1=='o'):
	print("%s,YOU HAVE TO PLAY AS 'X'"%(name2))
	symbol2='X'
	symbol1='O'
else:
	print("\nTAKING SYMBOL BY DEFAULT:\n%s='X' \n%s='O'"%(name1,name2))
	symbol1='X'
	symbol2='O'

#block for selecting player randomly
print("\nRANDOMLY SELECTINNG THE FIRST PLAYER")
x=random.choice([1,2])
if(x==1):
	name=name1
elif(x==2):
	name=name2
print("PLAYER 1 IS %s"%(name))
print("\nLoading...")

#delay block
r=0
while(r<20000000):
	r=r+1
#approximate delay of 5secs as per my laptop conditions

import os
os.system('cls')
print("\nLETS GO!!")

#Function to take input from user.Takes input position
	#input value is restricted from 1 to 9
		#The input value cannot be repeated
	#ON alternate trials the values of the list for the given input position is set as "X" and"O"
	#if the input position does not satisfy any of the conditions a "INVALID choice" message is shown
#start of the takeValue() function block

def takeValue():
	num=int(input("%s select a position: "%(name)))
	if((num<10) and (num>0)):
		if((a[num-1]=='X') or (a[num-1]=='O')):
			print("Position is already taken,try again")
			takeValue()
		elif(x%2==1):
			a[num-1]=symbol1
		else:
			a[num-1]=symbol2
	else:
		print("INVALID choice ,try again")
		takeValue()
	return

#end of the takeValue() function block
#printing function definition
	#the function uses basic print statement to show the list in the form of a tic tac toe layout
#start of the  start() function block

def show( ):
	print("// TIC TAC TOE //")
	print("\n")
	print(" ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ "%(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))
	print("\n")
	return
show()

#end of the start() function block
#condition check function definition
	#The function consists of multiple if elif statements to check the required conditionn for winning and draw
	#the function returns data of tyoe boolean 
	#boolean false is generaated for all the win and draw condition
	#boolean true is  generated once all the conditions fail
#start of the check() functionn block

def check(count):
	i=0
	flag=True
	#a while loop used to count the number of inputs taken
	while(i<8):
		if(a[i].isalpha()):
			count=count+1
		i=i+1	
	if(count>4):
		if((a[0]==a[1]==a[2]=='X') or (a[0]==a[1]==a[2]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[3]==a[4]==a[5]=='X') or (a[3]==a[4]==a[5]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[6]==a[7]==a[8]=='X') or (a[6]==a[7]==a[8]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[0]==a[3]==a[6]=='X') or (a[0]==a[3]==a[6]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[1]==a[4]==a[7]=='X') or (a[1]==a[4]==a[7]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[2]==a[5]==a[8]=='X') or (a[2]==a[5]==a[8]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[0]==a[4]==a[8]=='X') or (a[0]==a[4]==a[8]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[2]==a[4]==a[6]=='X') or (a[2]==a[4]==a[6]=='O')):
			print("%s wins!!"%(name))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif(count>=8):
			print("Its a Draw!!")
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
				flag=False

	else:
		h=1
		flag=True
	return flag

#end of function check() block

#a while loop that  iterates 9 times 
	#the loop calls the functions defined and is terminated in between if the check() function returns a false 
while(n<9 and game):
	takeValue()
	import os
	os.system('cls')
	show()
	game=check(count)
	
	if(x==1):
		x=2
	elif(x==2):
		x=1
	
	if(x==1):
		name=name1
	elif(x==2):
		name=name2
	n=n+1

#end of program
