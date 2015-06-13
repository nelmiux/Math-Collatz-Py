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
        assert (((type(i) is int) and (type(j) is int)) == True)
        assert (((i > 0) and (j > 0) and (i < 1000001) and (j < 1000001) and (i <= j)) == True)
        m = 1
        for n in range (i, j + 1) :
            l = length (n)
            if m < l :
                m = l
    except (TypeError, ValueError, AssertionError, OverflowError, MemoryError) :
        m = 0

    """                          
    if (((type(i) is int) == False) or ((type(j) is int) == False)) :
        raise TypeError
    """
    """                 
    if ((i < 1) or (j < 1) or (i > 1000000) or (j > 1000000) or (i > j)) :
        raise ValueError
    """
    return m

def length (n) :
    l = 1
    while n > 1 :
        if (n % 2 == 0) :
            n = n / 2
        else :
            n = 3 * n + 1
        l += 1
    return l;

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
        assert (((type(i) is int) and (type(j) is int) and (type(v) is int)) == True)
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
