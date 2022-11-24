from typing import List

def sea_cucumbers(config: List[List[str]]):
    # complexity: = 4*(E+S)*counter + n*m
    # counter = number of needed iterations till they stop
    # number of unblocked east cucumbers = E
    # number of unblocked south cucumbers = S
    # n*m for initial search
    # for each iteration:
    # E*(4 checks: left, right at new location, up, and up at new location) + S*(4 checks)

    old_queue_east = set()  # queue for unblocked east cucumbers
    new_queue_east = set()  # a temporary queue to hold popped cucumbers until all have been popped and moved
    old_queue_south = set()  # queue for unblocked south cucumbers
    new_queue_south = set()  # a temporary queue to hold popped cucumbers until all have been popped and moved
    temp_queue = set()  # a temporary queue to hold cucumbers of the same tribe that have been freed

    n = len(config)
    m = len(config[0])
    counter = 1  # count the iterations till stop

    # initial search and fill queues
    for i in range(n):
        for j in range(m):
            iplus = (i + 1) % n
            jplus = (j + 1) % m
            if config[i][j] == 'v' and config[iplus][j] == '.':
                old_queue_south.add((i, j))
            if config[i][j] == '>' and config[i][jplus] == '.':
                old_queue_east.add((i, j))

    # update the queues at each iteration
    while (old_queue_east or old_queue_south) and counter < 100:
        while old_queue_east:
            i, j = old_queue_east.pop()
            iminus = (i - 1) % n
            jplus, jminus = (j + 1) % m, (j - 1) % m
            config[i][j] = '.'  # update old square
            config[i][jplus] = '>'  # update new square
            new_queue_east.add((i, jplus))  # we don't know if this cucumber is blocked yet

            # update adjacent south cucumbers
            if config[iminus][j] == 'v':
                old_queue_south.add((iminus, j))  # old square is now free
            if config[iminus][jplus] == 'v':
                old_queue_south.remove((iminus, jplus))  # new square is now taken

            # another east cucumber has been freed
            if config[i][jminus] == '>':
                temp_queue.add((i, jminus))

        # which cucumbers are now blocked?
        while new_queue_east:
            i, j = new_queue_east.pop()
            jplus = (j + 1) % m
            if config[i][jplus] == '.':
                old_queue_east.add((i, j))
        while temp_queue:
            old_queue_east.add(temp_queue.pop())

        while old_queue_south:
            i, j = old_queue_south.pop()
            iplus, iminus = (i + 1) % n, (i - 1) % n
            jminus = (j - 1) % m
            config[i][j] = '.'  # update old square
            config[iplus][j] = 'v'  # update new square
            new_queue_south.add((iplus, j))  # we don't know if this cucumber is blocked yet
            if config[i][jminus] == '>':
                old_queue_east.add((i, jminus))  # old square is now free
            if config[iplus][jminus] == '>':
                old_queue_east.remove((iplus, jminus))  # new square is now taken
            if config[iminus][j] == 'v':
                temp_queue.add((iminus, j))

        while new_queue_south:
            i, j = new_queue_south.pop()
            iplus = (i + 1) % n
            if config[iplus][j] == '.':
                old_queue_south.add((i, j))
        while temp_queue:
            old_queue_south.add(temp_queue.pop())

        counter += 1

    return counter

def build_input():
    l = ["v...>>.vv>",
         ".vv>>.vv..",
         ">>.>v>...v",
         ">>v>>.>.v.",
         "v>v.vv.v..",
         ">.>>..v...",
         ".vv..>.>v.",
         "v.v..>>v.v",
         "....v..v.>"]
    l = [list(row) for row in l]
    return l

if __name__ == '__main__':
    l = build_input()
    for row in l:
        print("".join(row))
    sol = sea_cucumbers(l)
    print(sol)
    for row in l:
        print("".join(row))
