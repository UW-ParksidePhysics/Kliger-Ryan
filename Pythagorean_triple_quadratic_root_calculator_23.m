fileID = fopen('Pythagorean_triples.txt', 'r');
PT = fscanf(fileID, '%d %d %d\n', [3, Inf]);
fclose(fileID);
filename = fopen('pythagorean_triple_quadratic_roots.txt', 'wt');

for triple = PT
    a = triple(1);
    b = triple(2);
    c = triple(3);
    [x, x2] = quadratic_roots(a, b, c);
    disp([num2str(triple.'), ' ',num2str(x), ' ', num2str(x2)])
    fprintf(filename, '%i %i %i %g%+gi %g%+gi\n' , a, b, c, real(x),imag(x), real(x2), imag(x2));
end
fclose(filename);