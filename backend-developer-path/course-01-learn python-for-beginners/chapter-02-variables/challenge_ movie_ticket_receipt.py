movie_name = "Starlight"
ticket_count = 3
ticket_price = 8
amount_paid = 30

# my first attempt
print("Movie:", movie_name)
print("Tickets:", ticket_count, "| Total:", (ticket_count*ticket_price))
print("Change:", (amount_paid-ticket_count*ticket_price))

# improved attempt
total_cost = ticket_count * ticket_price
change = amount_paid - total_cost

print(f"Movie: {movie_name}")
print(f"Tickets: {ticket_count} | Total: {total_cost}")
print(f"Change {change}")

# Code above / assignment below

"""Movie Ticket Receipt
Use f-strings to complete the three print() calls in main.py. Use the provided variables rather than typing their values directly into your strings.

Print these lines in order, replacing the placeholders with the appropriate values:

Movie: <movie_name>
Tickets: <ticket_count> | Total: <total_cost>
Change: <change>
Calculate the total cost by multiplying the ticket count by the ticket price. Calculate the change by subtracting the total cost from the amount paid. You may create variables for these calculations or include them inside your f-strings.

For example, if the movie is Orbit, there are 2 tickets costing 5 each, and the customer pays 15, the output is:

Movie: Orbit
Tickets: 2 | Total: 10
Change: 5

Print only the three receipt lines, with the labels and punctuation shown above."""