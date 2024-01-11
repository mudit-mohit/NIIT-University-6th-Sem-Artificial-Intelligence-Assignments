import random
def prnt_brd(brd):
    for r in brd:
        print(" ".join(r))
    print()
def chck_wn(brd, symbl):
    for i in range(3):
        if all(brd[i][j] == symbl for j in range(3)) or all(brd[j][i] == symbl for j in range(3)):
            return True
    if all(brd[i][i] == symbl for i in range(3)) or all(brd[i][2 - i] == symbl for i in range(3)):
        return True
    return False
def gt_emp_position(brd):
    emp_position = []
    for i in range(3):
        for j in range(3):
            if brd[i][j] == ' ':
                emp_position.append((i, j))
    return emp_position
def mke_bst_mov(brd):
    for i in range(3):
        if brd[i].count('x') == 2 and brd[i].count(' ') == 1:
            return i, brd[i].index(' ')
        if [brd[j][i] for j in range(3)].count('x') == 2 and [brd[j][i] for j in range(3)].count(' ') == 1:
            return [brd[j][i] for j in range(3)].index(' '), i
    if [brd[i][i] for i in range(3)].count('x') == 2 and [brd[i][i] for i in range(3)].count(' ') == 1:
        return [brd[i][i] for i in range(3)].index(' '), [brd[i][i] for i in range(3)].index(' ')
    if [brd[i][2 - i] for i in range(3)].count('x') == 2 and [brd[i][2 - i] for i in range(3)].count(' ') == 1:
        return [brd[i][2 - i] for i in range(3)].index(' '), 2 - [brd[i][2 - i] for i in range(3)].index(' ')
    for i in range(3):
        if brd[i].count('o') == 2 and brd[i].count(' ') == 1:
            return i, brd[i].index(' ')
        if [brd[j][i] for j in range(3)].count('o') == 2 and [brd[j][i] for j in range(3)].count(' ') == 1:
            return [brd[j][i] for j in range(3)].index(' '), i
    if [brd[i][i] for i in range(3)].count('o') == 2 and [brd[i][i] for i in range(3)].count(' ') == 1:
        return [brd[i][i] for i in range(3)].index(' '), [brd[i][i] for i in range(3)].index(' ')
    if [brd[i][2 - i] for i in range(3)].count('o') == 2 and [brd[i][2 - i] for i in range(3)].count(' ') == 1:
        return [brd[i][2 - i] for i in range(3)].index(' '), 2 - [brd[i][2 - i] for i in range(3)].index(' ')
    for i in range(3):
        if brd[i].count('x') == 1 and brd[i].count(' ') == 2:
            return i, brd[i].index(' ')
        if [brd[j][i] for j in range(3)].count('x') == 1 and [brd[j][i] for j in range(3)].count(' ') == 2:
            return [brd[j][i] for j in range(3)].index(' '), i
    if [brd[i][i] for i in range(3)].count('x') == 1 and [brd[i][i] for i in range(3)].count(' ') == 2:
        return [brd[i][i] for i in range(3)].index(' '), [brd[i][i] for i in range(3)].index(' ')
    if [brd[i][2 - i] for i in range(3)].count('x') == 1 and [brd[i][2 - i] for i in range(3)].count(' ') == 2:
        return [brd[i][2 - i] for i in range(3)].index(' '), 2 - [brd[i][2 - i] for i in range(3)].index(' ')
    for i in range(3):
        if brd[i].count('o') == 1 and brd[i].count(' ') == 2:
            return i, brd[i].index(' ')
        if [brd[j][i] for j in range(3)].count('o') == 1 and [brd[j][i] for j in range(3)].count(' ') == 2:
            return [brd[j][i] for j in range(3)].index(' '), i
    if [brd[i][i] for i in range(3)].count('o') == 1 and [brd[i][i] for i in range(3)].count(' ') == 2:
        return [brd[i][i] for i in range(3)].index(' '), [brd[i][i] for i in range(3)].index(' ')
    if [brd[i][2 - i] for i in range(3)].count('o') == 1 and [brd[i][2 - i] for i in range(3)].count(' ') == 2:
        return [brd[i][2 - i] for i in range(3)].index(' '), 2 - [brd[i][2 - i] for i in range(3)].index(' ')
    emp_position = gt_emp_position(brd)
    return random.choice(emp_position)
brd = [[' ' for _ in range(3)] for _ in range(3)]
print("Initial Board:")
prnt_brd(brd)
r, c = mke_bst_mov(brd)
brd[r][c] = 'x'
print("Updated Board:")
prnt_brd(brd)
