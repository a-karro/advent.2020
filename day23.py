class Cups:
    def __init__(self, data):
        self.data = dict.fromkeys(set(data))
        for i, d in enumerate(data[:-1]):
            self.data[d] = data[i+1]
        self.data[data[-1]] = data[0]
        self.cur = data[0]
        self.mx = max(data)
        self.mn = min(data)
        self.fragment = [0, 0, 0]
        self.has_fragment = False

    def calc_dest(self):
        dc = self.cur - 1
        if dc < self.mn:
            dc = self.mx
        while self.has_fragment and dc in self.fragment:
            dc = dc - 1
            if dc < self.mn:
                dc = self.mx
        return dc

    def move_to_next(self):
        self.cur = self.data[self.cur]

    def remove_3(self):
        p = self.data[self.cur]
        for i in range(3):
            self.fragment[i] = p
            p = self.data[p]
        self.data[self.cur] = p
        self.has_fragment = True

    def insert_3_at_dest(self, dd):
        if not self.has_fragment:
            return
        self.has_fragment = False
        k = self.data[dd]
        self.data[dd] = self.fragment[0]
        self.data[self.fragment[2]] = k

    def get_from_1(self, two=False):
        x = 1
        r = ''
        if two:
            f = self.data[1]
            k = self.data[f]
            r = str(f * k)
        else:
            for _ in range(8):
                r = r + str(self.data[x])
                x = self.data[x]
        return r

    def play(self, limit):
        cnt = 0
        while cnt < limit:
            cnt += 1
            if cnt % 1_000_000 == 0:
                print("moves: ", cnt)
            self.remove_3()
            dest = self.calc_dest()
            self.insert_3_at_dest(dest)
            self.move_to_next()


s = [int(c) for c in open('data/day23.txt', 'r').read()]
dl = len(s)

cups = Cups(s)
cups.play(100)
print("Puzzle 23.1: ", cups.get_from_1(two=False))

s.extend(list(range(cups.mx+1, 1_000_001)))
cups = Cups(s)
cups.play(10_000_000)
print("Puzzle 23.2: ", cups.get_from_1(two=True))
