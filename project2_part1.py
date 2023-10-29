#!/usr/bin/env python3
#def print_output(output):
    #write output to file
    #with open("output.txt", 'a') as file:
        #file.writelines(output)
        #file.close()
def generate_sublists(list):
    n = len(list)
    sublists = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublists.append(list[start:end])
    return sublists

def exhaustive_knapsack(W, items):
    best = None
    sublist_nested = generate_sublists(items)
    for candidate_items in sublist_nested:
        if verify_knapsack(W, items, candidate_items):
            if best == None or total_value(candidate_items) > total_value(best):
                best = candidate_items
    return best 


def verify_knapsack(W, items, candidate_items):
    total_weight = 0
    for item in candidate_items:
        total_weight += item[1]
    if total_weight <= W:
        return True
    else:
        return False

def total_value(candidate_items):
    total_value = 0
    for item in candidate_items:
        total_value += item[1] #This is the item weight
    return total_value

def main():
    #with open("input.txt", 'r') as file:
        #content =  file.readlines()
        #file.close()
    test_1size = 4
    test_1 = [[1,2], [4,3], [3,6], [6,7]]
    test_1amount = 12
    result = exhaustive_knapsack(test_1amount,test_1)
    print(result)
    print(total_value(result))
    #list_1 = [1,2,3]
    #sublist_nested = sublists(test_1)
    print("Hello World")
    #print(sublist_nested)

if __name__ == '__main__':
    main()
