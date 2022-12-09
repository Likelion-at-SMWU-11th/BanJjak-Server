#include <string>
#include <vector>
#include <iostream>

using namespace std;

class FX
{
protected:
    long long n;
    int diff(long long n, long long i);
    virtual int limit(); // virtual로 만들어야 함

public:
    FX(long long n);
    long long solution();
};

class FX2 : public FX
{
protected:
    int limit();

public:
    FX2(long long n);
    // long long solution(); // override할수도 있지만 중복 코드 증가
};

FX::FX(long long n) { this->n = n; }

FX2::FX2(long long n) : FX(n) { ; }

int FX::limit() { return 2; }

int FX2::limit() { return 3; }

long long FX::solution()
{
    long long i;
    for (i = n + 1; diff(n, i) > limit(); i++) // FX와 FX2에서 limit() 다른 함수 호출 -> virtual
        ;
    return i;
}

int FX::diff(long long n, long long i)
{
    int count = 0;
    int len = sizeof(n) * 8; // n의 비트 수 (sizeof()는 바이트 수로 리턴)
    long long mask = 1;
    for (int j = 0; j < len; j++)
    {
        if ((n & mask) != (i & mask))
            count++;      //다른 비트의 개수
        mask = mask << 1; //왼쪽으로 shift
    }
    return count;
}

// long long FX2::solution()
// {
//     long long i;
//     for (i = n + 1; diff(n, i) > 3; i++)
//         ;
//     return i;
// }

int main()
{
    long long n = 7;
    FX myfx(n);
    FX2 myfx2(n);
    cout << n << " : " << myfx.solution() << endl;  // 7 : 11 -> 3까지 허용
    cout << n << " : " << myfx2.solution() << endl; // 7 : 9  -> 3까지 허용
}