#include <iostream>
#include <cmath>
using namespace std;

class Point
{
protected:
    float x, y;

public:
    Point();
    Point(float x, float y);
    float length();
    float operator*(Point &p);
    friend ostream &operator<<(ostream &os, const Point &x);
};

// 3차원 class
class TPoint : public Point
{
    float z;

public:
    TPoint();
    TPoint(float x, float y, float z);
    float length(); // override
    float operator*(TPoint &p);
    friend ostream &operator<<(ostream &os, const TPoint &x);
};

Point::Point()
{
    x = 0;
    y = 0;
}

Point::Point(float x, float y) : x{x}, y{y} { ; }

float Point::length()
{
    return sqrt(x * x + y * y);
}

float Point::operator*(Point &p)
{
    return (x * p.x + y * p.y);
}

ostream &operator<<(ostream &os, const Point &x)
{
    os << '(' << x.x << ", " << x.y << ')';
    return os;
}

TPoint::TPoint() { z = 0; }

TPoint::TPoint(float x, float y, float z) : Point(x, y)
{
    this->z = z;
}

float TPoint::length() // override
{
    return sqrt(Pount::length() * Point::length() + z * z);
    // 부모의 이전 함수 명시적으로 호출 가능
}

float TPoint::operator*(TPoint &p)
{
    return (p.x * x + p.y * y + p.z * z);
}

ostream &operator<<(ostream &os, const TPoint &x)
{
    os << '(' << x.x << ", " << x.y << ", " << x.z << ')';
    return os;
}

int main()
{
    Point a(2, 5);
    Point b(3, -4);
    cout << b << endl;
    cout << b.length() << endl;
    cout << (a * b) << endl;

    TPoint ta(2, 5, 1);
    TPoint tb(3, -4, 5);
    cout << tb << endl;
    cout << tb.length() << endl;
    cout << (ta * tb) << endl;
    return 0;
}