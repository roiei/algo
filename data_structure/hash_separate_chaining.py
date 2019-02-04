

class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value

class Hash_sc:
    def __init__(self, size, fp_hash):
        self.table_size = size
        self.table = [[] for i in range(size)]
        self.n = 0
        self.fp_hash = fp_hash

    def insert(self, key, value):
        index = self.fp_hash(key) % self.table_size
        self.table[index].insert(0, Node(key, value))
        #self.table[index][0:] = Node(key, value) # <- X
        return True

    def find(self, key):
        index = self.fp_hash(key) % self.table_size
        for node in self.table[index]:
            if node.key == key:
                return True
        return False

    def remove_at(self, key):
        index = self.fp_hash(key) % self.table_size
        i = 0
        found = False
        for node in self.table[index]:
            if node.key == key:
                found = True
                break
            i += 1
        if True == found:
            del self.table[index][i]
            return True
        return False

    def print_all(self):
        i = 0
        for alist in self.table:
            print('{:02}'.format(i), end=': ')
            for node in alist:
                print(node.key, node.value, end=' ')
            print()
            i += 1
        print()
        
def hash_unit_test():
    hash_map = Hash_sc(10, lambda x : x)
    hash_map.print_all()
    hash_map.insert(65, 'A')
    hash_map.print_all()
    hash_map.insert(67, 'C')
    hash_map.print_all()
    hash_map.insert(69, 'E')
    hash_map.print_all()
    hash_map.insert(79, 'O')    
    hash_map.print_all()
    hash_map.insert(70, 'F')
    hash_map.print_all()
    hash_map.remove_at(79)
    hash_map.print_all()
    print(hash_map.find(70))
    hash_map.print_all()
    hash_map.insert(89, 'Y')
    hash_map.print_all()


hash_unit_test()