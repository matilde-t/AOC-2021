clear
close all
clc

format bank
tic
file = fopen("./input.txt", "r");
crabs = fscanf(file, "%d,");
f = @(x) sum(abs(crabs-x));
x = particleswarm(f, 1, min(crabs), max(crabs), "swarmsize", 25);
f(round(x))
fclose('all');
toc