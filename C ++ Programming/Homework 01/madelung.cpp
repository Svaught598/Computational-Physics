#include <iostream>
#include <cmath>
using namespace std;



double madelung_constant(int L) 
{
    double madelung_cnst = 0;
    float temp = 0;

    for (int i = -L; i <= L; i++)
    {
        for (int j = -L; j <= L; j++)
        {
            for (int k = -L; k <= L; k++)
            {
                if (i == 0 && j == 0 && k == 0)
                {
                    madelung_cnst += 0;
                }
                else if ((i + j + k) % 2 == 0) 
                {
                    temp = pow(i, 2) + pow(j, 2) + pow(k, 2);
                    madelung_cnst -= 1/sqrt( (float) temp);
                }
                else 
                {
                    temp = pow(i, 2) + pow(j, 2) + pow(k, 2);
                    madelung_cnst += 1/sqrt(temp);
                }
            }
        }
    }
    return madelung_cnst;
}

int main() 
{
    cout << "The Madelung Constant for NaCl is: " << madelung_constant(100) << endl;
    cout << sqrt(6.5) << endl;
    cout << pow(2, 2) << endl;
    return 0;
}

