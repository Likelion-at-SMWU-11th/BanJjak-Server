#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Path
{
    int x1, x2, y1, y2;

public:
    Path(int xx1, int yy1, int xx2, int yy2);
    friend bool operator==(Path &a, Path &b);
};

// Path를 기록하는 class
class PathQue
{
    vector<Path> paths;
    bool isIn(Path a);

public:
    void push(Path a);
    int count();
};

class MyGame
{
    int x, y;
    PathQue myque;
    void move(char c);

public:
    MyGame();
    void move(string &commands);
    int getX();
    int getY();
    int getCount();
};

class OutofBound
{
};

Path::Path(int xx1, int yy1, int xx2, int yy2)
{
    x1 = xx1;
    y1 = yy1;
    x2 = xx2;
    y2 = yy2;
}

bool operator==(Path &a, Path &b)
{
    if (a.x1 == b.x1 && a.x2 == b.x2 && a.y1 == b.y1 && a.y2 == b.y2)
        return true;
    if (a.x1 == b.x2 && a.x2 == b.x1 && a.y1 == b.y2 && a.y2 == b.y1)
        return true;
    return false;
}

void PathQue::push(Path a)
{
    if (!isIn(a))
        paths.push_back(a);
}

bool PathQue::isIn(Path a)
{
    for (int i = 0; i < paths.size(); i++)
        if (paths[i] == a)
            return true;

    return false;
}

int PathQue::count()
{
    return paths.size();
}

MyGame::MyGame()
{
    x = 0;
    y = 0;
}

int MyGame::getX() { return x; }
int MyGame::getY() { return y; }

int MyGame::getCount()
{
    return myque.count();
}

void MyGame::move(string &commands)
{
    for (int i = 0; i < commands.length(); i++)
        try
        {
            int preX = x; //이전 위
            int preY = y;
            move(commands[i]); //한글자씩 이동
            Path temp(preX, preY, x, y);
            myque.push(temp); //큐에 넣기
        }
        catch (OutofBound &e) // move가 exception -> push() 자동 생략
        {
        }
}

void MyGame::move(char c)
{
    switch (c)
    {
    case 'U':
        if (y == 5)
            throw OutofBound();
        else
            y++;
        break;
    case 'D':
        if (y == -5)
            throw OutofBound();
        else
            y--;
        break;
    case 'L':
        if (x == 5)
            throw OutofBound();
        else
            x++;
        break;
    case 'R':
        if (x == -5)
            throw OutofBound();
        else
            x--;
    default:
        break;
    }
}

int main()
{
    MyGame game;
    string commands = "ULURRDLLU";
    game.move(commands);
    cout << "끝난 후 위치 : (" << game.getX() << "," << game.getY() << ")" << endl; //끝난 후 위치 : (1,2)
    Path path1(1, 2, 3, 4), path2(3, 4, 1, 2);
    cout << (path1 == path2) << endl; // 1
    Path path3(1, 2, 3, 4), path4(3, 4, 1, 1);
    cout << (path3 == path4) << endl; // 0
    PathQue myque;
    myque.push(path1);
    myque.push(path2);
    myque.push(path3);
    myque.push(path4);
    cout << myque.count() << endl;                       // 2
    cout << "이동한 거리 : " << game.getCount() << endl; // 7
    return 0;
}