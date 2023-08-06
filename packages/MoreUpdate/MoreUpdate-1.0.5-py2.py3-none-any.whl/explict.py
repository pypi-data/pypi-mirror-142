import time
import traceback
from tracemalloc import stop
from dill.source import getsource





class Constant:
	def __init__(self,constantV):
		self.__value = constantV

	def get(self):
		return self.__value

class Var:
	def __init__(self,value):
		self.__value = value

	def get(self):
		return self.__value

	def type(self):
		return type(self.__value)

	def set(self,value):
		if(type(self.__value) != type(value)):
			raise TypeError(f"{value} Have type of {type(value)} not {type(self.__value)}")
		else:
			self.__value = value



class TYPE:
	STRING = Constant("")
	INT = Constant(0)
	FLOAT = Constant(0.0)
	OBJECT = Constant({})
	BYTE = Constant("123".encode("utf-8"))
	ARRAY = Constant([])
	




class Function:
	def __init__(self,func,*args):
		self.func = func
		self.args = []
		self.exp = []
		for argv in args:
			#print(argv)
			self.args.append(argv)
			self.exp.append(type(argv))

	def call(self,*args):
		if len(args) != len(self.args):
			raise Exception(f"Argument doesn't match our record : {len(args)} and {len(self.args)}")
		Pass = True
		for a in range(len(args)):
			if type(args[a]) != self.exp[a]:
				raise TypeError(f"type of {args[a]} {type(args[a])} is not {self.exp[a]}")
		self.func(*args)
			


class fs:
	def writeFile(name,content,callback):
		try:
			with open(name,"w") as f:
				f.write(content)
				try:
					callback()
				except:
					#no callback is ok!
					pass
		except Exception as e:
			callback(e)
	def appendFile(name,content,callback):
		try:
			with open(name,"a") as f:
				f.write(content)
				try:
					callback()
				except:
					#no callback is ok!
					pass
		except Exception as e:
			callback(e)
	def linebyline(name,callbackaline):
		try:
			with open(name,"r") as f:
				for line in f:
					callbackaline(line)
		except Exception as e:
			print("WARRNING")
			print(traceback.format_exc())
			print(e)
			

import string	
import random # define the random module  
S = 16  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  


class Random:
	def __init__(self,seed):
		self.seed = seed
		self.lastO = seed
	
	def getO(self):
		self.lastO = (self.lastO + 97851512328937) * 48123098591283 % 10**10
		return self.lastO

import re
def hash(s):
    a = 1
    c = 0
    o = 0
    if (s) :
        a = 0
        for strs in s:
            o = ord(strs)
            a = (a<<6&268435455) + o + (o<<14)
            c = a & 266338304
            a = a^c>>21 if c != 0 else a
    return hex(a)[2:]
class Secure:
	def hash(msgs,digets=25,loop=2,debug=False):
		msg = [ord(str(m)) << 31 for m in msgs]
		sum = 152235
		randoms = Random(sum)



		for m in msg:

			sum += m
			rt = Random(m)
			for i in range(digets):
				sum += (10**4)*rt.getO()
			sum += (10**3)*randoms.getO()
		#print(sum)
		r = Random(int(sum))
		s = sum
		for i in range(250):
			s += (10**i)*r.getO()
		part1 = hex(s)[2:]
		s = sum*50259123
		r = Random(s)
		for j in range(loop):
			for i in range(250+10*(j+1)):
				s += (10**(i))*r.getO()
			part2 = hex(s)[2:]
			chars = ""
			for i in range(len(part1)-1):
				try:
					chars += hex(ord(part1[i]) + ord(part2[i]))[2:]
				except:
					chars += hex(ord(part1[i]))[2:]
			part1 = chars
		part1 = part1[2:]
		if(r.getO() < ((10**10)/2)):
			part1 = part1[::-1]
		part1 = part1[395:]
		part1 = hash(msgs) + part1
		#print(part1)
		#part1
		if(not debug):
			return part1[:128]
		else:
			return [part1,msg,sum]


#passwd = Secure.hash("Hello")


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))






#Decorator 
import multiprocessing
from threading import Thread
def initProcess():
	print("[INFO] Starting")
	print(f"[INFO] Core Allowed : {multiprocessing.cpu_count()}")
	print("[INFO] Testing..")
	try:
		def work():
			return "Hello"
		p = Thread(target=work)
		p.start()
		p.join()
		print("[INFO] Started Fine...")
	except:
		print("[CRITICAL] SomeThings Wrong in the runner")

apply_tuple = lambda f: lambda args: f(*args)

def parallel(func):
	def wrapper(*argv):
		#print(argv,func)
		thread = Thread(target=func,args=argv)
		thread.start()
	return wrapper

queue = []

def Queuing(func):
	def wrapper(*argv):
		#print(argv,func)
		thread = Thread(target=func,args=argv)
		queue.append(thread)
	return wrapper

class Queue:
	def start():
		while len(queue) != 1:
			queue[0].start()
			del queue[0]
		queue[0].start()
		queue[0].join()


class Timer:
	def __init__(self):
		start = 0
		stop = 0

	def start(self):
		self.start = time.time()

	def stop(self):
		self.stop = time.time()
		return (self.stop-self.start)

##########


# for i in range(1,25):
# 	start = time.perf_counter()
# 	a = Secure.hash("HelloWorld",i,debug=True)
# 	print(a[1:])
# 	stop = time.perf_counter()
# 	print(f"Took : {stop-start}ms for {i} digets")
# 	print("[INFO] Perform test in 200 case...")
# 	counter = 0
# 	for i in range(200):
# 		a = id_generator(16)
# 		b = id_generator(16)
# 		ah = Secure.hash(a,i)
# 		bh = Secure.hash(b,i)
# 		if(ah == bh and a != b):
# 			counter += 1
# 	print(f"{counter} case are collison")
# import difflib
# def getD(a,b):
# 	letter = ""
# 	for i,s in enumerate(difflib.ndiff(a, b)):
# 		if s[0]==' ': continue
# 		elif s[0]=='-':
# 			letter += s[-1]
# 		elif s[0]=='+':
# 			letter += s[-1]
# 	return letter.lower()




# counter = 0
# case = []
# testcase = 2000
# digets = 25
# start = time.perf_counter()
# for i in range(testcase):
	
# 	a = id_generator(16)
# 	b = id_generator(16)
# 	timehash = time.perf_counter()
# 	ah = Secure.hash(a,digets)
# 	bh = Secure.hash(b,digets)
# 	timeendhash = time.perf_counter()
# 	#print(f"Took : {timeendhash - timehash}ms")
# 	fn = format(len(getD(ah,bh)), '06d')
# 	fn2 = format(i, '04d')
# 	if(ah == bh and a != b):
# 		stop = time.perf_counter()
# 		counter += 1
# 		print(fn2,ah[:16],bh[:16],fn,f"{timeendhash - timehash}ms","Collision...",(stop-start))
# 		case.append([a,b,ah[:16],bh[:16]])
# 		start = time.perf_counter()
# 	else:
# 		# if(i%100==0):
# 		# 	print(fn2,ah[:16],bh[:16],fn,f"{timeendhash - timehash}ms")
# 		print(fn2,ah[:16],bh[:16],fn,f"{timeendhash - timehash}ms")
# 		pass
# print(f"{counter}/{testcase} case are collison... ({counter/testcase})")
# for c in case:
# 	print(c)

#print(len(getD(Secure.hash("Quanvn"),Secure.hash("Quanvn1"))))
