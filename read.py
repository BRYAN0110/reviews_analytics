data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		sum_len = sum_len + len(data[count])
		count += 1
print(sum_len)	 
average_len = sum_len / len(data)
print(average_len)
		
