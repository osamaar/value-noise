from random import random, seed

def debug_func(fn):
    def new(*args, **kwargs):
        print 'DEBUG: function call:', fn.func_name, args, kwargs
        return fn(*args, **kwargs)
    return new

#@debug_func
def octave(step, amp, bitmap, modifier):
    size = len(bitmap)
    for i in xrange(0, size-1, step):
        for j in xrange(0, size-1, step):
            modifier[i      ][j      ] = random()%amp - 0.5*amp
            modifier[i      ][j+step] = random()%amp - 0.5*amp
            modifier[i+step][j      ] = random()%amp - 0.5*amp
            modifier[i+step][j+step] = random()%amp - 0.5*amp

    for i in xrange(0, size-1, step):
        for j in xrange(0, size-1, step):
            bilinear(modifier, i, j, step+1)

    for i in xrange(size):
        for j in xrange(size):
            bitmap[i][j] += modifier[i][j]

def print_map(bitmap):
    print '\n'.join([str([round(y, 2) for y in x]) for x in bitmap])

def bilinear(bitmap, i0, j0, size):
    # bilinear interpolation by interpolating on x axis then y axis
    # en.wikipedia.org/wiki/Bilinear_interpolation#Algorithm
    shift = size - 1
    denum = shift*shift
    for i in xrange(i0, i0+size):
        for j in xrange(j0, j0+size):
            enum = bitmap[i0      ][j0      ] * (i0 + shift - i) * (j0 + shift - j) + \
                   bitmap[i0+shift][j0      ] * (i - i0        ) * (j0 + shift - j) + \
                   bitmap[i0      ][j0+shift] * (i0 + shift - i) * (j - j0        ) + \
                   bitmap[i0+shift][j0+shift] * (i - i0        ) * (j - j0        )
            bitmap[i][j] = enum/float(denum)
            
def test_bilinear():
    m = [[0, 0, 0, 3],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 3]]
    print m
    bilinear(m, 0, 0, 4)
    print m

#@debug_func
def generate(size, octaves, map_seed=None):
    if 2**octaves > size:
        raise ValueError('Cannot have more octaves than map size')

    seed(map_seed)
    bitmap = [[0]*size for i in xrange(size)]
    modifier = [[0]*size for i in xrange(size)]

    # step controls level of detail
    step = size-1
    amp = 1
    presist = .6
    while step > 1 and octaves !=0:
        octave(step, amp, bitmap, modifier)
        step /= 2
        amp *= presist
        print octaves
        octaves -= 1

    return bitmap

def normalize(bitmap, start, end):
    size = len(bitmap)
    peak = 1.0 * max(max(x) for x in bitmap)
    valley = 1.0 * min(min(x) for x in bitmap)
    scale = end - start
    for i in xrange(size):
        for j in xrange(size):
            bitmap[i][j] = start + scale*(bitmap[i][j] - valley)/(peak - valley)

