# # creation logic behind the scenes is hidden.   
# # To instantiate a class means to create an object from it. is meant to be a blueprint for other classes.
# Single Responsibility principle should be followed

# from abc import ABC, abstractmethod
# @abstractmethod
# class Shape(ABC):
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("Drawing circle")

# class Square(Shape):
#     def draw(self):
#         print("Drawing square")

# # Factory class
# class ShapeFactory:
#     def getShape(self,shape_type):
#         if shape_type.lower()=="circle":
#             return Circle()
#         elif shape_type.lower()=="square":
#             return Square()
#         return None
    
# # Driver code
# if __name__ == "__main__":
#     shape_factory=ShapeFactory()
#     shape1=shape_factory.getShape("CIRCLE")
#     if shape1:shape1.draw()
#     shape2 = shape_factory.getShape("SQUARE")
#     if shape2: shape2.draw()

# Example logistic service

from abc import ABC, abstractmethod
class Logistics(ABC):
    @abstractmethod 
    def send(self):
        pass

class Road(Logistics):
    def send(self):
        print("sending by road") 

class Air(Logistics):
    def send(self): 
        print("sending by air") 

class LogisticsFactory:
    @staticmethod
    def get_logistics(self,mode):
        if mode.lower()=='air':
            return Air()
        elif mode.lower() == "road":
            return Road()
        else:
            raise ValueError(f"Unknown logistics mode: {mode}")
class LogisticsService:
    def send(self, mode):
        # Using the Logistics Factory to get the desired object based on the mode
        logistics = LogisticsFactory.get_logistics(self,mode)
        logistics.send()

if __name__ == "__main__":
    service = LogisticsService()
    service.send("Air")
    service.send("Road")