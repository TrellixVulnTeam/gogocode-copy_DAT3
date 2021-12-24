#include <iostream>
#include <time.h>
#include <iomanip>
using namespace std;
int main(){
    int count = 100000000;
    clock_t start, finish;
    double duration;
    int i;

    //���������ʱ��
    int looptime;
    i = count;
    start = clock();//��¼��ʼʱ��
    while ( (i--))
    finish = clock();//��¼����ʱ��
    looptime = finish - start;
    cout << "��ѭ����" << looptime << endl;

    //�����ӷ�
    unsigned char uc = 200;
    i = count;
    start = clock();
    while(i--){
        uc += 7; 
    }
    finish = clock();
    cout << "8λ�������ӷ�" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while (i--){
        uc *= 7;
    }
    finish = clock();
    cout << "8λ�������˷�" << finish - start - looptime << endl;

    //32λ����
    long long l = 200;
    i = count;
    start = clock();
    while(i--){
        l += 7;
    }
    finish = clock();
    cout << "32λ�������ӷ�" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        l *= 7;
    }
    finish = clock();
    cout << "32λ�������˷�" << finish - start - looptime << endl;

    //64λ����
    long long ll = 200;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "64λ�������ӷ�" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "64λ�������˷�" << finish - start - looptime << endl;

    //float
    float f = 3.1415926;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "float���ӷ�" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "float���˷�" << finish - start - looptime << endl;

    //double
    double d = 3.1415926;
    i = count;
    start = clock();
    while(i--){
        ll += 7;
    }
    finish = clock();
    cout << "double���ӷ�" << finish - start - looptime << endl;

    i = count;
    start = clock();
    while(i--){
        ll *= 7;
    }
    finish = clock();
    cout << "double���˷�" << finish - start - looptime << endl;
    return 0;
}
