def interpolation(d, x):
	output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
	return output

print("Values needed are Y1, Y2 floating values(observed) and X1, X2 floating values observed and a value to interpolate")
y1 = float(input("Enter Y1: \n"))
y2 = float(input("Enter Y2: \n"))
x1 = float(input("Enter X2: \n"))
x2 = float(input("Enter X2: \n"))
value_to_interpolate = float(input("Enter value to interpolate: \n"))

data=[[y1, y2],[x1, x2]]

print(f"Interpolated value is: {interpolation(data, value_to_interpolate)}")
