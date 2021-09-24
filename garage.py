class Garage:

    def __init__(self):
        self.ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currect_tickets = {}


    def take_ticket(self):
        for tickets in self.ticket:
            
        #-decreases tickets by 1

    
    def pay_for_parking(self):
        #-update our dict. from unpaid to paid
        #print("Thank you, you have 15 minutes to leave")
    
    def leave_garage(self):
        # if paid , print("Thanks have a nice day")
        # if unpaid, print("Please pay.")
        # update spaces +1
        # update tickets +1


def run():
    our_garage = Garage()
    while True:
        print("Welcome to our garage! Please take a ticket.")