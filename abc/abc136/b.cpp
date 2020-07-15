#include <iostream>
using namespace std;

int main(){
    int N, count=0;
    cin >> N;
    for(int i=1;i<=N;i++){
        int digit=0, num=i;
        while(num!=0){
            num/=10;
            digit++;
        }
        if(digit%2!=0){
            count++;
        }
    }
    cout << count;
    return 0;
}