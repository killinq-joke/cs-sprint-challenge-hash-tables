#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    obj = {}
    for i in tickets:
        obj[i.source] = i.destination
    key = obj["NONE"]
    route.append(key)
    while obj[key] != "NONE":
        route.append(obj[key])
        key = obj[key]
    route.append(obj[key])
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, len(tickets)))