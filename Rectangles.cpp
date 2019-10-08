//
//  main.cpp
//  ProgTeam
//
//  Created by Oishika Chaudhury on 10/8/19.
//  Copyright © 2019 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int numberOfInputs;
    cin>>numberOfInputs;
    int x,y;
    bool isPossible=true;
    vector<int> vectorOfInts;
    for (int i=0; i<numberOfInputs; ++i){
        if (!(i==0)){
            cin>>x>>y;
            if (x < y) {
                swap(x,y);
            }
            // x >= y
            if (x<=vectorOfInts[i-1]) {
                vectorOfInts.push_back(x);
            }
            else if (y<=vectorOfInts[i-1]) {
                vectorOfInts.push_back(y);
            }
            
            else {
                isPossible=false;
                break;
            }
        }
        else{
           cin>>x>>y;
            if (x>=y){
                vectorOfInts.push_back(x);
            }
            else {
                vectorOfInts.push_back(y);
            }
        }
    }
    if (isPossible){
        cout<<"YES"<<endl;
    }
    else {
        cout<<"NO"<<endl;
    }
}
