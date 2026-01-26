class EagerSingleton:
    __instance=None
    def __init__(self):
        if EagerSingleton.__instance is not None:
            raise Exception("This is a singleton!")
        EagerSingleton.__instance=self

    @staticmethod
    def getInstance():
        return EagerSingleton.__instance

EagerSingleton._EagerSingleton__instance = EagerSingleton()


# This is the class-level variable that stores the singleton object
# Internally, Python rewrites it as:
# EagerSingleton._EagerSingleton__instance

# if the varaible is changed to private , and then the variable is called , the vairable name is changed to __Test__x
# class Test:
#     # x=10
#     __x=10
# print(dir(Test))
# print(Test.__x)

# singleton instance is created only when its needed -i.e only when getInstance is called.
class LazySingleton():
    __instance=None
    def __init__(self):
        if LazySingleton.__instance is not None:
            raise Exception("This class is singleton")
        LazySingleton.__instance=self
        
    @staticmethod
    def getInstance():
        if LazySingleton.__instance is not None:
            LazySingleton() 
        return LazySingleton.__instance
obj = LazySingleton.getInstance()
obj2=LazySingleton.getInstance()

