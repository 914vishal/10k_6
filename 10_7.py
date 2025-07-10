# arr = [0,0,1,1,1,0,1,1,0]   ----->  3
# arr = [0,1,1,1,1,0,1,0,1,1,1]   ----->  4


arr = [0,0,1,1,1,0,1,1,0] 
maximum = 0
count = 0
for i in range(len(arr)):
    if arr[i]==1:
        count+=1
    else:
        if count>maximum:
            maximum=count
            count=0       
print(maximum)