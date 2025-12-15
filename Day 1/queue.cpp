#include <iostream>
using namespace std;

// Memory block size and chunk size
const int TOTAL_MEMORY = 1000;
const int CHUNK_SIZE = 200;
const int MAX_CHUNKS = TOTAL_MEMORY / CHUNK_SIZE;

class MemoryManager {
private:
    int memory[TOTAL_MEMORY];   // The big memory pool
    bool allocated[MAX_CHUNKS]; // Tracks which chunks are used

public:
    MemoryManager() {
        // Initially all chunks are free
        for (int i = 0; i < MAX_CHUNKS; i++) {
            allocated[i] = false;
        }
    }

    // Allocate one 200-size array (chunk)
    int allocate() {
        for (int i = 0; i < MAX_CHUNKS; i++) {
            if (!allocated[i]) {
                allocated[i] = true;

                // Return the starting index of the chunk
                return i * CHUNK_SIZE;
            }
        }

        cout << "Memory Manager: No free chunks available!\n";
        return -1; // failed
    }

    // Free a previously allocated chunk
    void freeArray(int startIndex) {
        if (startIndex < 0 || startIndex >= TOTAL_MEMORY) {
            cout << "Invalid free request.\n";
            return;
        }

        int chunkId = startIndex / CHUNK_SIZE;

        if (!allocated[chunkId]) {
            cout << "This chunk is already free!\n";
            return;
        }

        allocated[chunkId] = false;
        cout << "Chunk starting at index " << startIndex << " freed.\n";
    }

    // Read a value
    int read(int startIndex, int offset) {
        if (offset < 0 || offset >= CHUNK_SIZE) {
            cout << "Read error: offset out of range.\n";
            return -1;
        }
        return memory[startIndex + offset];
    }

    // Write a value
    void write(int startIndex, int offset, int value) {
        if (offset < 0 || offset >= CHUNK_SIZE) {
            cout << "Write error: offset out of range.\n";
            return;
        }
        memory[startIndex + offset] = value;
    }
};

int main() {
    MemoryManager mm;

    // Allocate two arrays (chunks)
    int arr1 = mm.allocate();
    int arr2 = mm.allocate();

    cout << "Array 1 starts at: " << arr1 << "\n";
    cout << "Array 2 starts at: " << arr2 << "\n\n";

    // Write values into arr1
    mm.write(arr1, 0, 10);
    mm.write(arr1, 1, 20);
    mm.write(arr1, 2, 30);

    // Read back
    cout << "arr1[0] = " << mm.read(arr1, 0) << "\n";
    cout << "arr1[1] = " << mm.read(arr1, 1) << "\n";
    cout << "arr1[2] = " << mm.read(arr1, 2) << "\n\n";

    // Free one chunk
    mm.freeArray(arr1);

    // Try allocating again
    int arr3 = mm.allocate();
    cout << "Array 3 starts at: " << arr3 << "\n";

    return 0;
}
