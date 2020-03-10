import time


class Solution:
    def reconstructQueue(self, people):
        if not people:
            return []
        people.sort(key=lambda param: param[1])
        queue = []
        queue.append(people[0])
        people.pop(0)
        for p in people:
            #print('p = {}, {}'.format(p[0], p[1]))
            inserted = False
            front_cnt = p[1]
            for i in range(len(queue)):
                if p[0] > queue[i][0]:
                    continue
                elif p[0] <= queue[i][0] and front_cnt > 0:
                    front_cnt -= 1
                    continue

                queue.insert(i, p)
                inserted = True
                break

            if False == inserted:
                queue.append(p)
        return queue


    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        
        people.sort(key=lambda p:p[1])
        res = [people.pop(0), (-1, -1)]

        for p in people:
            left = p[1]
            for i in range(len(res)):
                if p[0] > res[i][0]:
                    continue
                    
                if p[0] <= res[i][0] and left:
                    left -= 1
                    continue
                break
            
            res.insert(i, p)

        res.pop()
        return res


inputs = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

stime = time.time()
sol = Solution()
ret = sol.reconstructQueue(inputs)
print('elapse time: {} sec'.format(time.time() - stime))
print(ret)