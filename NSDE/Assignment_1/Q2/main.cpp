#include <iostream>
#include <vector>
#include <fstream>
#include "arange.h"
#include "Euler_fwd_bwd_rk4.h"
using namespace std;

int main() {
    //Initial Condition:
    vector<double> y0 = {1.0}; // y(0) = 1

    //Define time parameters:
    int t_start = 0;
    int t_end = 2;
    vector<double> step_sizes = {0.25, 0.125, 0.0625, 0.03125, 0.015625};
    //Using loop, obtain 5*3=15 results using all schemes and step sizes, store all 15 vectors as a 2D vector:
    vector<vector<double>> all_results;
    for (double step_size : step_sizes) {
        vector<double> arange_vector = arange(t_start, t_end, step_size);
        //Euler Forward:
        vector<double> euler_fwd_result = euler_forward(y0, arange_vector);
        all_results.push_back(euler_fwd_result);
        //Euler Backward:
        vector<double> euler_bwd_result = euler_backward(y0, arange_vector);
        all_results.push_back(euler_bwd_result);
        //RK4:
        vector<double> rk4_result = rk4(y0, arange_vector);
        all_results.push_back(rk4_result);
    }

    //Output to .txt file, all 15 vectors, 15 txt files, one for each scheme and step size, naming convention: "method_stepsize.txt"
    vector<string> method_names = {"euler_forward", "euler_backward", "rk4"};
    int file_index = 0;
    for (double step_size : step_sizes) {
        for (const string& method_name : method_names) {
            string filename = method_name + "_stepsize_" + to_string(step_size) + ".txt";
            ofstream outfile(filename);
            if (outfile.is_open()) {
                const vector<double>& result_vector = all_results[file_index];
                for (double val : result_vector) {
                    outfile << val << endl;
                }
                outfile.close();
            } else {
                cerr << "Error opening file: " << filename << endl;
            }
            file_index++;
        }
    }

    return 0;
}
