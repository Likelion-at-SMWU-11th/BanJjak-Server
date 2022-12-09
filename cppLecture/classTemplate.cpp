#include <iostream>

using namespace std;

template <class T, int N>
class mysequence
{
    T memblock[N];

public:
    void setmember(int x, T value);
    T getmember(int x);
};

template <class T, int N>
void mysequence<T, N>::setmember(int x, T value)
{
    memblock[x] = value;
}

template <class T, int N>
T mysequence<T, N>::getmember(int x)
{
    return memblock[x];
}

int main()
{
    mysequence<int, 5> myints;
    myints.setmember(0, 100);
    cout << myints.getmember(0) << endl;

    mysequence<double, 5> myfloats;
    myfloats.setmember(3, 3.1316);
    cout << myfloats.getmember(3) << endl;
}