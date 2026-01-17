#include <iostream>
using namespace std;
//header file for openmp:
#include <omp.h>
#include "add.h"

//Do a simple Hello World:
int main() {
    cout << "Hello, World!" << endl;
    //create an array of size 4 assigning each element to its index value:
    int arr[4];
    for (int i = 0; i < 4; i++) {
        arr[i] = i;
    }

    int sum = 0;

    //spawn 4 threads: arr has to be shared among all threads:
    omp_lock_t sum_lock;
    omp_init_lock(&sum_lock);
    #pragma omp parallel num_threads(4) shared(arr)
    {
        //get thread id:
        int tid = omp_get_thread_num();
        //add values of arr[i] onto another variable using atomic operation:
        omp_set_lock(&sum_lock);
        sum += arr[tid];
        omp_unset_lock(&sum_lock);
    }
    omp_destroy_lock(&sum_lock);
    cout << "Sum is " << sum << endl;
    cout<< "Using add function: " << add(5, 10) << endl;
    return 0;
}