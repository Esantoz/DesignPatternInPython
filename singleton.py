
class Singleton:
    __instance = None
    
    def __init__(self):
        if Singleton.__instance != None:
            print("Class already exists!")
        else:
            Singleton.__instance = self
    
    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance
    
    
    
a = Singleton.getInstance()
print(a)
b = Singleton.getInstance()
print(b)
c = Singleton.getInstance()
print(c)