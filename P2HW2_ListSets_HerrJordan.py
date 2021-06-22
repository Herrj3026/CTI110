#
# CTI-110
# P2HW2 - List and Sets
# Jordan Herr 
# 6/22/2021
#




##User input 1-10 inputs
#1
num_list = []
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#2
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)


#3
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#4
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#5
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#6
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#7
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#8
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#9
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)

#10
user_num = int(input("Enter a number for the list:"))
num_list.append(user_num)



#section of finding the min,max,length, sum, and average
length = len(num_list)
smallest = min(num_list)
largest = max(num_list)
total = sum(num_list)
average = sum(num_list)/len(num_list)


#coverting the list to a set
num_set = set(num_list)


#outputs
print("The lowest number in the list:", smallest)
print("The highest number in the list: ", largest)
print("The total numbers in this list: ", length)
print ("The sum of the numbers in this list: ",total)
print ("The averag of the numbers in this list: ",average)

print("This is the list converted into a set", num_set)








               
