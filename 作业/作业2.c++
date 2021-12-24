#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    double s = 1;
    int k = 1, t = 1;
    while (1.0 / (k + 1) > 1e-5){
        t *= -1;
        s += t / (double) (k + 1);
        k++;
    }
    cout << s << endl;
    return 0;
}