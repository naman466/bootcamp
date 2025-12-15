#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Group Gi contains horses sorted fastest -> slowest
// winnersOrder is indices of groups sorted by the race of group winners

vector<string> findFinalCandidates(
    const vector<vector<string>>& groups,
    const vector<int>& winnersOrder
) {
    vector<string> candidates;
    int G = groups.size();      
    int K = groups[0].size();   

    for (int rank = 0; rank < G; rank++) {
        int groupIndex = winnersOrder[rank];

        for (int j = 0; j < K; j++) {
            if (rank + j <= 2) {
                candidates.push_back(groups[groupIndex][j]);
            }
        }
    }
    return candidates;
}

int main() {
    vector<vector<string>> groups = {
        {"A1", "A2", "A3", "A4", "A5"},
        {"B1", "B2", "B3", "B4", "B5"},
        {"C1", "C2", "C3", "C4", "C5"},
        {"D1", "D2", "D3", "D4", "D5"},
        {"E1", "E2", "E3", "E4", "E5"}
    };

    vector<int> winnersOrder = {0, 1, 2, 3, 4};

    vector<string> candidates = findFinalCandidates(groups, winnersOrder);

    cout << "Final race candidates (can still be in top 3):\n";
    for (auto& h : candidates)
        cout << h << "\n";

    return 0;
}
