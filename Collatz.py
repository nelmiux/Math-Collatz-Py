#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    try :
        assert ((len (a)) == 2)
        assert ((type(a[0]) is str) and (type(a[1]) is str))
        assert ((type(int(a[0])) is int) and (type(int(a[1])) is int))
    except (TypeError, ValueError, AssertionError, OverflowError, MemoryError) :
        return [0, 0]
    return [int(a[0]), int(a[1])]

# ------------
# collatz_length
# ------------

cache = {1: 1}

def collatz_length (n) :
    """
    calculate the cycle length of n
    return the cycle length of an integer n
    """
    l = 1
    t = n
    if n in cache :
        l = cache[t]
    else :
        while n != 1 :
            if (n % 2 == 0) :
                n = n // 2
            else :
                n = (3 * n + 1) // 2
                l += 1
            l += 1
    cache[t] = l
    return l

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    try :
        assert ((type(i) is int) and (type(j) is int))
        assert ((i > 0) and (j > 0) and (i < 1000001) and (j < 1000001))
        if (i == j) :
            return collatz_length(i)
    except (TypeError, ValueError, AssertionError, OverflowError, MemoryError) :
       return 0
    return max(collatz_length(n) for n in range(min(i, j), max(i, j) + 1))

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    try :
        assert ((type(i) is int) and (type(j) is int) and (type(v) is int))
        assert (v != 0)
        assert (w is not None)
        w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
    except (TypeError, ValueError, AssertionError, OverflowError, MemoryError) :
        w.write("")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
