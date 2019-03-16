


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.red = False

class RBTree:
    def __init__(self):
        self.root = None # Node
        self.n = 0

    def find(self, key, value):
        cur = self.root
        while None != cur:
            if cur.data.key < key:
                cur = cur.right
            elif cur.data.key > key:
                cur = cur.left
            else:
                break
        return cur if cur.value.key == key else None

    def rotate(self, key, pivot):
        child = gchild = None
        if key >= pivot.data.key and pivot != self.root:
            child = pivot.right
        else:
            child = pivot.left
        if key >= child.data.key:       # left rotation
            gchild = child.right
            child.right = gchild.left
            gchild.left = child
        else:                           # right rotation
            gchild = child.left
            child.left = gchild.right
            gchild.right = child

        if key >= pivot.data.key and pivot != self.root:
            pivot.right = gchild
        else:
            pivot.left = gchild
        return gchild

    def insert(self, key, value):
        '''
             [ggp]
                \
                 [gp]
                     \
                      [p] <- red
                     /
                   [t]    <- red
                  /   \
                 a     b 

            at final, t's color is changed to black
                     gp's color is changed to red
        '''
        ggp = gp = p = self.root
        t = self.root.left

        while None != t:
            if value == t.data.value:   # duplicate value
                return False
            if t.left != None and t.right != None and t.left.red == True and t.right.red == True:
                # do color promotion
                t.red = True
                t.left.red = t.right.red = False
                if True == p.red:   # need rotation
                    gp.red = True   # see the diagram above
                    if (value > gp.data.value) != (value > p.data.value): # twist case like above
                        p = rotate(value, gp)   # double rotation
                    t = rotate(value, ggp)      # rotation based on ggp(pivot)
                    t.red = False
                self.root.left.red = False      # root cannot be red
            ggp = gp
            gp = p
            p = t
            if value > t.data.value:
                t = t.right
            else:
                t = t.left

        t = Node()
        t.data.value = value
        t.left = t.right = None
        t.red = True
        if value > p.data.value and p != self.root:
            p.right = t
        else:
            p.left = t
        self.n += 1
        if p.red == True:
            gp.red = True
            if value > gp.data.value != value > p.data: # twist case like above
                p = rotate(value, gp)   # double rotation
            t = rotate(value, ggp)
            t.red = False
        self.root.left.red = False
        return True

    def delete_leaf(self, value, delp, deln):
        if value == deln.data.value and deln.left == None and deln.right == None:
            # red leaf case
            del deln
            if (value >= delp.data.value) and delp != self.root:
                delp.right = None
            else:
                delp.left = None
            return True
        elif value == deln.data.value:    # black node with at least one child
            if deln.left != None:
                deln.left.right = deln.right
                ret = deln.left
            else:                           # delte right child
                deln.right.left = deln.left
                ret = deln.right
            ret.red = False
            del deln
            if (ret.data.value >= delp.data.value) and delp != self.root:
                delp.right = ret
            else:
                delp.left = ret
            return True
        elif deln.left != None and value == deln.left.data.value:
            del deln.left
            deln.left = None
            return True
        elif deln.right != None and value == deln.right.data.value:
            del deln.right
            deln.right = None
            return True
        return False

    def read_as_parent(self, delgp, delp, sib): # when sibling is red
        '''
                dlep       ==>      sib
               /    \               /  \
             del    sib <- red    delp  d
            /   \  /   \         /   \
           a    b  c    d       del   c
                               /  \
                              a    b

        '''
        if sib == None or sib.red == False:
            return False
        rotate(sib.data.value, delgp)
        sib.red = False
        delp.red = True
        return True

    def bind_node(self, delp):
        delp.red = False
        delp.left.red = True
        delp.right.red = True

    def is_leap(self, p):
        '''
        two child are red
        '''
        if p == None:
            return False
        if (p.left == None or p.left == None and p.left.red == True and 
            p.left.left == None and p.left.right == None) and\
            (p.right == None and p.right.red == True and
            p.right.left == None and p.right.right == None):
            return True
        else:
            return False

    def is_2_node(self, p):
        '''
        no child or two black nodes case
        '''
        if p == None:
            return False
        if p.red == True:
            return False
        if (p.left == None and p.right == None) or 
            (p.left != None and p.right != None and p.left.red == False and p.right.red == False):
            return True
        else:
            return False

    def borrow_key(self, delp, delp, deln, sib):
        if is_2_node(sib):  # child are all black or no chid case
            return False
        if deln.data.value > sib.data.value:
            if sib.left != None and sib.left.red == True:
                sibc = sib.left
            else:
                sibc = sib.right
        else:
            if sib.right != None and sib.right.red == True:
                sibc = sib.right
            else:
                sibc = sib.left
        if (delp.data.value > sib.data.value) != (sib.data.value > sibc.data.value):
            # double rotation
            rotate(sibc.data.value, delp)
            rotate(sibc.data.value, delpg)
            sib.red = False
            sibc.red = True
        else:
            # single rotation
            rotate(sib.data.value, delgp)
            sib.red = True
            sibc.red = False
        deln.red = True
        delp.red = False
        if self.root.left.red == True:
            self.root.left.red = False
        return True

    def swap_key(self, deln):
        cdd = deln.right
        while cdd.left != None:
            cdd = cdd.left
        deln.data.value = cdd.data.value
        return cdd.data.value

    def remove(self, value):
        delgp = delp = self.root
        deln = self.root.left
        sib = None
        while is_leap(deln) == False:
            if deln.red == False:
                if read_as_parent(delgp, delp, sib):
                    delgp = sib
                    if deln.data.value >= delp.data.value:
                        sib = delp.left
                    else:
                        sib = delp.right
            if deln != self.root.left and is_2_node(deln):
                if False == borrow_key(delgp, delp, deln, sib):
                    bind_node(delp)
            if value == deln.data.value:
                value = swap_key(deln)
            delgp = delp
            delp = deln
            if vlaue >= deln.data.value:
                sib = deln.left
                deln = deln.right
            else:
                sib = deln.right
                deln = deln.left

        if deln.red == False:
            if read_as_parent(delgp, delp, sib):
                delgp = sib
                if deln.data.value >= delp.data.value:
                    sib = delp.left
                else:
                    sib = delp.right

        if deln != self.root.left and is_2_node(deln):
            if False == borrow_key(delgp, delp, deln, sib):
                bind_node(delp)
        if True == delete_leaf(value, delp, deln):
            self.n -= 1
            return True
        return False


