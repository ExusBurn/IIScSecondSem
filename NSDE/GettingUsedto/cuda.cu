#include <iostream>
#include <cuda_runtime.h>
using namespace std;

//Simple code to print hello from GPU, only use 2 threads
__global__ void helloFromGPU() {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    if (idx < 2) {
        printf("Hello from GPU thread %d out of 2 threads.\n", idx);
    }
}
int main() {
    // Launch kernel with 1 block of 2 threads
    helloFromGPU<<<1, 2>>>();
    // Wait for GPU to finish before accessing on host
    cudaDeviceSynchronize();
    return 0;
}