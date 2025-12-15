#include <iostream>
using namespace std;

const int MEMORY_SIZE = 1000;
const int MAX_ARRAY_SIZE = 200;

struct Block {
    int start;   // starting index in the memory pool
    int size;    // size of this block
    bool free;   // free or allocated
};

class MemoryManager {
private:
    int memory[MEMORY_SIZE];

    Block blocks[100]; // at most 100 segments
    int blockCount;

public:
    MemoryManager() {
        blockCount = 1;

        // Initially: one big free block of size 1000
        blocks[0] = {0, MEMORY_SIZE, true};
    }

    // Allocate array with size <= 200
    int allocate(int size) {
        if (size > MAX_ARRAY_SIZE) {
            cout << "Error: Cannot allocate more than 200.\n";
            return -1;
        }

        for (int i = 0; i < blockCount; i++) {
            if (blocks[i].free && blocks[i].size >= size) {

                int startIndex = blocks[i].start;

                // If exact fit → use the whole block
                if (blocks[i].size == size) {
                    blocks[i].free = false;
                }
                else {
                    // Split block
                    Block newBlock = {
                        blocks[i].start + size,
                        blocks[i].size - size,
                        true
                    };

                    blocks[i].size = size;
                    blocks[i].free = false;

                    // Insert new free block
                    blocks[blockCount++] = newBlock;
                }

                return startIndex;
            }
        }

        cout << "Error: Not enough memory!\n";
        return -1;
    }

    // Free a previously allocated array
    void freeArray(int startIndex) {
        for (int i = 0; i < blockCount; i++) {
            if (blocks[i].start == startIndex) {
                if (blocks[i].free) {
                    cout << "Error: Block already free!\n";
                    return;
                }

                blocks[i].free = true;
                cout << "Freed array at index " << startIndex << "\n";
                return;
            }
        }

        cout << "Error: Invalid free request.\n";
    }

    // Write value to an array
    void write(int start, int offset, int value) {
        if (start + offset >= MEMORY_SIZE) {
            cout << "Write error: out of memory range.\n";
            return;
        }
        memory[start + offset] = value;
    }

    // Read value from an array
    int read(int start, int offset) {
        if (start + offset >= MEMORY_SIZE) {
            cout << "Read error: out of memory range.\n";
            return -1;
        }
        return memory[start + offset];
    }
};

int main() {
    MemoryManager mm;

    int a = mm.allocate(50);      // ok
    int b = mm.allocate(120);     // ok
    int c = mm.allocate(200);     // ok (max allowed)
    int d = mm.allocate(300);     // Error

    // Write to array "a"
    mm.write(a, 0, 10);
    mm.write(a, 1, 99);

    cout << "a[0] = " << mm.read(a, 0) << "\n";
    cout << "a[1] = " << mm.read(a, 1) << "\n\n";

    // Free an array
    mm.freeArray(b);

    // Allocate again (should reuse space)
    int e = mm.allocate(70);
    cout << "New array starts at: " << e << "\n";

    return 0;
}
