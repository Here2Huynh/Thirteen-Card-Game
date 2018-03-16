#print triangles

def print_right_triangle(n):
    """ """
    #rows
    for i in range(n + 1):
        print i * 'x'
print 'This is right triangle: '
print_right_triangle(5)

def print_rotated_right_triangle(n):
    """ """
    for i in range(n + 1):
        print ((n - i) * ' ') + ('x' * i)
print 'This is rotated right triangle: '
print_rotated_right_triangle(5)

def isosceles_triangle(n):
    """ """
    #2space + 1x + 2space x
    #1space + 2x + 1space xx
    #0space + 3x + 0space xxx
    for i in range(1,n+1):
	       print ((n - i) * ' ' + i * '* ')
print 'This is a isosceles triangle: '
isosceles_triangle(5)

#now invert them
#print diamonds 
