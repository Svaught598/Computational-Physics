#include <iostream>
using namespace std;


int main() 
{
    int fib(int x);
    int big = 40;
    //do NOT go above 40!!!

    for (int i = 0; i < big; i++) {
        cout << i << " " << fib(i) << "\n";
    }

    return 0;

}

int fib(int x) 
{
    int temp;

    if (x < 0) {
        return 0;
    }

    else if (x == 1 or x == 0) {
        return 1;
    }

    else {
        return fib(x - 1) + fib(x - 2);
    }
}