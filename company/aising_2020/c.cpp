#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i=1;i<N+1;i++){
        int sum=0;
        int range_x = i-5 >0 ? int(pow((i-5),0.5))+1 : 0;
        for (int x=1;x<range_x;x++){
            int range_y = i-x*x-x-3 >0 ? int(pow((i-x*x-x-3),0.5))+1 : 0;
            for (int y=1;y<range_y;y++) {
                int range_z = i-x*x-y*y-x*y-x-y > 0 ? int(pow(i-x*x-y*y-x-y, 0.5))+1: 0;
                for (int z=1;z<range_z;z++) {
                    if (x*x + y*y + z*z + x*y + y*z + z*x == i){
                        sum++;
                    }
                }
            }
        }
        cout << sum << endl;
    }

}
