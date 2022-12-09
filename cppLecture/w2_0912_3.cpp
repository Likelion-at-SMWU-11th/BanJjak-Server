#include <iostream>
//#include <cstring>

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
    int var;

    cin >> var;

    if (var % 2)
    {
        cout << "The value " << var << " is an odd number" << endl;
    }
    else
    {
        cout << "The value " << var << " is an even number" << endl;
    }

    /*
    string cat;
    if(var % 2 == 0)
        cat = "even";
    else
        cat = "odd";
    cout << "The value " << var << " is an " << cat << " number" << endl;
    */

    return 0;
}