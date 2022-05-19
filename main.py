
#importing local and global files 
import os, sys,difflib,threading
import gh
file_path = 'pyfiglet-0.8.post1/'
sys.path.append(os.path.dirname(file_path))
file_path2 = 'lolpython-2.2.0/'
sys.path.append(os.path.dirname(file_path2))
file_path3='cowsay-4.0/'
sys.path.append(os.path.dirname(file_path3))

#importing timer
import timer
import time

#import difflib 
from difflib import Differ

#importing lol pythonand figlet
from lolpython import lol_py 
import pyfiglet
import cowsay

#printing banner
result = pyfiglet.figlet_format("                           QWERTY DIO",width=2000)
lol_py(result)
#coloured text /rules
GREEN = '\033[32m'
ENDC = '\033[m'
cowsay.beavis(GREEN+"<^>Do not close the terminal \n <^> Always save the file while using \n <^>After the finishing just save and close the text editor"+ENDC)



#getting names
ch=input("Enter your name: ")
re=ch.replace(" ","_")#reoplacing spaces

#specifying path
pathT=re+".txt"

print(pathT)
os.system("touch "+pathT)
result2 = pyfiglet.figlet_format("           welcome  "+ch)
lol_py(result2)

time.sleep(2)

def count():
     
    timer.countdown(20)
    os.system("pkill xed")
    check()
    check2()
     
    
    


x = threading.Thread(target=count)  



def check():
    
    d = Differ()
    path1="main.txt"  
    e=open(path1).readlines()
    e="".join(e)
    ee=e.replace(" ","")
    y=open(pathT).readlines()
    y="".join(y)
    yy=y.replace(" ","")
    difference = list(d.compare(ee, yy))
    count1=-1
    for x in difference:
        t=x.split(" ")
        if t[0]=="+" or t[0]=="-":
            count1+=1
    
    fi=open("log.txt",'a')
    fi.write("\n")
    fi.write(pathT+" /count/"+str(count1)+"\n ")
    fi.flush()
    fi.close()
    
    print(count1)
    
def check2():
    
    path1="main.txt"
    path2=pathT
    main_file=open(path1).readlines()
    competition_entry=open(path2).readlines()
    diff=difflib.HtmlDiff().make_file(main_file,competition_entry,path1,path2)
    diff_file=open(re+'.html','w')
    diff_file.write(diff)
    diff_file.close() 
   
     

def openfile():
    
    x.start()
    os.system("xed "+pathT)
   
    while gh.pros("xed"):
    	continue
    timer.ty=False


openfile()


#Code By christo vincent























    












