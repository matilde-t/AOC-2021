clear
close all
clc

file = fopen("./input.txt", "r");
vents = sparse(1000,1000);
while 1
    data = fscanf(file, "%d,%d -> %d,%d", 4);
    if size(data) == 0
        break
    end
    data = data + 1;
    if data(1) == data(3)
        vents(data(1),min(data(2),data(4)):max(data(2),data(4))) = ...
            vents(data(1),min(data(2),data(4)):max(data(2),data(4))) + 1;
    elseif data(2) == data(4)
        vents(min(data(1),data(3)):max(data(1),data(3)),data(2)) = ...
            vents(min(data(1),data(3)):max(data(1),data(3)),data(2)) + 1;
    end
end
sum(sum(vents>1))
spy(vents)
fclose('all');