#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    string line;
    string input[] = {};

    while(getline(cin, line)) {
        input.push_back(line);
    }

    for (int i=0; i<input.length; i++) {
        cout << input[i] << endl;
    }
}