## light python syntax validator
Python has this builtin to the IDE already, this is for those that choose to be different...
# Usage
```python
python3 syntax.py --help

usage: syntax.py [-h] [-fd FD] [--string STRING] [--silent]

optional arguments:
  -h, --help       show this help message and exit
  -fd FD           File descriptor to compile
  --string STRING  Execute python code from string
  --silent         Don't raise exception when encountering an error
```

# Examples
Using --string
```python
$ python3 syntax.py --string "print('Hello, World')"
3.6.9 (default, Nov  7 2019, 10:44:02) [GCC 8.3.0] 

Hello, World
[+] Code executed in 0.00020972099991922732
```
Using -fd
```python
$ python3 syntax.py -fd main.py
3.6.9 (default, Nov  7 2019, 10:44:02) [GCC 8.3.0] 

unexpected EOF while parsing (<string>, line 1)
Workin' Hard 
```
Using --silent
```python
$ python3 syntax.py -fd main.py
3.6.9 (default, Nov  7 2019, 10:44:02) [GCC 8.3.0]

Workin' Hard
```
The **syntax.py** file with -fd supplied will even run code if the previous line was an error. If the next line/lines read from the line that error'd it will then throw an error.

## main.py
```python
print("Hello, World" #<-- this will error.
print("Workin' Hard") #<-- this will still run.
```