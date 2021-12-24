#include<iostream>
using namespace std;


int n = 10;

template< class t > t abs(t x){
    if (x < 0) return -x;
    return x;
}


int main(){
    int a = -1;
    float b = 2.0;
    double c  = -3.0, e;
    e = abs(a) + abs(b) + abs(c);
    cout << e << endl;
    return 0;
}
