# import the time module
import time
ty=True
mins=0
secs=0
# define the countdown func.
def countdown(t):
	
	while (ty and t):
		    mins, secs = divmod(t, 60)
		    timer = '{:02d}:{:02d}'.format(mins, secs)
		    print(timer, end="\r")
		    time.sleep(1)
		    t -= 1
	typ=t	    
	min, sec = divmod(typ, 60)
	hour, min = divmod(min, 60)
	f=open("log.txt","a")
	f.write("\n \n")
	f.write(" timing :")
	f.write(str(hour)+":"+str(min)+":"+str(sec)+"\n")
	f.flush()
	f.close()

    
  
