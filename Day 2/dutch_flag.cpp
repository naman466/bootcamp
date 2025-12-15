#include <iostream>
#include <vector>
using namespace std;

void dutchFlag(vector<int>& arr) {
    int low = 0, mid = 0, high = arr.size() - 1;

    while (mid <= high) {
        switch (arr[mid]) {
            case 0:
                swap(arr[low], arr[mid]);
                low++;
                mid++;
                break;

            case 1:
                mid++;
                break;

            case 2:
                swap(arr[mid], arr[high]);
                high--;
                break;
        }
    }
}

int main() {
    vector<int> arr = {2, 0, 2, 1, 1, 0};

    dutchFlag(arr);

    cout << "Sorted: ";
    for (int x : arr) cout << x << " ";

    return 0;
}
