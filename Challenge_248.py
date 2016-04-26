# SOLUTION IN PYTHONNN 

from math import sqrt
from Queue import Queue

# bline, circle, ellipse function adapted from: http://members.chello.at/~easyfilter/bresenham.html

with open('248E.bitmap.input') as file:
    lines = [f.strip().split() for f in file]

def print_drawing(drawing):
    print 'P3\n%d %d\n255' % (len(drawing[0]), len(drawing))
    print '\n'.join([' '.join(['%-4d %-4d %-4d' % l for l in line]) for line in drawing])

def point(drawing, data):
    data = [int(d) for d in data]
    r, g, b, y, x = data[0:5]
    drawing[y][x] = (r, g, b)

def line(drawing, data):
    data = [int(d) for d in data]
    r, g, b = data[0:3]
    y1, x1, y2, x2 = data[3:7] if data[4] < data[6] else data[5:7] + data[3:5]
    for i in xrange(x1, x2 + 1):
        drawing[y1 + (y2 - y1) * (i - x1) // (x2 - x1)][i] = (r, g, b)

def rect(drawing, data):
    data = [int(d) for d in data]
    r, g, b, y, x, h, w = data[0:7]
    for i in xrange(h):
        drawing[y + i][x:x + w] = [(r, g, b) for p in xrange(w)]

def bline(drawing, data):
    data = [int(d) for d in data]
    r, g, b, y1, x1, y2, x2 = data[0:7]
    dx, sx = abs(x2 - x1), 1 if x1 < x2 else -1
    dy, sy = -abs(y2 - y1), 1 if y1 < y2 else -1
    err = dx + dy
    while True:
        drawing[y1][x1] = (r, g, b)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

def circle(drawing, data):
    data = [int(d) for d in data]
    r, g, b, ym, xm, r_ = data[0:6]
    x, y, err = -r_, 0, 2 - 2 * r_
    while x < 0:
        drawing[ym + y][xm - x] = (r, g, b)
        drawing[ym - x][xm - y] = (r, g, b)
        drawing[ym - y][xm + x] = (r, g, b)
        drawing[ym + x][xm + y] = (r, g, b)
        r_ = err
        if r_ <= y:
            y += 1
            err += 2 * y + 1
        if r_ > x or err > y:
            x += 1
            err += 2 * x + 1

def ellipse(drawing, data):
    data = [int(d) for d in data]
    r, g, b, ym, xm, rv, rh = data[0:7]
    y1, x1, y2, x2 = ym + rv, xm - rh, ym - rv, xm + rh

    a_, b_= abs(x2 - x1), abs(y2 - y1)
    b1 = b_&1
    dx, dy = 4.0 * (1 - a_) * b_ * b_, 4.0 * (b1 + 1) * a_ * a_
    err = dx + dy + 1.0 * b1 * a_ * a_

    if x1 > x2:
        x1 = x2
        x2 += a_
    if y1 > y2:
        y1 = y2
    y1 += (b_ + 1)/2
    y2 = y1 - b1
    a_ *= 8 * a_
    b1 = 8 * b_ * b_

    while x1 <= x2:
        drawing[y1][x2] = (r, g, b)
        drawing[y1][x1] = (r, g, b)
        drawing[y2][x1] = (r, g, b)
        drawing[y2][x2] = (r, g, b)
        e2 = 2 * err;
        if e2 <= dy:
            y1 += 1
            y2 -= 1
            dy += a_
            err += dy
        if e2 >= dx or 2 * err > dy:
            x1 += 1
            x2 -= 1
            dx += b1
            err += dx

    while y1 - y2 < b_:
        drawing[y1, x1 - 1] = (r, g, b)
        y1 += 1
        drawing[y1, x2 + 1] = (r, g, b)
        drawing[y2, x1 - 1] = (r, g, b)
        y2 -= 1
        drawing[y2, x2 + 1] = (r, g, b)


def fill(drawing, data):
    data = [int(d) for d in data]
    r, g, b, y, x = data[0:5]
    color = drawing[y][x]
    q = Queue()
    q.put([x, y])
    visited = set([])
    while not q.empty():
        curr = q.get()
        if tuple(curr) in visited:
            continue
        w = [curr[0], curr[1]]
        e = [w[0], w[1]]
        while w[0] > 0 and drawing[w[1]][w[0] - 1] == color:
            w[0] -= 1
        while e[0] < len(drawing[0]) - 1 and drawing[e[1]][e[0] + 1] == color:
            e[0] += 1
        for i in xrange(w[0], e[0] + 1):
            drawing[w[1]][i] = (r, g, b)
            if w[1] > 0 and drawing[w[1] - 1][i] == color:
                q.put([i, w[1] - 1])
            if w[1] < len(drawing) - 1 and drawing[w[1] + 1][i] == color:
                q.put([i, w[1] + 1])
        visited.add(tuple(curr))

def smartfill(drawing, data):
    data = [int(d) for d in data]
    r, g, b, y, x, tol = data[0:6]
    color = drawing[y][x]
    q = Queue()
    q.put([x, y])
    visited = set([])
    while not q.empty():
        curr = q.get()
        if tuple(curr) in visited:
            continue
        w = [curr[0], curr[1]]
        e = [w[0], w[1]]
        while w[0] > 0:
            curr_color = drawing[w[1]][w[0] - 1]
            dr, dg, db = curr_color[0] - color[0], curr_color[1] - color[1], curr_color[2] - color[2]
            if sqrt(dr * dr + dg * dg + db * db) < tol:
                w[0] -= 1
            else:
                break
        while e[0] < len(drawing[0]) - 1:
            curr_color = drawing[e[1]][e[0] + 1]
            dr, dg, db = curr_color[0] - color[0], curr_color[1] - color[1], curr_color[2] - color[2]
            if sqrt(dr * dr + dg * dg + db * db) < tol:
                e[0] += 1
            else:
                break
        for i in xrange(w[0], e[0] + 1):
            drawing[w[1]][i] = (r, g, b)
            if w[1] > 0:
                curr_color = drawing[w[1] - 1][i]
                dr, dg, db = curr_color[0] - color[0], curr_color[1] - color[1], curr_color[2] - color[2]
                if sqrt(dr * dr + dg * dg + db * db) < tol:
                    q.put([i, w[1] - 1])
            if w[1] < len(drawing) - 1:
                curr_color = drawing[w[1] + 1][i]
                dr, dg, db = curr_color[0] - color[0], curr_color[1] - color[1], curr_color[2] - color[2]
                if sqrt(dr * dr + dg * dg + db * db) < tol:
                    q.put([i, w[1] + 1])
        visited.add(tuple(curr))

def process(lines):
    x, y = int(lines[0][0]), int(lines[0][1])
    drawing = [[(0, 0, 0) for col in xrange(x)] for row in xrange(y)]
    for l in lines[1:]:
        if l[0] == 'point':
            point(drawing, l[1:])
        elif l[0] == 'line':
            line(drawing, l[1:])
        elif l[0] == 'rect':
            rect(drawing, l[1:])
        elif l[0] == 'bline':
            bline(drawing, l[1:])
        elif l[0] == 'circle':
            circle(drawing, l[1:])
        elif l[0] == 'ellipse':
            ellipse(drawing, l[1:])
        elif l[0] == 'fill':
            fill(drawing, l[1:])
        elif l[0] == 'smartfill':
            smartfill(drawing, l[1:])
    print_drawing(drawing)

process(lines)