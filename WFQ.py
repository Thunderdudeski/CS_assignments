
input_stream = ["S Mary","P Dee","P Dee","E Eileen","E Mike","E Joe","P Dee","E Vicky","E George","P Dee","P Joe","E Sally","P Joe","S Pete","P Dee","S Bill","S Chase","E Price","P Dee","E Sue"]

def main():
    priority = []
    standard = []
    economy = []
    for string in input_stream: #sorts data stream from input list based off of the first letter
        match string[0]:
            case "P":
                priority.append(string)
            case "S":
                standard.append(string)
            case "E":
                economy.append(string)

    print_queues(priority, standard, economy)

def print_queues(priority, standard, economy):
    if len(priority) + len(standard) + len(economy) <= 0: # ends recursion once lists are empty
        return
    for x in range(clamp(len(priority), 0,3)): # prints 3 from priority queue if 3 are available
        print(priority[0])
        priority.pop(0)

    for x in range(clamp(len(priority), 0,2)): #prints 2 from standard queue if 2 are available
        print(standard[0])
        standard.pop(0)

    print(economy[0]) # prints 1 from economy queue if 1 is available
    economy.pop(0)

    print_queues(priority, standard, economy) # recursively calls print_queues function until all lists are empty

def clamp(n, minn, maxn): #clamps a number n within the minn and maxn values
    return max(min(maxn, n), minn)

if __name__ == '__main__':
    main()