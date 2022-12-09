//헤더파일에 declaration 모아둠
class Negative
{
};

class Sample
{
private:
    int n;
    int m;
    void setM(int x, int y);

public:
    Sample();
    Sample(int x);
    Sample(const Sample &a);
    ~Sample(); // destructor -> 메모리에서 사라질 때 불림
    void setM(int x);
    int getM() const;
    Sample operator+(Sample &a);
    friend Sample operator-(const Sample &a, const Sample &b); // friend -> special한 function, private 오픈, 뒤에 정의할 함수는 외부 함수
};

// cpp 파일
#include <iostream>

using namespace std;

Sample::Sample()
{
    m = 0;
    cout << "Sample() is called." << endl;
}
Sample::Sample(int x) //: m{x} // member variable 선언 가능 m=x; 와 동일
{
    // m = x;
    this->m = m; // scope이 다르면 동일 변수 이름 허용
    //왼쪽 m은 class scope(class member function) / 오른쪽 m은 local scope(파라미터)
    cout << "Sample(int x) is called." << endl;
}
Sample::Sample(const Sample &a) //파라미터가 나 자신
{
    m = a.m + 1000; //클래스 내부 -> private에 바로 access 가능(getM()사용X)
}
Sample::~Sample()
{ // destructor는 하나만 정의 가능
    cout << m << " ~Sample() is called." << endl;
}

void Sample::setM(int x)
{
    m = x;
}

int Sample::getM() const
{
    return m;
}

Sample Sample::operator+(Sample &a) //연속적인 덧셈 가능하도록 Sample return
{
    Sample x;            //새로운 x 만들기
    x.m = this->m + a.m; //각각의 m, n 계산
    x.n = this->n + a.n;
    return x;
}

Sample operator-(const Sample &a, const Sample &b) // global 함수, Sample:: 안함
{
    Sample x;
    x.m = a.m - b.m;
    x.n = a.n - b.n;
    return x;
}

int main()
{
    Sample x; //스택에 저장
    cout << "x" << endl;
    Sample *w; // pointer variable -> constructor와 관련X, 주소만 저장 4bytes 크기
    w = new Sample();
    cout << "w" << endl;
    // malloc -> heap : 사라지는 순서가 중괄호에 결정X
    // Java에서는 garbage collector가 자동으로 삭제

    x.getM();  // class의 member .
    w->getM(); //포인터 변수의 member variable은 ->

    {
        Sample y;
        cout << "y" << endl;
        x.setM(2);
        y.setM(20);
        Sample y2(y);
        Sample y3;
        y3 = x + y;

        {
            delete w;
            Sample z(100);
            cout << "z" << endl;
            cout << "x.m = " << x.getM() << endl;
            cout << "y.m = " << y.getM() << endl;
            cout << "z.m = " << z.getM() << endl;
            cout << "y2.m = " << y2.getM() << endl;
            cout << "y3.m = " << y3.getM() << endl;
            cout << "z sizeof " << sizeof(z) << endl;
        }
    }
}