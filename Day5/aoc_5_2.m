clear
close all
clc

file = fopen("./prova.txt", "r");
vents = sparse(1500,800);
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
    elseif (abs(data(1)-data(3)) == abs(data(2)-data(4))) || ...
            (abs(data(1)+data(3)) == abs(data(2)+data(4)))
        if data(1)<data(3)
            x = [data(1):data(3)];
        else
            x = [data(1):-1:data(3)];
        end
        if data(2)<data(4)
            y = [data(2):data(4)];
        else
            y = [data(2):-1:data(4)];
        end
        vents(sub2ind(size(vents),x,y)) = vents(sub2ind(size(vents),x,y)) + 1;
    end
end
sum(sum(vents>1))
spy(vents')
fclose('all');