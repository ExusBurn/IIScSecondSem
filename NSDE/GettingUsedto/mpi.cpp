#include <iostream>
#include <mpi.h>
using namespace std;

int main(int argc, char** argv) {
    // Initialize the MPI environment
    MPI_Init(&argc, &argv);
    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    // Get the rank of the process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    //Print a message starting from process 0 till process world_size-1 in order
    for (int i = 0; i < world_size; i++) {
        if (world_rank == i) {
            cout << "Hello from process " << world_rank << " out of " << world_size << " processes." << endl;
        }
        // Synchronize all processes
        MPI_Barrier(MPI_COMM_WORLD);
    }
    // Finalize the MPI environment
    MPI_Finalize();
    return 0;
}