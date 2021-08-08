//
//  main.cpp
//  Codeforces
//
//  Created by Oishika Chaudhury on 4/2/20.
//  Copyright © 2020 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int x,y;
    cin >> x >> y;
    int h = x;
    vector<int> nums{0,0,0,0,0,0,0,0,0,0};
    bool found = false;
    while (!found && x <= y){
        while (h > 0)  { nums[h%10] += 1; h/=10; }
        for (int i = 0; i < nums.size(); i ++){
            if ( nums[i] > 1) break;
            else if (i == nums.size()-1) { cout << x << endl; return 0; }
        }
        for (int i = 0; i < nums.size(); i ++) nums[i] = 0;
        x+=1; h=x;
    }
    cout << -1 << endl;
    
}
