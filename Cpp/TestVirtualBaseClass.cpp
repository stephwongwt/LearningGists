#include <iostream>
using namespace std;

class A { 
public:
    A() // constructor 
    { 
      a = 10;
      cout << "I am A: " << a << endl;
    }

    void testA(int ina) {
      a = ina;
      cout << "testA "<< a << endl;
    }

    void seta(int ina) {
      a = ina;
      cout << "setA "<< a << endl;
    }
private:
  int a;
}; 
  
class B : private virtual A {
public:
  void testA(int ina) {
    cout << "testA actually B "<< ina << endl;
  }
  void testB(int ina) {
    seta(ina);
    cout << "testB "<< ina << endl;
  }
};

int main() {
	A objA; //I am A: 10
	B objB; //I am A: 10
  objA.testA(1); //testA 1
  objB.testA(2); //testA actually B 2
  objB.testB(3); // setA 3
                 // testB 3
  objB.testA(4); // testA actually B 4
	return 0;
}
