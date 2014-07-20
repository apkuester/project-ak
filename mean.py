#made on 7/20/2014 
#print the mean of the numbers given in a file
import sys #library sys
sum = 0
n = 0
#Sum import values
for num in open('data.txt'): #open each file and look at each line in the file
	sum += float(num) #convert number to float
	n += 1 #add a number to each number
	
print sum/n #print the end sum divided by the n
#Very nice code, well done...:)