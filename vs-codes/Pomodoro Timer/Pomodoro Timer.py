import time
import os

def convert(t):
    return t * 60

def countdown(t, label):
      #60 sec = 1 min
	while t:
		#We want mins in sec so that we can display Eg: 1 min 30 sec
		min, sec = divmod(t, 60) #divmod returns a tuple
		
		#This is the same as: t//60 (time divided by 60) to get minutes
		#Then t%60 to get seconds.

		print(f"{label}: {min:02d}:{sec:02d}", end="\r") 
		#print out how much time we have
		time.sleep(1)
		t -= 1

def pomodoro(work, rest):   #Convert our min to second
	w = convert(work)
	r = convert(rest)
	countdown(w, "Work")
	os.system("clear||cls")
	countdown(r, "Rest")
	os.system("clear||cls")


work = int(input("Enter work time (min): ")) 
rest = int(input("Enter rest time (min): "))

pomodoro(work, rest)




