import collections
import queue
import sys

hand = queue.Queue()
pile = [collections.deque(), collections.deque(), collections.deque(), collections.deque(), collections.deque(),
        collections.deque(), collections.deque()]


def reduce(pile):
    while len(pile) >= 3:
        n = int(len(pile))
        if (pile[0] + pile[1] + pile[n - 1]) % 10 == 0:
            hand.put(pile.popleft())
            hand.put(pile.popleft())
            hand.put(pile.pop())
        elif (pile[0] + pile[n - 2] + pile[n - 1]) % 10 == 0:
            hand.put(pile.popleft())
            k = pile.pop()
            hand.put(pile.pop())
            hand.put(k)
        elif (pile[n - 3] + pile[n - 2] + pile[n - 1]) % 10 == 0:
            hand.put(pile[n - 3])
            hand.put(pile[n - 2])
            hand.put(pile[n - 1])
            pile.pop()
            pile.pop()
            pile.pop()
        else:
            break


while 1:

    while not hand.empty():
        hand.get()
    for i in range(0, 7):
        pile[i].clear()
    x = str(input())
    lis = x.split()
    if len(lis) == 1:
        sys.exit(0)

    for i in range(0, 52):
        hand.put(int(lis[i]))

    for i in range(0, 7):
        pile[i].append(hand.get())

    for i in range(0, 7):
        pile[i].append(hand.get())

    end = int(0)
    loop = int(14)

    while not end:
        for i in range(0, 7):
            if len(pile[i]) == 0:
                continue
            loop = loop + 1
            pile[i].append(hand.get())
            reduce(pile[i])

            if hand.qsize() == 52:
                print("Win : " + str(loop))
                end = 1
                break

            if hand.qsize() == 0:
                print("Loss : " + str(loop))
                end = 1
                break