#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>


using namespace std;

int Answer;

int main(int argc, char** argv)
{
    int T, test_case;

    cin >> T;
    for(test_case = 0; test_case  < T; test_case++)
    {
        int n, k;
        vector<int> v;
        cin >> n >> k;
        for(int i = 0; i < n; i++) {
            int temp;
            scanf("%d", &temp);
            v.push_back(temp);
        }
        sort(v.begin(), v.end());

        Answer = 1;
        int cur = 0;

        for(int i = 1; i < n; i++) {
            if(v[i] - v[cur] <= k) {
                Answer++;
            }
            else {
                cur++;
            }
        }

        cout << "Case #" << test_case+1 << endl;
        cout << Answer << endl;
    }

    return 0;//Your program should return 0 on normal termination.
}