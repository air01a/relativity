from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)


z = -1 / (x**2 + y**2 + 1)

df_dx = diff(z, x)
df_dy = diff(z, y)


g11=simplify(1+df_dx**2)
g22=simplify(1+df_dy**2)
g21=g12=simplify(df_dx*df_dy)

metric = Matrix([[g11,g12],[g21,g22]])
metric_inv = metric.inv()
print(metric, metric_inv) 
