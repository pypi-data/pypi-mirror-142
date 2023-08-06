# MoreUpdate
## Some Added stuff for python 3


MoreUpdate ae just add more and will more stuff for faster coding.

- Faster coding
- More shorter code

## Features

- Explicit Type Function
- Constant Value
- Explicit Type Variable


## Installation



Install the dependencies and devDependencies

```sh
pip install MoreUpdate
```






## Tutalrial 

### 1.Explicit Type Function

```python
from explict import Function,TYPE


def foo(bar): #wanted bar is a string...
	print(bar)

# Used : Function(Your_def,..Some type with TYPE.<TYPE>.get())
foo = Function(foo,TYPE.STRING.get())


#.call(argument) to call that function
foo.call("Hello")

foo.call(123) #Error goes here!


```

```bash
Hello
TypeError: type of 123 <class 'int'> is not <class 'str'>
[Finished in 233ms]
```
### 2.Constant
```python
from explict import Constant

a = Constant("123")

a.get() # return "123" no set
```

### 3.Explicit Type variable
```python
from explict import Var

a = Var("123")

a.get() # return "123"

a.set("1234") # Fine
print(a.get()) # 1234

a.set(123) #Uh oh...
print(a.get())



```

```bash
1234
TypeError: 123 Have type of <class 'int'> not <class 'str'>
[Finished in 95ms]
```
### 4.All TYPE built-in 
```python
from explict import TYPE,Constant,Function

# TYPE.STRING.get() # String type "Hello"
# TYPE.INT.get() # Integer type 123
# TYPE.FLOAT.get() # Float type 1.23
# TYPE.OBJECT.get() # Dict or Object type {"a":1}
# TYPE.BYTE.get() # Byte like b'123'
# TYPE.ARRAY.get() # That array type []

#Create Your own TYPE
class MyType:
	def __init__(self,v):
		self.v = v

	def say(self):
		print(f"Hi {self.v}")

TYPE.MYTYPENAME = Constant(MyType("Some example Value"))

#used your type

def sayhi(mytype):
	mytype.say()

sayhi = Function(sayhi,TYPE.MYTYPENAME.get()) # <class '__main__.MyType'>


A = MyType("123")
sayhi.call(A)
sayhi.call("123")
```

```bash
Hi 123
TypeError: type of 123 <class 'str'> is not <class '__main__.MyType'>
[Finished in 194ms]
```


### 5.FS in Python

```python

from explict import fs

def CallBack(err):
	if(not err):
		print("Done")

fs.writeFile("filename.txt","Some content",CallBack)
# fs.appendFile Will append text like before

```

```bash
Done
[Finished in 294ms]
```

```python

from explict import fs

def printl(line):
	print(line)


fs.linebyline("filename.txt",printl)

```

```bash
Hello
This
is
the
content
of
the
file
[Finished in 294ms]
```


### 6.Secure Function (beta)

```python
from explict import Secure


# Some getting info from client

email = "who@gmail.com"
plaintext = "12345678"
# Secure.hash(Text,Digest)
hashtext = Secure.hash(plaintext) # 125 Digits default of 25 digest 250000000 case test no collision...

print(email,hashtext)

# Do something to store the hash

# Compare 

guess = "12345678"

if(hashtext == Secure.hash(guess)):
	print("Right!")


```

```bash
who@gmail.com 4ba87acc46d6b6dc56b706d9a6a6b9e706b9b6868689594979b6070c66a61696b9e9a699e3931393639333934633539623961393939363732396363356334633
Right!
[Finished in 513ms]
```
## More Comming Soon...
#### Video comming soon..