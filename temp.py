from sympy import Symbol, solve, ln
x = Symbol('x')
solve(2*((225+x)*ln(1+x/225)+(75-x)*ln(1-x/75)+(75-x)*ln(1-x/75)+(25+x)*ln(1+x/25))-0.99, x)