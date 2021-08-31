#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int cuttingRodNonDP(int length, const vector<int>& prices){
    if (length == 0){
        return 0;
    }
    //Generating all possible combinations
    int profit = 0;
    for (int i = 0; i < length; i ++){
        profit = max(profit, prices[i] + cuttingRodNonDP(length-i-1, prices));
    }
    return profit;
}

int cuttingRodDP(int length, const vector<int>& prices){
    vector<int> maxProfits(length+1,0);
    for (int i = 1; i <= length; i ++){
        int maxValue = 0;
        for (int j = 0; j  < i; j++){
            maxValue = max(maxValue, prices[j] + maxProfits[i-j-1]);
        }
        maxProfits[i] = maxValue;
    }
    return maxProfits[length];
}


int main(int argc, const char * argv[]) {
    int length = 8;
    vector<int> prices = {1,5,8,9,10,17,17,20};
    int maxValue = cuttingRodDP(length, prices);
    cout << maxValue << endl;
}
