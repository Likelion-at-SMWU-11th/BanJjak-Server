#include <iostream>

using namespace std;

int main(void)
{
    char opt;
    double var1, var2, result;

    cin >> opt >> var1 >> var2;

    switch (opt)
    {
    case '+':
        result = var1 + var2;
        break;
    case '-':
        result = var1 - var2;
        break;
    case '*':
        result = var1 * var2;
        break;
    case '/':
        result = var1 / var2;
        break;
    default:
        cout << "Not a case" << endl;
    }
    cout << "result : " << result << endl;
    return 0;
}
