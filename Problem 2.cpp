//
//  main.cpp
//  problem2
//
//  Created by Oishika Chaudhury on 4/4/20.
//  Copyright © 2020 Oishika Chaudhury. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string nester(string input){
    int openBrackets = 0;
    string outputString = "";
    for (int i = 0; i < input.size(); i ++){
        int value = input[i] - '0';
        
        if (openBrackets > value){
            for (int i = 0; i < openBrackets - value; i ++){
                outputString += ")";
            }
            outputString += input[i];
            openBrackets -= (openBrackets - value);
        }
        else if (openBrackets == value){
            outputString += input[i];
        }
        else {
            for (int i = 0; i < value - openBrackets; i ++){
                outputString += "(";
            }
            outputString += input[i];
            openBrackets += (value-openBrackets);
        }
    }
    for (int i = 0; i < openBrackets; i ++){
        outputString += ")";
    }
    return outputString;
}

int main() {
    int x ;
    cin >> x;
    string y;
    vector<string> answers;
    for (int i = 0; i < x; i ++){
        cin >> y;
        answers.push_back(nester(y));
    }
    for (int i = 0; i < answers.size(); i ++){
        cout << "Case #" << i+1 << ": " << answers[i] << endl;
    }
}
