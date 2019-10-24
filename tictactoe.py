#Simple tic tac toe program
#Using only basic selection and looping statements
#Using some predefined functions from class str
#Program is based on three functions..
a=['1','2','3','4','5','6','7','8','9']
x=1
print("WELCOME to tic tac toe")
#Function to take input from user.Takes input position
	#input value is restricted from 1 to 9
		#The input value cannot be repeated
	#ON alternate trials the values of the list for the given input position is set as "X" and"O"
	#if the input position does not satisfy any of the conditions a "INVALID choice" message is shown
#start of the takeValue() function block
def takeValue():
	num=int(input("Select a position: "))
	if((num<10) and (num>0)):
		if((a[num-1]=='X') or (a[num-1]=='O')):
			print("Position is already taken,try again")
			takeValue()
		elif(x%2==0):
			a[num-1]='O'
		else:
			a[num-1]='X'
	else:
		print("INVALID choice ,try again")
		takeValue()
	show()
	return
#end of the takeValue() function block
#printing function definition
	#the function uses basic print statement to show the list in the form of a tic tac toe layout
#start of the  start() function block
def show( ):
	print("\n")
	print(" ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ \n| %s | %s | %s |\n ___ ___ ___ "%(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))
	print("\n")
	return
#end of the start() function block
#condition check function definition
	#The function consists of multiple if elif statements to check the required conditionn for winning and draw
	#the function returns data of tyoe boolean 
	#boolean false is generaated for all the win and draw condition
	#boolean true is  generated once all the conditions fail
#start of the check() functionn block
count=0
def check( count):
	i=0
	flag=True
	#a while loop used to count the number of inputs taken
	while(i<8):
		if(a[i].isalpha()):
			count=count+1
		i=i+1	
	if(count>4):
		if((a[0]==a[1]==a[2]=='X') or (a[0]==a[1]==a[2]=='O')):
			print("Player %s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[3]==a[4]==a[5]=='X') or (a[3]==a[4]==a[5]=='O')):
			print("Player %s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[6]==a[7]==a[8]=='X') or (a[6]==a[7]==a[8]=='O')):
			print("Player%s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[0]==a[3]==a[6]=='X') or (a[0]==a[3]==a[6]=='O')):
			print("Player%s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[1]==a[4]==a[7]=='X') or (a[1]==a[4]==a[7]=='O')):
			print("Player%s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[2]==a[5]==a[8]=='X') or (a[2]==a[5]==a[8]=='O')):
			print("Player %s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[0]==a[4]==a[8]=='X') or (a[0]==a[4]==a[8]=='O')):
			print("Player %s wins!!"%(x))
			ex=input("press any key to quit: ")
			if(ex.isprintable()):
					flag=False
		elif((a[2]==a[4]==a[6]=='X') or (a[2]==a[4]==a[6]=='O')):
			print("Player%s wins!!"%(x))
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
n=0
game=True
show()
#a while loop that  iterates 9 times 
	#the loop calls the functions defined and is terminated in between if the check() function returns a false 
while(n<9 and game):
	takeValue()
	game=check(count)
	if(x==2):
		x=x-1
	else:
		x=x+1
	n=n+1
	
#end of program
