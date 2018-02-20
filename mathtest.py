
print("Hello, World!")
# different point
#3.1 number
print(2/3)
print(2//3)
print(2%3)

#3.2 string
print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

letters = ['a', 'b', 'c', 'd']
print(len(letters))

queue = deque(["Eric", "John", "Michael"])
print(queue.popleft())
print(queue)

print({x: x**2 for x in (2, 4, 6)})

print({x: x**2 for x in (2, 4, 6)})

x = 3

while x < 10 :
    x = x + 1
    Behold("test").when(x>5).show('x','x')
