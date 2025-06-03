class Car: #class_name
    def __init__(self,car_name,car_type): #constructor
        self.car_name = car_name
        self.car_type = car_type

    def mhaw(self,model): #instance method
        self.model = model #instance variable
        return self.car_name,self.car_type,self.model

    def mhaw_refine(self,new_model):
        self.new_model = new_model
        scorpio_retuning = self.new_model + self.model + '100hp'
        return scorpio_retuning,self.new_model,self.xuv900

obj1 = Car('Mahindra','SUV')
obj1.xuv900 ='mhaw new 2025' #instance variable,outside class,using object reference
print(obj1.mhaw('Scorpio'))
print(obj1.mhaw_refine('Range Rover'))
del obj1.car_type
print(obj1.__dict__)
#print(len(obj1.__dict__))

# obj2 = Car('Mahindra','Audi')
# print(obj2.mhaw('BMW'))