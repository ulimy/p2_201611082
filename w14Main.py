class Dog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print ('my dog is',self.name,'mung mung')
    
class ShihTzuDog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print ('my dog is',self.name,'si si')
        
class Maltese(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print ('my dog is',self.name,'mal mal')

mydog=Dog('dog')
mydog.talk()

mydog=ShihTzuDog('ShihTzuDog')
mydog.talk()

mydog=Maltese('Maltese')
mydog.talk()