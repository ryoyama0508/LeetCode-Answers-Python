def bits_insertion2(n, m, i, j):
    int_n, int_m = int(n, 2), int(m, 2)
    for idx in range(j - i + 1):
        if (int_m >> idx) & 1 != 0:
            int_n |= 1 << (idx + i)
    return "{0:b}".format(int_n)


result_backtarcking = []


def find_bst_sequences_backtracking(bst):
    if not bst.root:
        return []
    backtarcking([bst.root], [])
    return result_backtarcking


def backtarcking(choices, sequence):
    if not len(choices):
        result_backtarcking.append(sequence)
        return

    for i in range(len(choices)):
        if choices[i].left:
            if choices[i].right:
                backtarcking(
                    choices[:i]
                    + choices[i + 1 :]
                    + [choices[i].left, choices[i].right],
                    sequence + [choices[i].key],
                )
            backtarcking(
                choices[:i] + choices[i + 1 :] + [choices[i].left],
                sequence + [choices[i].key],
            )
        elif choices[i].right:
            backtarcking(
                choices[:i] + choices[i + 1 :] + [choices[i].right],
                sequence + [choices[i].key],
            )
        else:
            backtarcking(choices[:i] + choices[i + 1 :], sequence + [choices[i].key])


ret = 4294967292
print("{0:b}".format((1 << 31)))
print("{0:b}".format(ret))

new = (1 << 31) - ret
print("{0:b}".format(new))

print("{0:b}".format(new & ret))


def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0:  # if sign bit is 1, that means negative
        val = val - (1 << bits)  # compute negative value
    return val
