
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def closest_pair_brute_force(p, q1, q2):
    min_cost = 65535
    for i in range(len(p)-1):
        for j in range(i+1, len(p), 1):
            cost = math.sqrt((p[i].x - p[j].x)**2 + (p[i].y - p[j].y)**2)
            if cost < min_cost:
                min_cost = cost
    return min_cost

def closest_pair(p, q1, q2):
    """
    p : array of pointers
    q1: area 1 on x-axis
    q2: area2
        index of each point
    """
    if q2 - q1 <= 3:    # less then 3 points in the area
        return closest_pair_brute_force(p, q1, q2)

    d1 = closest_pair(p, q1, (q1+q2)/2)
    d2 = closest_pair(p, (q1+q2)/2, q2)
    min_d = min(d1, d2)

    # cross area : brute force..
    cross_d = min( distance between m-d ~ m+d area)
    min_d = min(min_d, cross_d)
    return mid_d


