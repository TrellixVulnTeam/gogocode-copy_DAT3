#include <iostream>
#include <time.h>
#include <iomanip>
using namespace std;
int main(){
    int count = 100000000;
    clock_t start, finish;
    double duration;
    int i;

    //不做运算的时间
    int looptime;
    i = count;
    start = clock();//记录开始时间
    while ( (i--))
    finish = clock();//记录结束时间
    looptime = finish - start;
    cout << "空循环：" << looptime << endl;

    //整数加法
    unsigned char uc = 200;
    i = count;
    start = clock();
    while(i--){
        uc += 7; 
    }
    finish = clock();
    cout << "8位整数：加法" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while (i--){
        uc *= 7;
    }
    finish = clock();
    cout << "8位整数：乘法" << finish - start - looptime << endl;

    //32位整数
    long long l = 200;
    i = count;
    start = clock();
    while(i--){
        l += 7;
    }
    finish = clock();
    cout << "32位整数：加法" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        l *= 7;
    }
    finish = clock();
    cout << "32位整数：乘法" << finish - start - looptime << endl;

    //64位整数
    long long ll = 200;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "64位整数：加法" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "64位整数：乘法" << finish - start - looptime << endl;

    //float
    float f = 3.1415926;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "float：加法" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "float：乘法" << finish - start - looptime << endl;

    //double
    double d = 3.1415926;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "double：加法" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "double：乘法" << finish - start - looptime << endl;
    return 0;
}
