//
//  main.cpp
//  Competitive programming
//

#include <iostream>
#include <vector>
#include <math.h>
#include <string.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O2,unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,mmx,avx,avx2")
#define FASTIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define PRECISION std::cout << std::fixed << std::setprecision(20);

int main() {
    FASTIO;
    //PRECISION;
    vector<vector<int>> positionsA;
    vector<vector<int>> positionsB;
    int n;
    cin >> n;
    int a,b;
    for (int i = 0; i < n; i ++){
        cin >> a >> b;
        vector<int> coords;
        coords.push_back(a); coords.push_back(b);
        positionsA.push_back(coords);
        coords.clear();
    }
    cin >> n;
    for (int i = 0; i < n; i ++){
        cin >> a >> b;
        vector<int> coords;
        coords.push_back(a); coords.push_back(b);
        positionsB.push_back(coords);
        coords.clear();
    }
    
}
