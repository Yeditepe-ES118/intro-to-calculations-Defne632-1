import math 

def find_period(L0, L1):
    g = 9.81 # (m/s**2)
    
    for L in range(L0, L1 + 1):
        T = 2 * math.pi * math.sqrt(L / g)
        print(f"when L = {L: .1f}  m, T = {T: .1f} s")
    
    T0 = 2 * math.pi * math.sqrt(L0 / g)
    T1 = 2 * math.pi * math.sqrt(L1 / g)
    return T0, T1



        
    
