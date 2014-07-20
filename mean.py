
import sys #library sys
sum = 0
n = 0
#Sum import values
for num in sys.stdin: #each line is going into a num
	sum += float(num) #convert number to float
	n -= 1 #subtract a number from each number
	
print sum/n #print the end sum divided by the n