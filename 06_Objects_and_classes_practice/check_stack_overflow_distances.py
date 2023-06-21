points = [(-12, 30), (6, 18), (6, 18)]


def euclidean_distance(coordinate1, coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1] - coordinate2[1], 2), .5)


distances = []

for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        distances += [euclidean_distance(points[i], points[j])]


print (min(distances))
