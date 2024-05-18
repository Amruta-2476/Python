# write a class Train which has methods to book a ticket, get status(no. of seats) and get fare info of trains under Indian Railways
class Train:
    trainsUnder = "Indian Railways"
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def getStatus(self):
        print(f"The {self.name} express has {self.seats} no.of seats.")
    def getFareInfo(self):
        print(f"The price of ticket is {self.fare}")
    def bookATicket(self):
        if(self.seats > 0):
            print(f"Your ticket is booked! Your seat number is {self.seats}")
            self.seats =  self.seats -1
        else:
            print("sorry this train is full")

print(Train.trainsUnder)
train1 = Train("Janshatabdi", 400, "Rs.100")
train1.getStatus()
train1.getFareInfo()
train1.bookATicket()
train1.getStatus()

print("............................")
train2 = Train("Vande Bharat", 500, "Rs.600")
train2.getStatus()
train2.getFareInfo()
train2.bookATicket()
train2.getStatus()