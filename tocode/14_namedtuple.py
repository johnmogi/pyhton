import collections

Coordinate = collections.namedtuple('Coordinate', ['x','y','z'])

p1 = Coordinate(x=10,y=25,z=450)
p2 = Coordinate(33,44,55)
p3 = p1.y + p2.x

print(p1,p2,p3)