//Google CodeJam - Oishika

#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main() {
    int a(0),b(0),c(0);
    cin >> a;
    vector<vector<long long>> retValue;
    for (int i = 0; i < a; i++){
        cin >> b;
        vector<vector<int>> matrix;
        for (int j = 0; j < b; j ++){
            vector<int> rows;
            for (int k = 0; k < b; k ++){
                cin >> c;
                rows.push_back(c);
            }
            matrix.push_back(rows);
        }
        
      
        int rowCount(0), colCount(0); long long trace(0);
        for (int m = 0; m < matrix.size() ; m ++){
            set<int> rowCheck;
            for (int j = 0; j < matrix[m].size(); j ++){
                if (rowCheck.find(matrix[m][j]) == rowCheck.end()){ rowCheck.insert(matrix[m][j]); }
                else{ rowCount += 1; break; }
            }
        }
        

        for (int m = 0; m < matrix.size() ; m ++){
            set<int> colCheck;
            for (int j = 0; j < matrix[m].size(); j ++){
                if (colCheck.find(matrix[j][m]) == colCheck.end()){ colCheck.insert(matrix[j][m]); }
                else { colCount += 1; break; }
            }
        }
        

        for (int q = 0; q < matrix.size(); q ++ ) {
            trace +=  (long long)(matrix[q][q]);
        }
        retValue.push_back({rowCount, colCount, trace});
    }

    for (int i = 0; i < retValue.size(); i ++){
        cout << "Case #" << i+1 << ": " << retValue[i][2] << " " << retValue[i][0] << " " << retValue[i][1] << endl;
    }
    
}
