% Quadratic Example-Ryan Kliger
a = input('quadratic root 1?')
b = input('quadratic root 2?')
c = input('quadratic root 3?')
discr = b*b - 4*a*c;
[x, x2] = quadratic_roots(a, b, c);


if discr < 0
    disp([num2str(x) '' , num2str(x2) '' , 'Discriminant is negative, roots are imaginary'])
elseif discr == 0
    disp([num2str(x) '' , num2str(x2) '' , 'Discriminant is 0, roots are repeated'])
else 
    disp([num2str(x) '' , num2str(x2) '' , 'roots are real'])
end    