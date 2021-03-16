import numpy as np

t0 = 0 #initial time
t_end = 730 #two years after February 2020, February 2022.

h = 1 #step size 
steps = int((t_end - t0)/h + 1) # number of steps

# variables:
t = np.linspace(t0, t_end, steps) # storing t values
S = np.zeros(steps) # storing S values
I = np.zeros(steps) # storing I values
R = np.zeros(steps) # storing I values

# parameters:
b = 0.400 #infection rate 
k = 0.035 #recovery rate

def dSdt(t,S,I):
    # dS/dt
    return -b*S*I/N

def dIdt(t,S,I):
    # dI/dt
    return (b*S/N-k)*I

def dRdt(t,S,I):
    return k*I
    # dR/dt
    
# initial conditions:
S[0] = 50000000 #2019 South Korean Population as rounded up to nearest tens of millions.
                #Even though the simulation starts from 2020, the most trustworthy census data is 2019. This is a potential limitation of this simulation.
                #Statistics Korea. (2020). Statistics Korea. http://kostat.go.kr/portal/eng/pressReleases/8/7/index.board?bmode=read&bSeq=&aSeq=386088&pageNo=1&rowNum=10&navCount=10&currPg=&searchInfo=&sTarget=title&sTxt=
I[0] = 1 #Starts with one infection
R[0] = 0
N = S[0] + I[0]

for n in range(steps-1): # range(start, stop, step), This part is a calculation of Euler's method.
    S[n+1] = S[n] + h*dSdt(t[n], S[n], I[n])
    I[n+1] = I[n] + h*dIdt(t[n], S[n], I[n])
    R[n+1] = R[n] + h*dRdt(t[n], S[n], I[n])

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})
plt.rcParams["figure.figsize"] = [8,5]
plt.plot(t,S,linewidth=2,label='S(t)')
plt.plot(t,I,linewidth=2,label='I(t)')
plt.plot(t,R,linewidth=2,label='R(t)')
plt.xlabel('t (days)')
plt.ylabel('S, I, R')
plt.legend(loc='best')
plt.show()
print("Figure 1. The SIR Modeling that shows the prediction to Feb 2022 based on Feb 2020")
#the code above was provided in CS51 Session 7.2 Spring 2021 at Minerva Schools at KGI.
