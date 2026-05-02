#include <vector>

using namespace std;
//Define Forward Function:
vector<double> euler_forward(const vector<double>& y0, vector<double>& linspace) {
    //We currently know y0[0] and its current timestep is linspace[0]:
    vector<double> y = {y0[0]};
    double t = linspace[0];

    for (int step = 0; step < linspace.size()-1; ++step) {
        //yn+1 = yn(1+delT(2t-t^3)):
        double t = linspace[step];
        double dydt = (2*t - t*t*t) * y.back();
        y.push_back(y.back() + (linspace[step+1] - linspace[step]) * dydt);
    }
    //Return final vector:
    return y;
}


//Define Backward Function: With yn+1 = yn/(1-delT(2t-t^3))
vector<double> euler_backward(const vector<double>& y0, vector<double>& linspace) {
    //We currently know y0[0] and its current timestep is linspace[0]:
    vector<double> y = {y0[0]};
    double t = linspace[0];

    for (int step = 0; step < linspace.size()-1; ++step) {
        //yn+1 = yn/(1-delT(2t-t^3)):
        double t = linspace[step+1];
        double dydt = (2*t - t*t*t);
        y.push_back(y.back() / (1 - (linspace[step+1] - linspace[step]) * dydt));
    }
    //Return final vector:
    return y;
}

vector<double> rk4(const vector<double>& y0, vector<double>& linspace) {
    //We currently know y0[0] and its current timestep is linspace[0]:
    vector<double> y = {y0[0]};
    double t = linspace[0];

    for (int step = 0; step < linspace.size()-1; ++step) {
        double h = linspace[step+1] - linspace[step];
        double t_n = linspace[step];
        double y_n = y.back();

        //Calculate k1, k2, k3, k4:
        double k1 = (2*t_n - t_n*t_n*t_n) * y_n;
        double k2 = (2*(t_n + h/2) - (t_n + h/2)*(t_n + h/2)*(t_n + h/2)) * (y_n + h/2 * k1);
        double k3 = (2*(t_n + h/2) - (t_n + h/2)*(t_n + h/2)*(t_n + h/2)) * (y_n + h/2 * k2);
        double k4 = (2*(t_n + h) - (t_n + h)*(t_n + h)*(t_n + h)) * (y_n + h * k3);

        //Update y:
        y.push_back(y_n + (h/6) * (k1 + 2*k2 + 2*k3 + k4));
    }
    //Return final vector:
    return y;
}