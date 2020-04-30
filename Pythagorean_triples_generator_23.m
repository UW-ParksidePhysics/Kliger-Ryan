c = 1
n = 1000
filename = fopen('Pythagorean_triples.txt', 'wt');
for a = 1:n-2
    for b = a:n-1
        c = sqrt(a^2 + b^2);
        if c == floor(c) & c < n
            fprintf(filename, '%i %i %i\n' , a, b, c);
        end 
    end
end
fclose(filename);