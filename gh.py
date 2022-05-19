import subprocess
import re
import os
def pros(poc):
	ps=subprocess.Popen("ps ax -o pid= -o args=",shell=True,stdout=subprocess.PIPE)
	ps_pid=ps.pid
	output=str(ps.stdout.read())
	ps.stdout.close()
	ps.wait()
	
	for line in output.split("\n"):
		res=re.findall("(\d+) (.*)",line)
		if res:
			pid=int(res[0][0])
			if poc in res[0][1] and pid != os.getpid() and pid != ps_pid:
				return True
	return False
