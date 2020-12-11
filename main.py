from datetime import date,time,datetime 
today=date.today()

print("TiME CHeCK!")

if __name__=='__main__':
	while True:
		ui = input("\n  -").lower()
		if "help" in ui:
			print('''ENTER
		check (to see current date and time.)
		exit  (to quit the program.)
		help (for usage)''')
		elif "date" in ui:
			print("Today's date is",today,"\n")
		elif "time" in ui:
			t=datetime.time(datetime.now())
			print("The time is",t)
		elif "exit" in ui:
				break
		else:
			print("Invalid Input",exit)
			break
