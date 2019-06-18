#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;

int main (void) {
    char str[10001];
    vector<int> arr;
    bool good = false;
    int i = 0;
    scanf("%s", str);

    while(str[i] != '\0') {
        //arr.push_back(str[i] - '0');
        arr.push_back(atoi(&str[i]));
        i++;
    }

    for(int i = 0; i < 6; i++) {
        int sum = 0;
        for(int con = 0; con < arr.size(); con++) {
            int t = arr[con] * arr[con];
            sum += t;
        }
        arr.clear();
        if(sum == 1) {
            good = true;
            break;
        }
        while(sum > 0) {
            arr.push_back(sum % 10);
            sum /= 10;
        }
        sum = 0;
    }

    if(good) {
        printf("HAPPY\n");
    }
    else {
        printf("UNHAPPY\n");
    }
    return 0;
}
