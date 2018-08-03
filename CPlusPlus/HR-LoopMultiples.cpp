#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for( int m = 1; m <= 10; m = m + 1 ) {
    cout << n << " x " << m << " = " << n*m << endl;
  }

  return 0;
}
