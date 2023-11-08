#!/usr/bin/env python3
def print_output(output):
    #write output to file
    with open("output1.txt", 'a') as file:
        file.writelines(output)
        file.close()
def generate_sublists(list):
    n = len(list)
    sublists = []
    for start in range(1, 1 << n):
        sublists.append([list[j] for j in range(n) if (start & (1 << j))])
    return sublists

def exhaustive_knapsack(W, items):
    best = None
    sublist_nested = generate_sublists(items)
    for candidate_items in sublist_nested:
        if verify_knapsack(W, items, candidate_items):
            if best is None or total_stocks(candidate_items) > total_stocks(best):
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

def total_stocks(candidate_items):
    total_stock = 0
    for item in candidate_items:
        total_stock += item[0] #This is the stock
    return total_stock

def main():
    with open("input.txt", 'r') as file:
        content =  file.readlines()
        file.close()
    result = []
    compareTime = True
    while compareTime:
        if len(content) == 0:
            compareTime = False
            break
        elif len(content) == 1:
            compareTime = False
            content.remove(content[0])
            break
        else: 
            input1 = content[0]
            input1 = input1.replace('\n','')
            size1 = int(input1)
            input2 = content[1]
            list1 = eval(input2)
            input3 = content[2]
            amount1 = int(input3)
            output = exhaustive_knapsack(amount1,list1)
            result1 = str(total_stocks(output)) + '\n'
            result.append(result1)
            content.remove(content[3])
            content.remove(content[0])
            content.remove(content[0])
            content.remove(content[0])
    print_output(result)


if __name__ == '__main__':
    main()
