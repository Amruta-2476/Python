class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.seatsArray = list(range(1, seats+1))
    
    def info(self):
        print(f"Name of the train : {self.name}")
        print(f"The price of ticket is {self.fare}")
        print(f"Total no.of seats are {self.seats}")

    def bookTicket(self):
        print('your tickect is booked')
        self.seats = self.seats - 1
        self.seatsArray.pop(0)
    
    def currentStatus(self):
        print(f"Available seats are: {self.seatsArray}")

    def cancelTicket(self):
        seatNo = int(input("Enter your seat number: "))
        self.seats = self.seats + 1
        self.seatsArray.append(seatNo) 


train1 = Train("Rajdhani", 100, 10)  
train1.info()  
train1.currentStatus()  
train1.bookTicket()  
train1.info()
train1.cancelTicket()
train1.currentStatus()