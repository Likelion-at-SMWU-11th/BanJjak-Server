#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
    std::string digit;
    cin >> digit;
    // switch문 : 파라미터로 user-define를 받지 않음 - stringX (int, float,...가능)

    if (digit == "zero") // java에서는 주소 비교, cpp에서는 value 비교
        cout << 0;
    else if (digit == "one")
        cout << 1;
    else if (digit == "two")
        cout << 2;
    else if (digit == "three")
        cout << 3;
    else if (digit == "four")
        cout << 4;
    else
        cout << "not a value I know";

    return 0;
}