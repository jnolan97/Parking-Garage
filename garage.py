class ParkingGarage():

    def __init__(self, ticket,ticket_list,parking_spaces,reserved,paid):
        self.ticket = ticket
        self.ticket_list = ticket_list
        self.parking_spaces = parking_spaces
        self.reserved = reserved
        self.paid = paid
    
    
    def takeTicket(self):
        # ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # parking_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # reserved = []
        
        for i in self.ticket_list:
            if self.ticket_list == []:
                print("Sorry! We're full.")
           
            elif i not in self.reserved:
                assign = i
                self.reserved.append(assign)
                self.ticket_list.remove(assign)
                self.parking_spaces.remove(assign)
                
                print(f"Your ticket is, {assign}")
                break
        return assign
   
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

    def showAvailable(self):
        print("Tickets Available: ", self.ticket_list)
        print("Parking Spaces Available: ", self.parking_spaces)
            


        
    
                
                
def run():
    driver = ParkingGarage(0,[1,2,3],[1,2,3],[],{'paid':False})
   
    
    while True:
        response = input("What do you want to do: park/exit/show?")
        
        if response.lower() == "park":
            driver.takeTicket()
        if response.lower() == "show":
            driver.showAvailable()
        
        if response.lower() == "exit":
            driver.payForParking()
            break
        
    
        
            
    




run()
