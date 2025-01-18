sum of 2d array
arr=[[1,2],[3,4],[5,6,7]]
result=0

for main in range (len(arr)):
    subarr=arr[main]
    result=result+sum(subarr)

print((result))

# row sum col sum whole sum 2d array

#whole element sum
arr=[[1,2,3],[4,5,6],[7,8,9]]
length=len(arr)

sum of elements in array
sumarr=0
for i in range(length):
    subarr=arr[i]
    sumarr+=sum(subarr)
print(sumarr)



# sum of rows
rowsum=[]
for i in range(length):
    subarr=arr[i]
    rowsum.append(sum(subarr))
print(rowsum)


# sum of cols
colsum=[]
for i in range(length):
    esum=0
    for j in range(length):
        element=arr[j][i]
        esum+=element
    colsum.append(esum)
print(colsum)




#optimised
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(arr)

rowsum = [0] * length
colsum = [0] * length
total_sum = 0

for i in range(length):  # Loop through rows
    for j in range(length):  # Loop through columns
        element = arr[i][j]
        rowsum[i] += element
        colsum[j] += element
        total_sum += element

print("Total Sum:", total_sum)  # Whole array sum
print("Row Sums:", rowsum)      # Row-wise sums
print("Column Sums:", colsum)   # Column-wise sums

