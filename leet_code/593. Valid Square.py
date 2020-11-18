import collections
import heapq


class Solution:
    def validSquare(self, p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p = [p1, p2, p3, p4]
        d = collections.defaultdict(int)
        for i in range(3):
            for j in range(i+1, 4):
                ax, ay = p[i]
                bx, by = p[j]
                ds = (ay-by)**2 + (ax-bx)**2
                d[ds] += 1
        # print d
        x = sorted(d.keys())
        # print x
        if len(x)==2:
            a, b = x
            if a>0 and b==2*a and d[a]==4 and d[b]==2:
                return True
        return False

    """
    Consider the square with side-length S placed in any orientation and location on the plane. The pairwise distances between points (in sorted order) are: S, S, S, S, S*sqrt(2), S*sqrt(2). With some thinking, we can prove this is a necessary and sufficient condition [details after]. Therefore, we should only check this condition, plus that S > 0. For convenience, we'll work with the squares of distances instead.

    Let's now prove our condition was necessary and sufficient.

Suppose points ABCD have pairwise distances in sorted order S, S, S, S, S*sqrt(2), S*sqrt(2). We want to show ABCD is a square. Let us call S a "small side" and S*sqrt(2) a "large side". Without loss of generality, suppose AC is a large side. If BD is a large side, then AB and BC are small sides, so B lies on the intersection of circles between A and C; similarly, D lies on the same intersection, and thus ABCD is a square (as two different circles of the same radius only intersect in two different points).

All other cases (AB, AD, CB, CD having a large side) are similar, so we'll only consider AB having a large side. Then, BC is the base of icoceles triangles ABC and DBC, so A and D must lie on the perpendicular bisector to BC. D must be closer to BC than A is (otherwise |DB| > |DA| is a contradiction). Since BDC is an equilateral triangle, angle ∠BDC = 60°, and therefore equal angles ∠ADB + ∠ADC = 300° and ∠ADB = 150°. But the sidelengths of triangle ADB are known, which uniquely determines ∠ADB = 90°, a contradiction.
    """

    def validSquare(self, p1, p2, p3, p4):
        def dist(P, Q):
            return (P[0] - Q[0])**2 + (P[1] + Q[1])**2
        
        D = [dist(p1, p2), dist(p1, p3), dist(p1, p4),
             dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        D.sort()
        return 0 < D[0] == D[1] == D[2] == D[3] and 2*D[0] == D[4] == D[5]

print(True == Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))

