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
            if i not in self.reserved:
                assign = i
                self.reserved.append(assign)
                self.ticket_list.remove(assign)
                self.parking_spaces.remove(assign)
                break
        print(f"Your ticket is, {assign}")
        return assign
    def payForParking(self):
        answer = input("Pay x amount: ")
        if int(answer) > 0:
            self.paid["paid"] = True
            print("Youre ticket has been payed you have 15 minutes to leave.")
        else:
            self.paid["paid"] = False

        
    
                
                
def run():
    driver = ParkingGarage(0,[1,2,3],[1,2,3],[],{'paid':False})
    
    while True:
        response = input("What do you want to do?")
        
        if response.lower() == "park":
            driver.takeTicket()
        if response.lower() == "pay":
            driver.payForParking()
        elif response.lower() == "exit":
            break
run()
