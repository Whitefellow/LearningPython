Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> helloFile = open ('C:\\Users\\Doug\\SkyDrive\\Documents\\hello.txt')
>>> helloFile
<_io.TextIOWrapper name='C:\\Users\\Doug\\SkyDrive\\Documents\\hello.txt' mode='r' encoding='cp1252'>
>>> helloFile = open('C:\\Users\\Doug\\SkyDrive\\Documents\\hello.txt')
>>> helloFile
<_io.TextIOWrapper name='C:\\Users\\Doug\\SkyDrive\\Documents\\hello.txt' mode='r' encoding='cp1252'>
>>> helloContent = helloFile.read()
>>> helloContent
'Hello world!'
>>> sonnetFile = open('sonnet29.txt')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sonnetFile = open('sonnet29.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'sonnet29.txt'
>>> sonnetFile = open('C:\\Users\\Doug\Skydrive\\Documents\\sonnet29.txt')
>>> sonnetfile
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sonnetfile
NameError: name 'sonnetfile' is not defined
>>> sonnetFile
<_io.TextIOWrapper name='C:\\Users\\Doug\\Skydrive\\Documents\\sonnet29.txt' mode='r' encoding='cp1252'>
>>> sonnetFile.readlines()
["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('Hello world!')
12
>>> baconFile.write('Hellow world!\n')
14
>>> BaconFile.Write('Hello world!\n')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    BaconFile.Write('Hello world!\n')
NameError: name 'BaconFile' is not defined
>>> baconFile.Write('Hello world!\n')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    baconFile.Write('Hello world!\n')
AttributeError: '_io.TextIOWrapper' object has no attribute 'Write'
>>> baconFile.write('Hello world!\n')
13
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello world!Hellow world!
Hello world!
Bacon is not a vegetable.
>>> baconFile.del('Hellow world!')
SyntaxError: invalid syntax
>>> baconFile.open
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    baconFile.open
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> baconFile.open('bacon.txt')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    baconFile.open('bacon.txt')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> baconFile
<_io.TextIOWrapper name='bacon.txt' mode='r' encoding='cp1252'>
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> ShelFile['cats'] = cats
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ShelFile['cats'] = cats
NameError: name 'ShelFile' is not defined
>>> ShelfFile['cats'] = cats
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ShelfFile['cats'] = cats
NameError: name 'ShelfFile' is not defined
>>> ShelfFile['cats'] = cats
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    ShelfFile['cats'] = cats
NameError: name 'ShelfFile' is not defined
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
>>> shelve.open()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    shelve.open()
TypeError: open() missing 1 required positional argument: 'filename'
>>> import shelve
>>> shelve.open()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    shelve.open()
TypeError: open() missing 1 required positional argument: 'filename'
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('mycats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> myCats.cats
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    myCats.cats
NameError: name 'myCats' is not defined
>>> fileObj
<_io.TextIOWrapper name='mycats.py' mode='w' encoding='cp1252'>
>>> fileObj.open
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    fileObj.open
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> fileObj
<_io.TextIOWrapper name='mycats.py' mode='w' encoding='cp1252'>
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close
<built-in method close of _io.TextIOWrapper object at 0x045D1C30>
>>> fileObj.close()
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> fileObj = open(myCats.py', 'w')
	       
SyntaxError: invalid syntax
>>> fileObj= open('myCats.py', 'w')
>>> import myCats
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    import myCats
ModuleNotFoundError: No module named 'myCats'
>>> 
 RESTART: C:/Users/Doug/AppData/Local/Programs/Python/Python36-32/Anewfolder/randomQuizGenerator.py 
Traceback (most recent call last):
  File "C:/Users/Doug/AppData/Local/Programs/Python/Python36-32/Anewfolder/randomQuizGenerator.py", line 49, in <module>
    random.shuffle[answerOptions]
TypeError: 'method' object is not subscriptable
>>> 
 RESTART: C:/Users/Doug/AppData/Local/Programs/Python/Python36-32/Anewfolder/randomQuizGenerator.py 
Traceback (most recent call last):
  File "C:/Users/Doug/AppData/Local/Programs/Python/Python36-32/Anewfolder/randomQuizGenerator.py", line 49, in <module>
    random.shuffle[answerOptions]
TypeError: 'method' object is not subscriptable
>>> 
