//
//  main.cpp
//  ProgTeam2
//
//  Created by Oishika Chaudhury on 10/8/19.
//  Copyright © 2019 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int desiredOriginal,desiredCopies;
    cin>>desiredCopies>>desiredOriginal;
    int copiesNow= (desiredOriginal-1);
    if ((desiredCopies-copiesNow)%2==0){
        cout<<"YES"<<endl;
    }
    else {
        cout<<"NO"<<endl;
    }
}
