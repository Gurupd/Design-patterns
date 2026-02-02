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
        if LazySingleton.__instance is None:
            LazySingleton() 
        return LazySingleton.__instance


# Several ways to make Singleton thread safe
# we can prevent multiple threads from creating multiple instances
# threading.Lock() is a mutex (mutual exclusion lock).
# It is a key that allows only one thread at a time to enter a critical section of code.

# 1. Synchronised method 
# import threading
# class Singleton:
#     __instance =None
#     __lock=threading.Lock()

#     def __init__(self):
#         if Singleton.__instance is not None:
#             raise Exception("This class is singleton")
#         Singleton.__instance=self

#     @staticmethod
#     def getInstance():
#         with Singleton.__lock:
#             if Singleton.__instance is None:
#                 Singleton()
#             return Singleton.__instance


#Double checking method
# import threading 
# class Singleton:
#     __instance=None
#     _lock=threading.Lock()
#     def __init__(self):
#         if Singleton.__instance is not None:
#             raise Exception("this is singleton") 
#         Singleton.__instance=self
#     @staticmethod
#     def getInstance():
#         if Singleton.__instance is None:
#             with Singleton._lock:
#                 if Singleton.__instance is None:
#                     Singleton()
#         return Singleton.__instance


#Bill Pugh Singleton (Best Practice for Lazy Loading)
class Singleton:
    def __init__(self):
        if hasattr(Singleton,'_created'):
            raise Exception("This class is singleton")

def getInstance():
    if not hasattr(getInstance, "_instance"):
        getInstance._instance = Singleton()
    return getInstance._instance


print(getInstance())


