#include <iostream>
#include <vector>
#include <string>
using namespace std;

class PhoneNumber
{
private:
    string number;

public:
    PhoneNumber(string num);
    string masking(int k) const; // const -> member function을 바꾸 않는다!
    friend ostream &operator<<(ostream &os, const PhoneNumber &p);
    // operator overlaoding을 member func으로 선언하려면 operator 왼쪽이 나 자신
};

PhoneNumber::PhoneNumber(string num) : number{num} { ; }

string PhoneNumber::masking(int k) const
{
    string masked = "";
    for (int i = 0; i < number.length(); i++)
    {
        if (i < k)
            masked += '*';
        else
            masked += number[i];
    }
    return masked;
}

ostream &operator<<(ostream &os, const PhoneNumber &p) // friend -> member func아님
{
    // string masked = p.masking(7);
    os << p.masking(7);
    return os;
}

int main()
{
    PhoneNumber pn("01022223333");
    cout << pn << endl; // *******3333
}