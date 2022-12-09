#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(void)
{
    int val1, val2, val3;
    int largest, mid, smallest;

    cin >> val1 >> val2 >> val3;
    if (val1 <= val2)
    {
        if (val2 <= val3)
        {
            largest = val3;
            mid = val2;
            smallest = val1;
        }
        else
        {
            largest = val2;
            if (val1 <= val3)
            {
                mid = val3;
                smallest = val1;
            }
            else
            {
                mid = val1;
                smallest = val3;
            }
        }
    }
    else
    { // val1>val2
        if (val1 <= val3)
        {
            largest = val3;
            mid = val1;
            smallest = val2;
        }
        else
        {
            largest = val1;
            if (val2 <= val3)
            {
                mid = val3;
                smallest = val2;
            }
            else
            {
                mid = val2;
                smallest = val3;
            }
        }
    }

    /*
    if(val1 > val2 && val1>val3){
        largest = val1;
        if(val2 > val3){
            mid = val2;
            smallest = val3;
        }else{
            mid = val3;
            smallest = val2;
        }
    }
    else if(val2 > val1 && val2>val3){
        largest = val2;
        if(val1 > val3){
            mid = val1;
            smallest = val3;
        }else{
            mid = val3;
            smallest = val1;
        }
    }
    else{
        largest = val3;
        if(val1 > val2){
            mid = val1;
            smallest = val2;
        }else{
            mid = val2;
            smallest = val1;
        }
    }
    */
    cout << "largest : " << largest << "  middle : " << mid << "  smallest : " << smallest << endl;

    return 0;
}
