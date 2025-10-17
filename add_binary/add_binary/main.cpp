#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int sum = 0;
        int carry = 0;

        int i = a.length() - 1;
        int j = b.length() - 1;

        while (i >= 0 || j >= 0 || carry == 1)
        {
            sum = carry;

            if (i >= 0)
            {
                sum += a[i] - '0';
                i--;
            }
            if (j >= 0)
            {
                sum += b[j] - '0';
                j--;
            }
            result += (sum % 2 + '0');
            carry = sum / 2;
        }
        reverse(result.begin(), result.end());
        return result;

    }
};

int main() 
{
    Solution sol;
    int choice;

    do 
    {
        cout << "\n===== Binary Adder Menu =====" << endl;
        cout << "1. Add two binary numbers" << endl;
        cout << "2. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) 
        {
            string a, b;
            cout << "Enter first binary number: ";
            cin >> a;
            cout << "Enter second binary number: ";
            cin >> b;

            // Validate inputs
            if (a.find_first_not_of("01") != string::npos || b.find_first_not_of("01") != string::npos) 
            {
                cout << "Error: Please enter valid binary numbers (only 0s and 1s)." << endl;
            }
            else 
            {
                string result = sol.addBinary(a, b);
                cout << "Result: " << result << endl;
            }
        }
        else if (choice == 2) 
        {
            cout << "Exiting program..." << endl;
        }
        else 
        {
            cout << "Invalid choice. Please try again." << endl;
        }

    } while (choice != 2);

    return 0;
}