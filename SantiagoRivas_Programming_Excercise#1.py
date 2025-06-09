# Create Function to create the program.
def buy_tickets(remaining_tickets):
    #Make sure the amount of tickets that the user is requesting follow the requirements. Not more than 1-4
    while True:
        try:
            num = int(input("How many tickets would you like to buy (1-4)? "))
            if 1 <= num <= 4:
                if num <= remaining_tickets:
                    return num
                else:
                    print(f"Only {remaining_tickets} tickets are left. Try again.")
            else:
                print("You can only buy between 1 and 4 tickets.")
       #Make an exception in case the number requested is bigger than the maximum amount.
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

# Function to run the ticket selling process, setting the amount of total tickets and buyers.
def sell_tickets():
    total_tickets = 20
    buyers = 0  # accumulator to count number of buyers

    while total_tickets > 0:
        print(f"\nTickets remaining: {total_tickets}")
        tickets_bought = buy_tickets(total_tickets)
        total_tickets -= tickets_bought
        buyers += 1  # count each successful buyer

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {buyers}")

# Finish the program.
sell_tickets()
