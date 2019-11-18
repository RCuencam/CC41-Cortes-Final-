import heapq as hq
import matplotlib.pyplot as plt
import numpy as np

##b_s bins size
## size of box
##count of box
def bins(b_s, sizes, counts):
    av = zip(sizes, counts)
    av=list(av) ##convert zip to list
    av.sort(reverse=True)
    seen = set([])
    c = [(0, av, [])]
    while 0 < len(c):
        (n, av, bins) = hq.heappop(c)
        for (bin, left) in packing_left(b_s, av):
            new_bins = bins + [bin] ##nuevo contenedor
            if 0 == len(left):
                return new_bins
            elif left not in seen:
                hq.heappush(c, (n+1, left, new_bins))
                seen.add(left)

def packing_left(bin_size, av, top=True):
    if 0 == len(av):
        yield ((), ())
    else:
        (size, count) = av[0]
        av = av[1:]
        for (bin, left, used) in p_s(bin_size, av):
            can_use = (bin_size - used) / size
            if count <= can_use:
                yield(((size, count),) + bin, left)
            elif 0 < can_use:
                yield(((size, can_use),) + bin,
                      ((size, count - can_use),) + left)
            else:
                yield(bin, ((size, count),) + left)

def p_s(bin_size, av):
    if 0 == len(av):
        yield ((), (), 0)
    else:
        (size, count) = av[0]
        av = av[1:]
        for (bin, left, used) in p_s(bin_size, av):
            for i in range(1 + min(count, (bin_size - used) // size)):
                if count == i:
                    yield(((size, count),) + bin, left, used + size * count)
                elif 0 < i:
                    yield(((size, i),) + bin,
                          ((size, count - i),) + left,
                          used + size * i)
                else:
                    yield(bin, ((size, count),) + left, used)


def sizes(arr,q,size_bin):
    sizes_boxs=[]
    for h,w,d in arr:
        sizes_boxs.append(h*w*d)
    
    box_result = bins(size_bin,sizes_boxs,q)
    print("First container", box_result[0])
    print("Next container" , box_result[1])

arr=[[1,1,5]
    ,[1,1,3]
    ,[1,1,2]]

q=[20,30,40] 

sizes(arr,q,25)    


