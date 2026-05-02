#Importing Plotting and Math Libraries:
import matplotlib.pyplot as plt
import cmath

#Define an exponential function taking parameter t
def exponential(t):
    return cmath.exp(t**2-t**4/4)

#Plot Exponential function from t in 0 to 2, save as png, simple plot:
t_values = [i*0.01 for i in range(201)]
exp_values = [exponential(t) for t in t_values]
plt.plot(t_values, [val.real for val in exp_values], label='Real Part')
plt.title('Exponential Function: exp(t^2 - t^4/4)')
plt.xlabel('t')
plt.ylabel('exp(t^2 - t^4/4)')
plt.legend()
plt.grid()


#Please change the directory as and when needed:
plt.savefig('/home/aadithya-iyer/Github/IIScSecondSem/NSDE/Assignment_1/Q2/exponential_plot.png')