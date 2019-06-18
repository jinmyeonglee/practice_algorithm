#include <cstdio>
#include <string>
#include <iostream>

struct Trie {
  struct Trie * go;
  struct Trie * fail;
  char label;
  bool output;
};

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; t++) {
        int n, m;
        std::string str, mark;
        scanf("%d %d", &n, &m);
        std::cin >> str;
        std::cin >> mark;
        for(int i = 0; i < m; i++) {
            for(int j = i + 1; j < m; j++) {

            }
        }
    }
    return 0;
}
