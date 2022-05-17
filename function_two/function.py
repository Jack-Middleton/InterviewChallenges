from scipy.interpolate import interp1d

# Linear interpolation using Pythons scipy module

X = [1,2,3,4,5] # random x values
Y = [11,2.2,3.5,-88,1] # random y values
 
# test value
interpolate_x = 2.5
 
# Finding the interpolation
y_interp = interp1d(X, Y)
# defaults to linear, keyword arguments for above can be kind, copy, axis, bounds error
# kind - linear, quadratic, cubic, previous etc.
# copy - holds boolean values if True, the class makes internal copies of X and Y
# axis - specifies the axis of y along which we interpolate 
# bounds error - holds boolean values if true, ValueError is raised if interpolation is attempted on a value outside of range x
print(f"Value of Y at x = {interpolate_x} is",
      y_interp(interpolate_x))