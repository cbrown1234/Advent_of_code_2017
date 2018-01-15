from itertools import cycle

def get_max_in_level(n):
    return (2*n+1)**2

def get_level(x):
    n = 0 
    while x > get_max_in_level(n):
        n += 1
    return n

def get_min_in_level(n):
    return get_max_in_level(n-1)+1

def side_size(n):
    return 2*n+1

def man_dist(coord):
    a, b = coord
    return abs(a) + abs(b)

def dist_from_straight_shot(x):
    n = get_level(x)
    mini = get_min_in_level(n)
    maxi = get_max_in_level(n)
    pos_in_level = x - mini
    pos_in_sub_level = pos_in_level % (2*n)
    dist_gen = list(range(-(n-1),n+1))
    return dist_gen[pos_in_sub_level]

x = 361527
print(man_dist((get_level(x), dist_from_straight_shot(x))))



  
