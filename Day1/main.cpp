#include <iostream>
using namespace std;

int main() {
    // Demonstrating array with integers
    int arr[3];
    arr[0] = 10;
    arr[1] = 20;
    arr[2] = 30;

    cout << "Integer array address: " << arr << endl;

    // Demonstrating array with characters
    char charArr[3];
    charArr[0] = 'a';
    charArr[1] = 'b';
    charArr[2] = 'c';

    cout << "Character array value: " << charArr << endl;

    return 0;
}

// Sorting array with 0s and 1s without using algorithm
#include <iostream>
using namespace std;

int main() {
    int arr[] = {0, 0, 0, 1, 1};
    int count0 = 0, count1 = 0;

    for (int i = 0; i < 5; i++) {
        if (arr[i] == 0) count0++;
        else count1++;
    }

    for (int i = 0; i < count0; i++) arr[i] = 0;
    for (int i = count0; i < 5; i++) arr[i] = 1;

    for (int i = 0; i < 5; i++) cout << arr[i] << " ";
    cout << endl;

    return 0;
}
