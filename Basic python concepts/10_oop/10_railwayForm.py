class RailwayForm:
    formType = "Railway form"
    def printData(self):
        print("This is a ", self.formType)
        print(f"Name is {self.name}")
        print(f"Age of {self.name} is {self.age}")
        print(f"Train is {self.train}")

johnsApplication = RailwayForm()
johnsApplication.name = "John Smith"
johnsApplication.age = 32
johnsApplication.train = "Vande Bharat"
johnsApplication.printData()