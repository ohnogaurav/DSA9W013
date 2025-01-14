# Array Basics Revision Notes

## Definition
- **Array**: Collection or group of homogeneous data stored in continuous memory allocation with a fixed size.

## Key Concepts
1. **Indexing**:
   - Array indexing starts from `0` due to pointer arithmetic.
   - Example: `arr[0]` points to the first element's memory address.

2. **Dereference Variable**:
   - `*` operator is used to dereference pointers.

3. **Behavior of `cout`**:
   - `cout` with `int` array: Prints memory address.
   - `cout` with `char` array: Prints the entire string (value).

## Example Programs
### C++
```cpp
#include <iostream>
using namespace std;

int main() {
    // Integer array example
    int arr[3];
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;
    cout << arr << endl; // Prints address

    // Character array example
    char arr[3];
    arr[0] = 'a';
    arr[1] = 'b';
    arr[2] = 'c';
    cout << arr << endl; // Prints "abc"
    return 0;
}
```

## Sorting Binary Array without Algorithm
### Python
#### Using Extra Space
```python
arr = [0, 0, 1, 1, 0, 1, 1]
newarr = []
count0 = arr.count(0)
count1 = arr.count(1)
newarr = [0] * count0 + [1] * count1
print(newarr)
```
#### In-place Sorting
```python
arr = [0, 0, 1, 1, 0, 1, 1]
count0 = arr.count(0)
arr[:count0] = [0] * count0
arr[count0:] = [1] * (len(arr) - count0)
print(arr)
```

## Tasks and Examples
### Task 1: Hello World
```python
print("Hello, World!")
```

### Task 2: Swapping Numbers (5 Techniques)
1. Temporary variable.
2. Addition and subtraction.
3. Multiplication and division.
4. XOR operation.
5. Python tuple unpacking:
```python
a, b = b, a
```

### Finding Maximum Element in Array
#### Using `sort`
```python
arr = [1, 2, 3, 4, 5, 0, -1]
arr.sort()
print(f"Max no. in array is {arr[-1]}")
```
#### Without Using Sort
```python
arr = [1, 2, 3, 4, 5, 0, -1]
max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num
print(f"Max no. in array is {max_num}")
```

## Custom Sorting: Odd Ascending, Even Descending
#### Example 1
```python
user = int(input())
arr = []
evarr = []

for i in range(1, user + 1):
    if i % 2 != 0:
        arr.append(i)
    else:
        evarr.append(i)
evarr.sort(reverse=True)
arr.extend(evarr)
print(arr)
```
#### Example 2
```python
user = int(input())
arr = list(range(1, user + 1))
even = sorted([i for i in arr if i % 2 == 0], reverse=True)
odd = [i for i in arr if i % 2 != 0]
arr[:len(odd)] = odd
arr[len(odd):] = even
print(arr)
```
