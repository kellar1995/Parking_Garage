class Garage:

    def __init__(self):
        self.ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.current_tickets = {
            "unpaid" : []
        }


    def take_ticket(self): #decreases tickets and spaces by 1
        tickets_taken = self.ticket.pop(0)
        spaces_taken = self.spaces.pop(0)
        ticket_dict = {
            "ticket" : tickets_taken, 
            "space" : spaces_taken
        }
        self.current_tickets["unpaid"].append(ticket_dict)
        print(f"Your ticket number is {tickets_taken}")


    def pay_for_parking(self):
        num = int(input("What is your ticket number?"))
        for ticket in range(len(self.current_tickets["unpaid"])):
            if self.current_tickets["unpaid"][ticket]["ticket"] == num:
                returned_tickets = self.current_tickets["unpaid"].pop(ticket)
                self.ticket.append(returned_tickets["ticket"])
                self.spaces.append(returned_tickets["space"])
            else:
                print("That is an invalid ticket number. Please try again.")

    
    def leave_garage(self):
        goodbye = int(input("What is your ticket number?"))
        for y in range(len(self.current_tickets["unpaid"])):
            if self.current_tickets["unpaid"][y]["ticket"] == goodbye:
                print("Please pay for your ticket first. Redirecting you to the pay portal now.")
                

        for x in self.ticket:
            if x == goodbye:
                print("Thank you, have a nice day!")
                break

        # pay = self.currect_tickets["unpaid"][1]["ticket"].pop(num)
        # if num not in self.currect_tickets["unpaid"][0]["ticket"]:

        #self.current_tickets{
        #   "unpaid" : [
        #       ticket_dict {
        #   
        #           "ticket" : tickets_taken
        #           "space"   : spaces_taken
        # }
        # ] 
        # }



            # for x in self.currect_tickets[ticket_dict][ticket]:
            #     self.ticket.append(num)
            # for y in self.currect_tickets[ticket_dict][space]:
            #     self.spaces.append(num)

            
        #-update our dict. from unpaid to paid
        #print("Thank you, you have 15 minutes to leave")
    
    
        # if paid , print("Thanks have a nice day")
        # if unpaid, print("Please pay.")
        # update spaces +1
        # update tickets +1


# class Car:

#     def __init__(self, name):
#         self.name = input("What is your name?")



def run():
    our_garage = Garage()
    while True:
        enter = input("Welcome to our garage! Would you like to take a ticket?").lower()
        if enter == "yes":
            our_garage.take_ticket()
        elif enter == "no":
            print("Please turn around.")
            break
        else:
            print("That is not a valid response.")

        choice = input("Would you like to take another ticket, pay for your ticket, or leave the garage?").lower()
        if choice == "take":
            our_garage.take_ticket()
        if choice == "pay":
            our_garage.pay_for_parking()
        elif choice == "leave":
            our_garage.leave_garage()


run()        