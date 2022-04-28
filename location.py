coor2 = [
    [-33.8795427,151.2052461],
    [-33.8743232,151.2067895],
    [-33.86870221443746, 151.2069698691709],
    [-33.86259456606607, 151.20752876231285]
]

# coor3 = [
#     [-33.87969,151.2052],
#     [-33.8744196,151.2067381]
# ]

# dist = [
#     600,
# ]

dist = [
    600,
    475,
    680,
]

def sampled_coor (dist, coor1x, coor1y, coor2x, coor2y):
    """ Generate coordinates and return list of coordinates for sampling streetview images.

    Args:
        dist (list): distance between two coordinates
        coor1x (float): x coordinate of the first coordinate
        coor1y (float): y coordinate of the first coordinate
        coor2x (float): x coordinate of the second coordinate
        coor2y (float): y coordinate of the second coordinate

    Returns:
        list: list of coordinates
    """

    sample = dist/20
    coorx = (coor2x - coor1x)/sample
    coory = (coor2y - coor1y)/sample
    
    coor_list = []
    for i in range(int(sample)):
        coor_list.append([coor2x - i*coorx, coor2y - i*coory])
    return coor_list

# print(sampled_coor(dist[1], coor[0][0], coor[0][1], coor[1][0], coor[1][1]))

# def coor_list():
#     for i in dist:
#         sampled_coor(dist[i], coor2[i][0], coor2[i][1], coor2[i+1][0], coor2[i+1][1])

def route_coor(dist, coor):
    """ Generate coordinates and return list of coordinates for sampling streetview images.

    Args:
        dist (list): distance between two coordinates
        coor1x (float): x coordinate of the first coordinate
        coor1y (float): y coordinate of the first coordinate
        coor2x (float): x coordinate of the second coordinate
        coor2y (float): y coordinate of the second coordinate

    Returns:
        list: list of coordinates
    """


    coor_list = []

    for i in range(len(dist)):
        sample = dist[i]/20
        coorx = (coor[i+1][0] - coor[i][0])/sample
        coory = (coor[i+1][1] - coor[i][1])/sample

        for j in range(int(sample)):
            coor_list.append([coor[i+1][0] - j*coorx, coor[i+1][1] - j*coory])
    return coor_list

coor = route_coor(dist, coor2)