"""Functions to manage and organize queues at Chaitana's roller coaster."""
normal_queue = ["Bob", "Mary", "Kyle", "Caroline"]
express_queue = ["Chad", "Brad", "Thad", "Tad"]

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number."""
    match ticket_type:
        case 1:
            normal_queue.append(person_name)
            return normal_queue
        case 2:
            express_queue.append(person_name)
            return express_queue
        case _:
            raise ValueError("Please check ticket type. Ticket type " + str(ticket_type) + " does not exist.")


def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index)."""
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue."""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name."""
    queue.pop(queue.index(person_name))
    return queue


def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue."""
    frens = 0
    for x in queue:
        if x == person_name:
            frens += 1
    return frens


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name."""
    getout = queue[len(queue)-1]
    queue.pop(queue.index(getout))
    return getout


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result."""
    singlefile = queue.copy()
    singlefile.sort()
    return singlefile
    
while True:

    menu = int(input("Welcome to the Coaster Queue Management System! Please enter the number for the function you wish to call: \n 1. Add visitor to the queue. \n 2. Find a visitor's position in queue. \n 3. Insert a visitor into the queue at a specific position. \n 4. Remove a visitor from the queue. \n 5. Count how many times the visitor appears in the queue. \n 6. Remove the last person from the queue. \n 7. Return a sorted list of members of the queue. \n Enter 0 to exit. \n"))
    if menu == 0:
        break
    if menu != 7:
        visitor = str(input("Please enter the visitor's name: "))
        ttype = int(input("Please enter the visitor's ticket type): "))
    if menu == 7:
        ttype = int(input("Please enter the queue type: "))

    match menu:
        case 1: 
            print("Adding the visitor to the queue.")
            print(add_me_to_the_queue(express_queue, normal_queue, ttype, visitor))
            print("Visitor has been successfully added!")
            input("Please press Enter to continue...")
        case 2:
            print("Finding visitor's position in the queue.")
            if ttype == 1:
                print("Visitor's position in the Normal Queue: ")
                print(find_my_friend(normal_queue, visitor))
            if ttype == 2:
                print("Visitor's position in the Express Queue: ")
                print(find_my_friend(express_queue, visitor))
            else: 
                ttype = input("Please check the user's ticket type.")        
            input("Please press Enter to continue...")
        case 3:
            print("Adding visitor to a specific position in queue.")
            newpos = int(input("Please enter the visitor's new position in the queue: "))
            if ttype == 1:
                print("Visitor's new position in the Normal Queue: ")
                print(add_me_with_my_friends(normal_queue, newpos, visitor))
            if ttype == 2:
                print("Visitor's new position in the Express Queue: ")
                print(add_me_with_my_friends(express_queue, newpos, visitor))
            if ttype != 1 and ttype != 2: 
                ttype = input("Please check the user's ticket type.")
            input("Please press Enter to continue...")
        case 4:
            print("Removing a visitor from the queue.")
            if ttype == 1:
                print("Visitor removed from Normal Queue.")
                print(remove_the_mean_person(normal_queue, person_name))
            if ttype == 2:
                print("Visitor removed from Express Queue.")
                print(remove_the_mean_person(express_queue, person_name))
            if ttype != 1 and ttype != 2: 
                ttype = input("Please check the user's ticket type.")
            input("Please press Enter to continue...")
        case 5:
            if ttype == 1:
                print("Visitor appears in Normal Queue: ")
                print(how_many_namefellows(normal_queue, person_name) + " times.")
            if ttype == 2:
                print("Visitor removed from Express Queue.")
                print(how_many_namefellows(express_queue, person_name) + " times.")
            if ttype != 1 and ttype != 2: 
                ttype = input("Please check the user's ticket type.")
            input("Please press Enter to continue...")
        case 6:
            if ttype == 1:
                print("Removing last visitor in Normal Queue.")
                print(remove_the_last_person(normal_queue))
            if ttype == 2:
                print("Removing last visitor in Express Queue.")
                print(remove_the_last_person(queue))
            if ttype != 1 and ttype != 2: 
                ttype = input("Please check the user's ticket type.")
            input("Please press Enter to continue...")
        case 7:
            if ttype == 1:
                print("Sorting the Normal Queue alphabetically.")
                print(sorted_names(normal_queue))
            if ttype == 2:
                print("Sorting the Express Queue alphabetically.")
                print(sorted_names(express_queue))
            if ttype != 1 and ttype != 2: 
                ttype = input("Please check the queue type.")
            input("Please press Enter to continue...")
        case 0:
            break

