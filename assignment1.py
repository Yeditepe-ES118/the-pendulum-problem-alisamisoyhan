import numpy as np
def find_period(L0,L1):
    g=9.81 # m/s**2
    T0 = 2* np.pi * np.sqrt(L0 /g)
    T1 = 2* np.pi * np.sqrt(L1 /g)
    for L in range(L0, L1 + 1):
        T_current = 2* np.pi * np.sqrt(L/ g)
        print (f"when L= {L:.1f} m, T={T_current:.1f} s")
    return T0, T1  
myresult=find_period(2,10)  
        

    