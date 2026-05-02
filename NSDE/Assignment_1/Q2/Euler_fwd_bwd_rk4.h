#ifndef EULER_FWD_BWD_RK4_H
#define EULER_FWD_BWD_RK4_H

#include <vector>

std::vector<double> euler_forward(const std::vector<double>&,
                                  std::vector<double>&);

std::vector<double> euler_backward(const std::vector<double>&,
                                   std::vector<double>&);

std::vector<double> rk4(const std::vector<double>&,
                        std::vector<double>&);

#endif
