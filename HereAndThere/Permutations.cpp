#include <vector>
#include <iostream>
using namespace std;

void allPermutations(string& word, int low, int high){
    if (low == high){
        cout << word << endl;;
    }
    for (int i = low; i <= high; i++){
        //1. Swap the character in the i-th position with the first character
        swap(word[low], word[i]);
        //2. Print that character and recurse on the rest of the string
        allPermutations(word, low+1, high);
        //3.Unswap the character
        swap(word[low], word[i]);

    }
    
}

int main(){
    string word = "boat";
    allPermutations(word, 0, 3);
    return 0;
}
