#include <iostream>
#include <vector>

using namespace std;

class Utility
{
public:
    static bool isDiv(int a, int b);
    static bool isPrime(int a); //소수인지 판단하는 함수
};

bool Utility::isDiv(int a, int b)
{
    return a % b;
}

bool Utility::isPrime(int a)
{
    int i;
    for (i = 2; i < a; i++)
        if (!isDiv(a, i))
            break;
    if (i == a) //최초로 자기자신을 나눌 수 있는 수가 자기지신이면 소수
        return true;
    else
        return false;
}

class P : public Utility
{
protected:
    int n;

public:
    P(int n);
    virtual int solution() = 0;
    // virtual -> 동적할당하면 자식의 solution 호출
};

//실습 8번 n보다 작은 소수 개수 구하기
class P8 : public P //상속
{
public:
    P8(int n);
    virtual int solution();
};

P::P(int n)
{
    this->n = n;
}

P8::P8(int n) : P(n) { ; }

int P8::solution()
{
    int count = 0;
    for (int i = 2; i <= n; i++)
        if (isPrime(i))
            //상속받은 member fuction call, 상속받지 않으면 Utility::isPrime()
            count++;
    return count;
}

//실습9 최대공약수 구하기
class P9 : public P
{
protected:
    int m;

public:
    P9(int n, int m);
    virtual int solution();
};

P9::P9(int n, int m) : P(n)
{
    this->m = m;
}

int P9::solution()
{
    int gcd = 1;
    for (int i = 2; i <= n; i++)
    {
        if (!isDiv(n, i) && !isDiv(m, i))
            gcd = i;
    }
    return gcd;
}

class P92 : public P9
{
public:
    P92(int n, int m);
    virtual int solution();
};

P92::P92(int n, int m) : P9(n, m) { ; }

int P92::solution()
{
    int gcd = P9::solution();
    return n * m / gcd;
}

//실습 10 약수 합 구하기
class P10 : public P8
{
public:
    P10(int n);
    virtual int solution(); // override
};

P10::P10(int n) : P8(n) { ; } // P8, Utility 둘 다 상속

int P10::solution()
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
        if (!isDiv(n, i))
            sum += i;
    return sum;
}

int main()
{
    cout << "12, 4: " << Utility::isDiv(12, 4) << endl; // 12, 4: 0
    cout << "13, 4: " << Utility::isDiv(13, 4) << endl; // 13, 4: 1
    cout << "12: " << Utility::isPrime(12) << endl;     // 12: 0
    cout << "13: " << Utility::isPrime(13) << endl;     // 13: 1
    P8 myp8(10);
    cout << "10 이하의 소수 개수 P8(10): " << myp8.solution() << endl; // P8(10): 4
    P10 myp1001(12), myp1002(5);
    cout << "12 약수의 합 P10(12): " << myp1001.solution() << endl; // 12 약수의 합 P10(12): 28
    cout << "5 약수의 합 P10(5) : " << myp1002.solution() << endl;  // 5 약수의 합 P10(5) : 6

    P *first, *second;
    first = new P8(10);
    second = new P8(5);
    cout << "P8(10) : " << first->solution() << endl; // P8(10) : 4
    cout << "P8(5) : " << second->solution() << endl; // P8(5) : 3

    first = new P10(10);
    second = new P10(5);
    cout << "P10(10) : " << first->solution() << endl; // P10(10) : 18
    cout << "P10(5) : " << second->solution() << endl; // P10(5) : 6

    first = new P9(12, 8);
    second = new P9(13, 7);
    cout << "P9(12, 8) : " << first->solution() << endl;  // P9(12, 8) : 4
    cout << "P9(13, 7) : " << second->solution() << endl; // P9(13, 7) : 1

    first = new P92(12, 8);
    second = new P92(13, 7);
    cout << "P92(12, 8) : " << first->solution() << endl;  // P92(12, 8) : 24
    cout << "P92(13, 7) : " << second->solution() << endl; // P92(13, 7) : 91

    delete[] first;
    delete[] second;
}