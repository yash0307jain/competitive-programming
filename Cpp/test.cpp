#include<bits/stdc++.h>
using namespace std;

int recursive_func(int n, int k, int arr[], int ind) {
    while(true) {
        int count_one = 0;
        for(int i = 0; i < n; i++)
            if(arr[i] == 1)
                count_one++;

        if(count_one == 1)
            break;

        int pos_count = 0;
        while(true) {
            if(ind == n)
                ind = 0;

            if(arr[ind] == 1) {
                pos_count++;
            }

            if(pos_count == k) {
                arr[ind] = 0;
                break;
            }

            ind++;
        }
    }

    int count_one = 0;
    int index = 0;
    for(int i = 0; i < n; i++) {
        if(arr[i] == 1) {
            count_one++;
            index = i;
        }
    }

    if(count_one != 1 && count_one != 0)
        return recursive_func(n, k, arr, ind);
    else
        return index + 1;
}

int safe_Position(int n, int k) {
    int arr[n];

    for(int i = 0; i < n; i++) {
        arr[i] = 1;
    }

    return recursive_func(n, k, arr, 0);
} 

int main() {
    int n, k;
    cin>>n>>k;

    cout<<safe_Position(n, k)<<endl;
    return 0;
}