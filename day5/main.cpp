#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "  we  are   doing   string  ";
    int count = 0;
    bool inWord = false;

    for (char c : s) {
        if (c != ' ') {
            if (!inWord) {
                count++;
                inWord = true;
            }
        } else {
            inWord = false;
        }
    }

    cout << count << endl;
    return 0;
}




// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
//     string s = "we are doing    string";
//     int count = 0;

//     // Use s.length() for the loop condition instead of n
//     for (int i = 0; i < s.length(); i++) {
//         if (s[i] == ' ') count++;
//     }

//     // Calculate the number of words
//     int ans = count + 1;

//     // Check for an empty string
//     if (s.length() == 0) ans = 0;

//     cout << ans; // Corrected to output the number of words
//     return 0;
// }
