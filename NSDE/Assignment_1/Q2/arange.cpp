#include <vector>
using namespace std;
vector<double> arange(int start, int end, double step_size) {
    vector<double> linspace_vector;
    for (double val = start; val <= end; val += step_size) {
        linspace_vector.push_back(val);
    }
    return linspace_vector;
}