#include<iostream>
using namespace std;

int main(){
    int N;
    int H[100000];
    cin >> N;
    for(int i=0;i<N;++i) cin >> H[i];
    for (int i=N-1;i>0;i--){
        if(H[i]+1==H[i-1]){
            H[i-1]-=1;
        }else if(H[i]<H[i-1]){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}