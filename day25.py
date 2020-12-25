data = open('data/day25.txt', 'r').read().splitlines()
card_pub = int(data[0])
door_pub = int(data[1])

sn = 7


def get_loop_size(subject, pub_key):
    x = 1
    cnt = 0
    while x != pub_key:
        cnt += 1
        x = x * subject % 20201227
    return cnt


def transform(subject, loop_size):
    x = 1
    for _ in range(loop_size):
        x = x * subject % 20201227
    return x


dl = get_loop_size(sn, door_pub)
cl = get_loop_size(sn, card_pub)

ek = transform(door_pub, cl)
ek2 = transform(door_pub, cl)
print("Puzzle 25.1: ", ek if ek == ek2 else "sumting wong")
