//
//  main.cpp
//  problem3
//
//  Created by Oishika Chaudhury on 4/4/20.
//  Copyright © 2020 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string timeChecker(vector<vector<int>> inputTimes){
    map<vector<int>, string> myMap;
    if (inputTimes.size() == 0) return "IMPOSSIBLE";
    
    vector<vector<int>> outPut = inputTimes;
    sort(outPut.begin(), outPut.end());
  
    int cameron = outPut[0][1];
    int jamie = 0;
    myMap.insert({outPut[0], "C"});
    for (int i = 1; i < inputTimes.size(); i ++){
        if (outPut[i][0] >= cameron){
            myMap.insert({outPut[i],"C"});
            cameron = outPut[i][1];
        }
        else if (outPut[i][0] >= jamie){
            myMap.insert({outPut[i],"J"});
            jamie = outPut[i][1];
        }
        else {
            return "IMPOSSIBLE";
        }
    }
   
    string outputString = "";
    for (int i = 0; i < inputTimes.size() ; i ++){
        outputString += myMap.find({inputTimes[i]})->second;
    }

    return outputString;
}

int main() {
    vector<string> answers;
    int c(0);
    cin >> c;
    for (int i = 0; i < c; i ++){
        int k(0);
        cin >> k;
        vector<vector<int>> inputVector;
        for (int j = 0; j < k; j++){
            int a,b;
            cin >> a >> b;
            vector<int> input{a,b};
            inputVector.push_back(input);
        }
        answers.push_back(timeChecker(inputVector));
    }
    for (int i = 0; i < answers.size() ; i ++){
        cout << "Case #" << i + 1 << ": " << answers[i] << endl;
    }
}
