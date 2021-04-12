# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie(item):
    for i in range(len(item)):
        if i >= 0:
            item[i] = "big"
    return item

print(biggie([-1, 3, 5, -5]))


# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(item):
    total = 0
    for i in item:
        if i > 0:
            total += 1
    item[-1] = total
    return item

print(count_positives([-1,1,1,1]))


# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(item):
    sum = 0
    for i in item:
        sum += i
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


# 4 Average - Create a function that takes a list and returns the average of all the values.
def average(item):
    sum = 0
    for i in item:
        sum += i
    return sum/len(item)

print(average([1,2,3,4]))


# 5 Length - Create a function that takes a list and returns the length of the list.
def length(item):
    return len(item)

print(length([37,2,1,-9]))


# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(item):
    if len(item) < 1:
        return False
    min = item[0]
    for i in item:
        if i < min:
            min = i
    return min

print(minimum([37,2,1,-9]))
print(minimum([]))


# 7 Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(item):
    if len(item) < 1:
        return False
    max = item[0]
    for i in item:
        if i > max:
            max = i
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))


# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimateAnalysis(item):
    dictionary = {'sumTotal': 0,'average': 0, 'minimum': item[0], 'maximum': item[0], 'length': len(item)}
    for i in item:
        if i < dictionary['minimum'] :
            dictionary['minimum'] = i
        if i > dictionary['maximum']:
            dictionary['maximum'] = i
        dictionary['sumTotal'] += i
        dictionary['average'] = dictionary['sumTotal']/len(item)
    return dictionary

print(ultimateAnalysis([37,2,1,-9]))


# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(item):
    for i in range(0, (len(item)-1)//2):
        temp = item[i]
        item[i] = item[len(item)-1-i]
        item[len(item)-1-i] = temp
    return item

print(reverse_list([37,2,1,-9]))

