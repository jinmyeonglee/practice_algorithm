#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int Answer;

int main(int argc, char** argv)
{
    int T, test_case;

    cin >> T;
    for(test_case = 0; test_case  < T; test_case++)
    {
        int n, m;
        cin >> n >> m;
        vector< vector<int> > v(n + 1, vector<int> (n + 1, 0));
        for(int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            v[a][b] = v[b][a] = 1;
        }

        Answer = 0;

        // Print the answer to standard output(screen).
        cout << "Case #" << test_case+1 << endl;
        cout << Answer << endl;
    }

    return 0;//Your program should return 0 on normal termination.
}