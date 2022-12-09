#include <iostream>

using std::cin;
using std::cout;
using std::endl;

// extern int j; // int j가 어딘가 있음 -> compiler에게 알려줌
int main(void)
{
    int val1, val2;
    int largest, smallest; //초기화하는 것이 좋은 습관, but 초기화하기 전에 사용X

    cout << "Please enter two integers : ";
    cin >> val1 >> val2;

    if (val1 > val2)
    {
        largest = val1;
        smallest = val2;
    }
    else
    {
        largest = val2;
        smallest = val1;
    }

    cout << "largest : " << largest << endl;
    /* endline 권장 : '\n'
    줄바꿈 - 두 개의 축(x축, y축)을 바꿔줘야 함 : os마다 다름
    1. 2개의 코드 이용
    2. 1개의 코드 이용
    : \n -> 2개의 코드가 필요한 os에서는 error
    :endl -> machine dependacny를 줄여줌*/
    cout << "smallest : " << smallest << endl;
    cout << "sum : " << (largest + smallest) << endl; // +가 << 우선순위 높음 - 확실하게 ()
    cout << "difference : " << (largest - smallest) << endl;
    cout << "mul : " << largest * smallest << endl;
    cout << "ratio : " << (largest / smallest) << endl;

    return 0;
}