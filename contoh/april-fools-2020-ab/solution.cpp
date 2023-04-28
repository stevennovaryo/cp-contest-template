#include <bits/stdc++.h>
using namespace std;

const int MOD = 1009;

int a, b;

int main() {
  scanf("%d %d", &a, &b);
  int ans = 1;
  if (b >= MOD) {
    ans = 0;
  } else {
    for (int i = 1; i <= b; ++i) {
      ans = 1LL * ans * i % MOD;
    }
  }

  ans = (ans + a) % MOD;
  printf("%d\n", ans);
  return 0;
}
