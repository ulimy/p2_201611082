Locations=tuple()
Locations=[(37.576557,126.985470),(37.571617,126.976439),(37.574454,126.957917),(37.570172,126.983096,(37.570423,126.992178))]
a=37.579618
b=126.977041
import math
distance=list()
for i in Locations:
    distances=math.sqrt(a-i[0])**2+(b-i[1])**2
    distance.append(distances)
print (min(y))