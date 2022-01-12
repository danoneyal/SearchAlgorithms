import matplotlib.cm as cm
import matplotlib.pyplot as plt

import bresenhams_line_generation_algorithm as bla
from bresenhams_line_generation_algorithm import *


class LineCoordinate:
    def __init__(self):
        self.start_position = PixelPosition()
        self.end_position = PixelPosition()

line = LineCoordinate()
line_array = []

# line.start_position = PixelPosition()
# line.end_position = PixelPosition()


# m slope is infinite
# delta_x_zero__positive_y_direction(self):
x1 = 45
x2 = 45
y1 = 1
y2 = 45
line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))

# delta_x_zero__negative_y_direction
x1 = 45
x2 = 45
y1 = 45
y2 = 1

line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))

# m slope is zero
# delta_y_zero__positive_x_direction(self):

x1 = 1
x2 = 45
y1 = 20
y2 = 20

line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))

# delta_y_zero__negative_x_direction(self):  #

x1 = 45
x2 = 1
y1 = 20
y2 = 20

line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))

# delta_y_smaller_then_delta_x -1<m<1,abs(m)<1
# delta_y_smaller_then_delta_x__positive_x_positive_y_direction(self):  # -1<m<1, abs(m)<1, x1<x2 , y1<y2

x1 = 1
x2 = 45
y1 = 1
y2 = 20
line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))
# delta_y_smaller_then_delta_x__positive_x_negative_y_direction(self):  # -1<m<1, abs(m)<1,x1<x2 , y1>y2

x1 = 1
x2 = 45
y1 = 45
y2 = 20
line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))
# delta_y_smaller_then_delta_x__negative_x_positive_y_direction(self):  # -1<m<1, abs(m)<1,x1>x2 , y1<y2

x1 = 45
x2 = 1
y1 = 20
y2 = 45
line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))
# delta_y_smaller_then_delta_x__negative_x_negative_y_direction(self):  # -1<m<1, abs(m)<1, x1>x2 , y1>y2
x1 = 45
x2 = 1
y1 = 45
y2 = 20
line.start_position.horizontal = x1
line.start_position.vertical = y1
line.end_position.horizontal = x2
line.end_position.vertical = y2
line_array.append(copy.deepcopy(line))
"""
       
    # delta_y_greater_then_delta_x -1<m<-1, abs(m)>1
    def test_line_search__delta_y_greater_then_delta_x__positive_x_positive_y_direction(self):# -1<m<-1, abs(m)>1, x1<x2 , y1<y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__positive_x_negative_y_direction(self):# -1<m<-1, abs(m)>1, x1<x2 , y1>y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__negative_x_positive_y_direction(self):#-1<m<-1, abs(m)>1, x1>x2 , y1<y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__negative_x_negative_y_direction(self):#-1<m<-1, abs(m)>1, x1>x2 , y1>y2
        pass
    
"""
for line in line_array:
    bla.BresenhamsLineGenerationAlgorithm.bresenham(line.start_position, line.end_position, 1)

    len_pixel_position_array = len(pixel_position_array)

    calc_result_array_short = np.zeros((2, len(pixel_position_array)))

    # element = pixel_position_array[0]
    calc_result_array_index = 0
    for element in pixel_position_array:
        calc_result_array_short[1, calc_result_array_index] = element.vertical
        calc_result_array_short[0, calc_result_array_index] = element.horizontal
        calc_result_array_index += 1

    # x = np.arange(0, 1, 0.05)
    # y = np.power(x, 2)

    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, 30, 1))
    ax.set_yticks(np.arange(0, 30, 1))
    # plt.scatter(x, y)
    plt.scatter(calc_result_array_short[0], calc_result_array_short[1])
    point1 = [x1, y1]
    point2 = [x2, y2]
    x_values = [point1[0], point2[0]]  # gather x-values
    y_values = [point1[1], point2[1]]  # gather y-values
    plt.plot(x_values, y_values)

    # plt.grid()
    plt.show()

    # plot pixels

    # define the size of the canvas
    Row = 50
    Cols = 50
    # create an image
    local_matrix_search = np.zeros((Row, Cols))

    # draw the pixels on the canvas
    for element in pixel_position_array:
        local_matrix_search[element.vertical][element.horizontal] = 1
        calc_result_array_index += 1

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
    plt.show()

    # ax1.imshow(calc_result_array, interpolation='nearest', cmap=cm.Greys_r)
    # plt.show()
