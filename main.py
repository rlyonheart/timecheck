from datetime import date,time,datetime 
today=date.today()

print("TiME CHeCK!")

if __name__=='__main__':
	while True:
		ui = input("\n  -").lower()
		if "help" in ui:
			print('''ENTER
		time (to see current time.)
                date (to see current date.)
		exit (to quit the program.)
		help (for usage.)''')
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
