# Collatz (Python)

## Status
![Build Status](https://travis-ci.org/nelmiux/Math-Collatz-Py.svg?branch=master)

### Functions
      	  	
collatz_eval(i, j)
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]

collatz_length(n)
    calculate the cycle length of n
    return the cycle length of an integer n

collatz_print(w, i, j, v)
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length

collatz_read(s)
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]

collatz_solve(r, w)
    r a reader
    w a writer

 
### Data
    cache = {1: 1}
