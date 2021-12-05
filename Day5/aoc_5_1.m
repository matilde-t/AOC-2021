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
        if data(2)<data(4)
            vents(data(1),data(2):data(4)) = vents(data(1),data(2):data(4)) + 1;
        else
            vents(data(1),data(4):data(2)) = vents(data(1),data(4):data(2)) + 1;
        end
    elseif data(2) == data(4)
        if data(1)<data(3)
            vents(data(1):data(3),data(2)) = vents(data(1):data(3),data(2)) + 1;
        else
            vents(data(3):data(1),data(2)) = vents(data(3):data(1),data(2)) + 1;
        end
    end
end
sum(sum(vents>1))
fclose('all');