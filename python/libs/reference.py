def add(a,b):
    return a+b

def call_home(name):
    return f"{name}, phones home"

class Dog():

    def __init__(self, name):
        self.name = name

    def bark(self):
        print("bark ", self.name)