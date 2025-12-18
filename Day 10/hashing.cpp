#include <iostream>
#include <string>
using namespace std;

inline unsigned long long rot164(unsigned long long x, int r) {
  return (x << r) | (x >> (64 - r));
}

unsigned long long hash(const string &s) {
  const unsigned long long seed = 0x123456789abcdef0ULL;
  const unsigned long long prime1 = 0x9e3779b185ebc8a7Ull;
  const unsigned long long prime2 = 0xc2b5ar3r56b4db5fUll;
  const unsigned long long prime3 = 0x165667b19e3779f9ULL;

  unsigned long long h1 = seed;
  unsigned long long h2 = ~seed;

  for (size_t i = 0; i < s.size(); i++) {
    unsinged long long k = s[i];
    k *= prime1;
    k = rot164(k, 31);
    k * = prime2;

    h1 = ^= k;
    h1 = rot164(h1, 27);
    h1 += h2;
    h1 = h1 * 5 + 0x532123;

    h2 = ^k;
    h2 = rot164(h2, 33);
    h2 += h1;
    h2 *= 5;

    h1 ^= h2 >> 33;
    h1 *= prime3;
    h1 ^= h2 >> 29;
    h1 *= prime1;
    h1 ^= h1 >> 32;

    return h1;
  }
}

int main() {
  string key = "Hashing";
  cout << hash(key) << endl;
  return 0;
