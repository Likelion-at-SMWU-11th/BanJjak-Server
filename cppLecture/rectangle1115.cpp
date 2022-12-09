#include <iostream>

using namespace std;

class Polygon
{
protected:
	int m, n;

public:
	Polygon(int m, int n);
	virtual ~Polygon();
	virtual void draw() = 0; // polygon에서는 draw() 정의X / 선언만
							 //상속받을 class의 의무 나열 -> return과 파라미터가 없는 draw() 함수 반드시 필요
};

class Rect : public Polygon
{
public:
	Rect(int m, int n);
	~Rect();
	void draw(); // override
};

class Triangle : public Polygon
{
public:
	Triangle(int m, int n);
	~Triangle();
	void draw();
};

class MyMulti : public string, public Rect
{
public:
	MyMulti(int m, int n, const char *str);
};

Polygon::Polygon(int m, int n)
{
	this->m = m;
	this->n = n;
}

Polygon::~Polygon()
{
	cout << "Polygon::~Polygon()" << endl;
}

Rect::Rect(int m, int n) : Polygon(m, n) { ; }

Rect::~Rect()
{
	cout << "Rect::~Rect()" << endl;
}

void Rect::draw()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cout << '*';
		cout << endl;
	}
}

Triangle::Triangle(int m, int n) : Polygon(m, n) { ; }

Triangle::~Triangle()
{
	cout << "Triangle::~Triangle()" << endl;
}

void Triangle::draw()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
			cout << '*';
		cout << endl;
	}
}

MyMulti::MyMulti(int m, int n, const char *str) : Rect(m, n), string(str)
{
	;
}

int main(void)
{
	// Polygon *pol;
	// int a;
	// int b;
	// int type;
	// cin >> type >> a >> b;

	// if (type == 3)
	// 	pol = new Triangle(a, b);
	// else if (type == 4)
	// 	pol = new Rect(a, b);

	// pol->draw();
	// delete pol; //메모리 반환

	MyMulti test(5, 3, "abc");
	test.draw();
	cout << test << endl; // string의 cout
	cout << test[2] << endl;

	return 0;
}