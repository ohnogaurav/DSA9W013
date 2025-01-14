# Finding max element in array
arr = [1, 2, 3, 4, 5, 0, -1]
max_num = arr[0]

for num in arr:
    if num > max_num:
        max_num = num

print(f"Max no. in array is {max_num}")

# Without using extra space
arr = [0, 0, 1, 1, 0, 1, 1]
count0 = 0
count1 = 0

for i in arr:
    if i == 0:
        count0 += 1
    elif i == 1:
        count1 += 1

arr[:count0] = [0] * count0
arr[count0:] = [1] * count1

print(arr)

# Odd-Even arrangement: Odd numbers first, even numbers in reverse order
user = int(input())
arr = []
evarr = []

for i in range(1, user + 1):
    if i % 2 != 0:
        arr.append(i)

for i in range(1, user + 1):
    if i % 2 == 0:
        evarr.append(i)
evarr.sort(reverse=True)
for i in evarr:
    arr.append(i)

print(arr)

# Another odd-even arrangement
user = int(input())
arr = [i for i in range(1, user + 1)]
even = []
odd = []

for i in arr:
    if i % 2 != 0:
        odd.append(i)
    elif i % 2 == 0:
        even.append(i)

even.sort(reverse=True)
arr[:len(odd)] = odd
arr[len(odd):] = even

print(arr)
