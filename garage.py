class ParkingGarage():

   
    
    
    def __init__(self, ticket):
        self.ticket = "ticket"
        
    
    
    def takeTicket(self):
        ticket_list = [1,2,3,4,5,6,7,8,9,10]
        parking_spaces = [1,2,3,4,5,6,7,8,9,10]

        reserved = []
        
        for i in ticket_list:
            if i not in reserved:
                assign = i
                reserved.append(assign)
        print(f"Your ticket is, {assign}")
        print(reserved)
        return assign
        
#             for i in ticket_list:
#                 if i not in reserved:
#                     ticket_list.remove(i)
#                     parking_spaces.remove(i)
#                     reserved.append(i)
#                     reserved.append(i)
    
                
                
def run():
    driver = ParkingGarage(0)
    
    while True:
        response = input("What do you want to do?")
        
        if response.lower() == "park":
            driver.takeTicket()
        elif response.lower() == "exit":
            break
run()