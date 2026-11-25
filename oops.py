#intialising a class
class employee:
    #special function /magical function/constructor
    def __init__(self):
        print("you are learning ML OPs concepts")
        self.id=1
        self.salary=5000000
        self.designation="SDE"
        print("attributes get intialise")

    def travel(self,destination):
        print("this travel method get called manually")
        print(f"Employee is now travelling to {self.designation}")

#create an obeject of a class
sam = employee()
sam.travel("kerla")   
print(type(sam))   