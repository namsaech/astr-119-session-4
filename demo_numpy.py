import numpy as np

x = 1.0 
y = 2.0

#exp and logs
print(np.exp(x))
print(np.log(x))
print(np.log10(x))
print(np.log2(x))
#min/mx/misc
print(np.fabs(x)) #abs value as a float
print(np.min(x))
print(np.fmax(x))

#populate arrays
n = 100 #define an int
z = np.arrange(n,dtype=float) #get an array
z = *= 2.0*np.pi/float(n-1)
sin_z = np.sin(z) #get an array sinz

#interpolation
print(np.interp(0.75, z sin_z))
print(np.sin(0.75))
