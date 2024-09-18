import threading

x = 1
y = 2
#print(f'x={id(x)}')
#print(f'y={id(y)}')

x = 3
#print(f'x={id(x)}')

# mutable vs immutable

def myFunction(val):
    print(f'BEFORE: val={id(val)}')
    val = val + 1
    print(f'AFTER:  val={id(val)}')

print(f'BEFORE: {x=}') 
myFunction(x)
print(f'AFTER:  {x=}')

def myFunctionString(val):
    print(f'BEFORE: val={id(val)}')
    val = "something else"
    print(f'AFTER:  val={id(val)}')

s = "string"
print(f'before pass it in: {id(s)}')
myFunctionString(s)
print(f'{s=}')

def myFuncList(l: list):
    print(f'BEFORE: l={id(l)}')
    l.append(324890)
    print(f'AFTER:  l={id(l)}')

myList = []
myList.append(40)
print(f'before myList addr={id(myList)}')
myList.append(41)
myFuncList(myList)
print(f'after myList addr={id(myList)}')

d = {}
d["1"] = 1
print(f'{d=}')

t = (1, 2, 3)

class MyClass():
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name
    
    def print_value(self):
        print(f'{self.age}')
        print(f'{self.name}')

m1 = MyClass(10, "Brandon")
m1.print_value()

class MyChildClass(MyClass):
    def __init__(self, age: int, name: str, children_names: list):
        super().__init__(age, name)
        self.children_names = children_names
        
    def __str__(self) -> str:
        return f"{self.age=}, {self.name=}, {self.children_names=}"
    
myChildren = ["A", "B", "C"]
m2 = MyChildClass(32, "Tom", myChildren)
print(f'm2={m2}')

t1 = threading.Thread(target=myFuncList, args=(myChildren,))
t1.start()