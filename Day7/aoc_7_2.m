clear
close all
clc

format bank
tic
file = fopen("./input.txt", "r");
crabs = fscanf(file, "%d,");
max_crab = max(crabs);
min_crab = min(crabs);
f = @(x) sum(abs(crabs-x).*(abs(crabs-x)+1)./2);
[x, fval] = particleswarm(f,1,min_crab, max_crab, "swarmsize", 25);
[round(x) f(round(x))]
fclose('all');
toc