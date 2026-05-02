#Obtain Smallest Step Size = 0.015625 Text file values for the 3 cases:
# /home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_backward_stepsize_0.015625.txt
# /home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_forward_stepsize_0.015625.txt
# /home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/rk4_stepsize_0.015625.txt
import numpy as np
import matplotlib.pyplot as plt
import cmath

#Change these directories as and when needed:
data_fwd = np.loadtxt('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_forward_stepsize_0.015625.txt')
data_bwd = np.loadtxt('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_backward_stepsize_0.015625.txt')
data_rk4 = np.loadtxt('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/rk4_stepsize_0.015625.txt')


# obtain 3 arrays for y_fwd, step size is just linspace from 0 to 2, 0.015625 as increment
y_fwd = data_fwd
y_bwd = data_bwd
y_rk4 = data_rk4
#Obtain array with step size of 0.015625 for exact solution:
t = np.arange(0, 2.0001, 0.015625)

#Actual Analytical solution:
def exponential(t):
    return cmath.exp(t**2-t**4/4)

#Compare solution with each method: Reference Exact Solution on each of the 3 plots:
#Plot all 3 subfigures in one figure side by side:
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
#Euler Forward Plot:
axs[0].plot(t, [exponential(ti).real for ti in t], label='Exact Solution', color='black', linestyle='--')
axs[0].plot(t, y_fwd, label='Euler Forward', color='blue')
axs[0].set_title('Euler Forward Method vs Exact Solution')
axs[0].set_xlabel('t')
axs[0].set_ylabel('y(t)')
axs[0].legend()
axs[0].grid()
#Euler Backward Plot:
axs[1].plot(t, [exponential(ti).real for ti in t], label='Exact Solution', color='black', linestyle='--')
axs[1].plot(t, y_bwd, label='Euler Backward', color='orange')
axs[1].set_title('Euler Backward Method vs Exact Solution')
axs[1].set_xlabel('t')
axs[1].set_ylabel('y(t)')
axs[1].legend()
axs[1].grid()
#RK4 Plot:
axs[2].plot(t, [exponential(ti).real for ti in t], label='Exact Solution', color='black', linestyle='--')
axs[2].plot(t, y_rk4, label='RK4', color='green')
axs[2].set_title('RK4 Method vs Exact Solution')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')    
axs[2].legend()
axs[2].grid()
#Please change the directory as and when needed:
plt.savefig('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/methods_comparison_plot.png')

#Alright, now I need to do the next part of b:
#Now, Plot Solution for ALL Step Sizes from each method along with analytical solution:
step_sizes = [0.250000, 0.125000, 0.062500, 0.031250, 0.015625]
methods = {
    'Euler Forward': ('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_forward_stepsize_{}.txt', 'blue'),
    'Euler Backward': ('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/euler_backward_stepsize_{}.txt', 'orange'),
    'RK4': ('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/rk4_stepsize_{}.txt', 'green')
}

fig, axs = plt.subplots(1, 3, figsize=(18, 5))

for ax, (method_name, (file_template, _)) in zip(axs, methods.items()):
    # Analytical solution
    ax.plot(t, [exponential(ti).real for ti in t],
            label='Exact Solution', color='black', linestyle='--')

    # All step sizes for this method
    for step_size in step_sizes:
        fname = file_template.format(f"{step_size:.6f}")
        data = np.loadtxt(fname)

        num_steps = int(2 / step_size) + 1
        t_steps = np.linspace(0, 2, num_steps)

        ax.plot(t_steps, data, label=f'h = {step_size}', alpha=0.7)

    ax.set_title(method_name)
    ax.set_xlabel('t')
    ax.set_ylabel('y(t)')
    ax.grid()
    ax.legend()

plt.tight_layout()
plt.savefig('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/all_methods_all_stepsizes.png')
plt.close()
# ===== End of Part (b) =====

#Part c now:

#Function to compute maximum absolute error:
#We have y, we have analytic solution, and we have step size:
#Increment with stepsize from t = 0 to 2
#Keep track of 2 things: The max error and the absolute sum of errors
#At the end, Print Max Error and Absolute Sum corresponding to each scheme and step size

errors = {
    'Euler Forward': {'h': [], 'max': [], 'avg': []},
    'Euler Backward': {'h': [], 'max': [], 'avg': []},
    'RK4': {'h': [], 'max': [], 'avg': []}
}


def compute_errors(numerical_solution, step_size):
    num_steps = int(2 / step_size) + 1
    t_steps = np.linspace(0, 2, num_steps)
    
    max_error = 0
    abs_sum_error = 0
    
    for i in range(num_steps):
        t_val = t_steps[i]
        exact_val = exponential(t_val).real
        error = abs(numerical_solution[i] - exact_val)
        
        if error > max_error:
            max_error = error
        abs_sum_error += error
    
    return max_error, abs_sum_error
#Now, Compute and Print errors for each method and step size:
for method_name, (file_template, _) in methods.items():
    for step_size in step_sizes:
        fname = file_template.format(f"{step_size:.6f}")
        data = np.loadtxt(fname)

        max_err, abs_sum_err = compute_errors(data, step_size)
        avg_err = abs_sum_err / len(data)

        errors[method_name]['h'].append(step_size)
        errors[method_name]['max'].append(max_err)
        errors[method_name]['avg'].append(avg_err)

# ===== Part (c): Order of accuracy =====

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# ---- Left: Maximum error ----
for method_name in errors:
    axs[0].loglog(
        errors[method_name]['h'],
        errors[method_name]['max'],
        marker='o',
        label=method_name
    )

# ---- Reference slope lines (MAX error) ----
h_ref = np.array(step_sizes)

# slope = 1 (Euler)
h0 = errors['Euler Forward']['h'][-1]
E0 = errors['Euler Forward']['max'][-1]
axs[0].loglog(
    h_ref,
    E0 * (h_ref / h0),
    'k--',
    linewidth=1.5,
    label='Slope 1'
)

# slope = 4 (RK4) — shifted to align with RK4 curve
idx = 1  # try 0, 1, or 2 if you want to fine-tune
h0 = errors['RK4']['h'][idx]
E0 = errors['RK4']['max'][idx]

axs[0].loglog(
    h_ref,
    E0 * (h_ref / h0)**4,
    'k:',
    linewidth=2.2,
    label='Slope 4'
)


axs[0].set_xlabel('log(h)')
axs[0].set_ylabel('log(Max Error)')
axs[0].set_title('Maximum Error vs Step Size')
axs[0].grid(True, which='both')
axs[0].legend()

# ---- Right: Average error ----
for method_name in errors:
    axs[1].loglog(
        errors[method_name]['h'],
        errors[method_name]['avg'],
        marker='o',
        label=method_name
    )

# ---- Reference slope lines (AVG error) ----

# slope = 1 (Euler)
h0 = errors['Euler Forward']['h'][-1]
E0 = errors['Euler Forward']['avg'][-1]
axs[1].loglog(
    h_ref,
    E0 * (h_ref / h0),
    'k--',
    linewidth=1.5,
    label='Slope 1'
)

# slope = 4 (RK4) — shifted to align with RK4 curve
idx = 1
h0 = errors['RK4']['h'][idx]
E0 = errors['RK4']['avg'][idx]

axs[1].loglog(
    h_ref,
    E0 * (h_ref / h0)**4,
    'k:',
    linewidth=2.2,
    label='Slope 4'
)



axs[1].set_xlabel('log(h)')
axs[1].set_ylabel('log(Average Error)')
axs[1].set_title('Average Error vs Step Size')
axs[1].grid(True, which='both')
axs[1].legend()

plt.tight_layout()
plt.savefig('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/error_convergence.png')
plt.close()
# ===== End of Part (c) =====