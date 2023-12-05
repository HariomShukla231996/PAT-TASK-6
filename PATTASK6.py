## 1. You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to create 
## two list one which have all the even numbers and another list which will have all the odd number in It?
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
even=[]
odd=[]
for num in list1:
  if num % 2 == 0:
    even.append(num)
  else:
    odd.append(num)
print(even)
print(odd)

## 2. given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to count all the prime numbers and create a new python list
## which will contain all the prime numbers in It?

list1 = [10, 501, 22, 37, 100, 999, 87, 351]
prime=[]

for i in list1:
  c = 0
  for j in range(1,i):
    if i%j==0:
      c+=1
      if c==1:
        prime.append(i)
print(prime)

## 3. given a Python List [10, 501, 22, 37, 100, 999, 87, 351] find 
# out how many numbers are there in the given python list which are happy numbers?

a = [10,501,22,37,100,999,87,351]
b = []
def is_happy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2
            sum = tempsum
        if sum == 1:
            b.append(a[i])
    return b
print(is_happy(a))

## 4. Write a python program to find sum of the first and last digits of an integer?

print("Enter a Number: ")
num = int(input())

count = 0
while num!=0:
    if count==0:
        last = num%10
        count = count+1
    rem = num%10
    num = int(num/10)

sum = rem + last
print("\nSum of first and last digit =", sum)

## 5. You have been given a list of N integers which represents the number of mangoes in a bag. 
# Each bag has a variable number of mangoes. There are M students in Guvi class, your task is to distribute the mangoes in such a way that each student gets one bag. 
# The difference between the number of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to student is minimum?

## 6. You have been given three lsits. 
# Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?

def find_duplicates(list1, list2, list3):

  duplicates = []
  for item in list1:
    if item in list2 and item in list3:
      duplicates.append(item)
  return duplicates


if __name__ == "__main__":
  list1 = [1, 2, 3, 4, 5]
  list2 = [3, 4, 5, 6, 7]
  list3 = [5, 6, 7, 8, 9]
  duplicates = find_duplicates(list1, list2, list3)
  print(duplicates)

## 7. Write a python program to find the first non repeating elements in the given list of integers?

def firstnon_repeating_element(list1):
    for i in range(len(list1)):
        if list1[i] not in list1[i + 1:]:
            return list1[i]
    return -1


list1 = [1, 2, 3, 1, 4, 2, 1, 2,3, 4]
print(firstnon_repeating_element(list1))

## 8. Write a python program to find the minimum element in a rated and sorted list?

list2 = [3, 4, 5, 8, 9, 10]
print(min(list2))

## 9. You have been given a python list [10, 20, 30, 9] and a value of 59. 
# Write a python program to find the triplet in the list whose sum is equal to the given value?

## 10. Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to zero?

def subArrayExists(arr, n):
	for i in range(n):
		# Starting point of the subarray and
		# sum is initialized with the first element of subarray
		sum = arr[i]
		if sum == 0:
			return True
		for j in range(i + 1, n):
			sum += arr[j]
			if sum == 0:
				return True
	return False

# Driver's code
if __name__ == "__main__":
	arr = [-3, 2, 3, 1, 6]
	N = len(arr)

	# Function call
	if subArrayExists(arr, N):
		print("Found a subarray with 0 sum")
	else:
		print("No Such Sub Array Exists!")



