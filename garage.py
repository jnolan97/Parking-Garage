class ParkingGarage():

    def __init__(self, ticket,ticket_list,parking_spaces,reserved,paid):
        self.ticket = ticket
        self.ticket_list = ticket_list
        self.parking_spaces = parking_spaces
        self.reserved = reserved
        self.paid = paid
    
    
    def takeTicket(self):
        if not self.ticket_list:
            print("Sorry we're full!")
        for i in self.ticket_list:
            # if self.ticket_list == []:
            #     print("Sorry! We're full.")
            if i not in self.reserved:
                    #assign = i
                self.reserved.append(i)
                self.ticket_list.remove(i)
                self.parking_spaces.remove(i)
                print(f"Your ticket is, {i}")
                break
                #return assign
   
    def payForParking(self):
        while True:
            answer = input("Pay x amount: ")
            if int(answer) > 0:
                self.paid["paid"] = True
                print("Youre ticket has been payed you have 15 minutes to leave. \nHave a nice day!")
                break
            if int(answer) <= 0:
                self.paid["paid"] = False
                print("Please pay the ticket fee.")
    def removeDriver(self):
        user = int(input("Which driver are you checking out? "))
        for drivers in self.reserved:
            if user == drivers:
                self.reserved.remove(drivers)
                self.ticket_list.append(drivers)
                self.parking_spaces.append(drivers)
                self.ticket_list.sort()
                self.parking_spaces.sort()

    def showAvailable(self):
        print("Tickets Available: ", self.ticket_list)
        print("Parking Spaces Available: ", self.parking_spaces)
    
    def needToPay(self):
        if self.reserved:
            return True
        else:
            return False



        
    
                
                
def run():
    driver = ParkingGarage(0,[1,2,3],[1,2,3],[],{'paid':False})
   
    
    while True:
        response = input("What do you want to do: park/exit/show/checkout?")
        
        if response.lower() == "park":
            driver.takeTicket()
        if response.lower() == "show":
            driver.showAvailable()
        if response.lower() == "checkout":
            driver.removeDriver()
            driver.payForParking()
        if response.lower() == "exit" and driver.needToPay() == True:
            driver.payForParking()
            break
        if response.lower() == "exit" and driver.needToPay() == False:
            break
    
        
            
    




run()
