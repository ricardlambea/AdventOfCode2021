#!/usr/bin/python3

### DAY 5.1

# function to create the dot matrix
def draw_matrix(x_dim, y_dim):
    dot_matrix = []
    for x in range(0, y_dim+1):
        dot_matrix.append([])
        for y in range(0, x_dim+1):
            dot_matrix[x].append(0)
    return dot_matrix

with open('input.txt', 'r') as f:
    clean_coords = []
    max_xcoords = []
    max_ycoords = []
    for line in f:
        coords = line.strip().split(' -> ')
        x0 = int(coords[0].split(',')[0])
        y0 = int(coords[0].split(',')[1])
        x1 = int(coords[1].split(',')[0])
        y1 = int(coords[1].split(',')[1])
        if x0 == x1 or y0 == y1:
            clean_coords.append([x0, y0, x1, y1])
            max_xcoords.append(max(x0, x1))
            max_ycoords.append(max(y0, y1))
    # print(clean_coords)

    max_x = max(max_xcoords)
    max_y = max(max_ycoords)

    c_matrix = draw_matrix(max_x, max_y)
    print('matrix levels: ' + str(len(c_matrix)))
    print('matrix level length: ' + str(len(c_matrix[0])))

    for coords in clean_coords:
        if coords[0] != coords[2] and coords[1] == coords[3]: #vertical flow
            if coords[0] < coords[2]:
                for x in range(coords[0], coords[2]+1):
                    c_matrix[coords[1]][x] += 1
            else:
                for x in range(coords[2], coords[0]+1):
                    c_matrix[coords[1]][x] += 1
        elif coords[1] != coords[3] and coords[0] == coords[2]: #horizontal flow
            if coords[1] < coords[3]:
                for y in range(coords[1], coords[3]+1):
                    c_matrix[y][coords[0]] += 1
            else:
                for y in range(coords[3], coords[1]+1):
                    c_matrix[y][coords[0]] += 1

    counter = 0
    for sublist in c_matrix:
        counter += sublist.count(1)
        counter += sublist.count(0)
    print(len(c_matrix) * len(c_matrix[0]) - int(counter))

    f.close()
