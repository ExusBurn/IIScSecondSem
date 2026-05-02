#include <mpi.h>
#include <omp.h>
#include <cuda_runtime.h>
#include <stdio.h>

//Initialize mpi on main:
int main(int argc, char** argv) {
    int vector[8] = {1,2,3,4,5,6,7,8};

    MPI_Init(&argc, &argv);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int local_vec[4];   // each rank owns 4 elements
    //Send left 4 elements to process 1:
    if (world_rank == 0) {
        // Rank 0 keeps first 4
        for (int i = 0; i < 4; i++)
            local_vec[i] = vector[i];

        // Send last 4 to rank 1
        MPI_Send(&vector[4], 4, MPI_INT, 1, 0, MPI_COMM_WORLD);
    }
    //Receive 4 elements from process 0:
    else if (world_rank == 1) {
        MPI_Recv(local_vec, 4, MPI_INT, 0, 0,
                 MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
    MPI_Finalize();
    return 0;
}