#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

class Semaphore {
private:
  std::atomic<int> count;

public:
  Semaphore(int initial) : count(initial) {}

  void wait() {
    while (true) {
      int expected = count.load();
      if (expected > 0) {
        if (count.compare_exchange_weak(expected, expected - 1)) {
          break;
        }
      }

      std::this_thread::yield(); // yield control while waiting
    }
  }

  void signal() { count.fetch_add(1); }
};

const int SIZE = 5;

struct Buffer {
  int data[SIZE];
  int head = 0; // producer puts
  int tail = 0; // consumer takes

  Semaphore empty_slots{SIZE};
  Semaphore full_slots{0};

  std::atomic_flag lock = ATOMIC_FLAG_INIT;

  void produce(int val) {
    empty_slots.wait();

    while (lock.test_and_set(std::memory_order_acquire))
      ;

    data[head] = val;
    head = (head + 1) % SIZE;

    lock.clear(std::memory_order_release);

    full_slots.signal();
  }

  int consume() {
    full_slots.wait(); // wait for data

    while (lock.test_and_set(std::memory_order_acquire))
      ;

    int val = data[tail];
    tail = (tail + 1) % SIZE;

    lock.clear(std::memory_order_release)

        empty_slots.signal();

    return val;
  }
};
