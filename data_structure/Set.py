


class SetItem:
    def __init__(self, name, parent, height):
        self.name   = name
        self.parent = parent
        self.height = height

    def __eq__(self, other):
        return self.name == other

class Set:
    def __init__(self):
        self.items = []
        self.n = 0

    def add(self, item):
        self.items.append(SetItem(item, -1, 1))
        self.n += 1
        return self.n - 1

    def find(self, item_to_find):
        idx = 0
        for item in self.items:
            if item == item_to_find:
                break
            idx += 1
        if idx >= self.n:
            return -1

        while self.items[idx].parent >= 0:
            idx = self.items[idx].parent     # parent >= 0
        return idx                           # index of root

    def union_by_idx(self, idx1, idx2):
        if self.items[idx1].height > self.items[idx2].height:
            self.items[idx2].parent = idx1
        elif self.items[idx1].height < self.items[idx2].height:
            self.items[idx1].parent = idx2
        else:
            self.items[idx1].height += 1
            self.items[idx2].parent = idx1


