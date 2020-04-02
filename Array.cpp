//
//  main.cpp
//  Array
//
//  Created by Oishika Chaudhury on 4/2/20.
//  Copyright © 2020 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;


int main() {
    vector<int> zero;
    vector<int> positive;
    vector<int> negative;
    int n, i = 0, k;
    cin >> n;
    while (i < n){
        cin >> k;
        if (k < 0 && negative.size()==0) negative.push_back(k);
        else if (k == 0) zero.push_back(0);
        else positive.push_back(k);
        i++;
    }
    cout << "1 " << negative[0] << endl;
    cout << positive.size() << " ";
    for (int i = 0; i < positive.size(); i ++) cout << positive[i] << " ";
    cout << endl;
    cout << "1 0" << endl;
    
}
