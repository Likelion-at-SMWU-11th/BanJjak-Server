#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Complex
{
    float a, b;

public:
    Complex();
    Complex(float a, float b);
    Complex operator+(Complex &plus);
    friend ostream &operator<<(ostream &os, const Complex &x);
};

Complex::Complex()
{
    a = 0;
    b = 0;
}

Complex::Complex(float a, float b) : a{a}, b{b} { ; }

Complex Complex::operator+(Complex &plus)
{
    Complex x;
    x.a = this->a + plus.a;
    x.b = this->b + plus.b;

    return x;
}

ostream &operator<<(ostream &os, const Complex &x)
{
    if (x.a != 0)
        os << x.a << " ";
    // if (x.b < 0)
    //     os << " - " << -x.b << 'i';
    // else
    //     os << " + " << x.b << 'i';
    if (x.b > 0)
        os << "+ ";
    os << x.b << "i" << endl;
    return os;
}

int main()
{
    Complex a(2, 1);
    Complex b(3, -4);
    cout << (a + b) << endl;

    return 0;
}