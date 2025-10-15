import numpy as np 

def surface_area(pi_app):
    a = 6378.137 #in km 
    c = 6356.752314245 #in km 
    e_squared = 1 - c**2/a**2
    s = 2 *pi_app* a**2 * (1 + (1 - e_squared)/np.sqrt(e_squared) * np.arctanh(np.sqrt(e_squared)))
    return s 

def compute_error(pi_app1,pi_app2):
    S_1 = surface_area(pi_app1)
    S_2 = surface_area(pi_app2)
    error = np.abs(S_1 - S_2)/S_2 * 100 #in %
    return error 

myresult = compute_error(3.14,3.1415)


