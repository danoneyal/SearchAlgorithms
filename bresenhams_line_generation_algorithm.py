import copy
import math

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np


# insert the coordinate to a list
# plot a matrix
# draw the pixels list on the matrix
# plot a straight line calculated using math equations

class PixelPosition:
    vertical: int  # y
    horizontal: int  # x


tolerance = 50
calc_result_array = np.zeros((2, tolerance))

# insert coordinate into PixelPosition
cur_position = PixelPosition()
pixel_position_array = []


# class BresenhamsLineGenerationAlgorithm:

# function for line generation
def bresenham(x1, y1, x2, y2, step_size=1):
    positive = 0
    negative = 1
    dirs_x = [step_size, -step_size]
    dirs_y = [step_size, -step_size]

    # check if abs(x2-x1) == 0
    calc_result_array_index = 0

    run = x2 - x1
    if run == 0:
        if y2 < y1:
            y1, y2 = (y2, y1)
        for y in range(y1, y2 + 1):
            cur_position.vertical = y
            cur_position.horizontal = x1
            calc_result_array[1, calc_result_array_index] = cur_position.vertical
            calc_result_array[0, calc_result_array_index] = cur_position.horizontal
            calc_result_array_index += 1

    # check the max distance
    if math.fabs(x2 - x1) > math.fabs(y2 - y1):
        # calc_result_array_index = 0
        m_new = 2 * (y2 - y1)
        slope_error_new = m_new - (x2 - x1)

        y = y1
        for x in range(x1, x2 + 1):

            cur_position.vertical = y
            cur_position.horizontal = x
            calc_result_array[1, calc_result_array_index] = cur_position.vertical
            calc_result_array[0, calc_result_array_index] = cur_position.horizontal
            calc_result_array_index += 1

            print("(", x, ",", y, ")\n")

            # Add slope to increment angle formed
            slope_error_new = slope_error_new + m_new

            # Slope error reached limit, time to
            # increment y and update slope error.
            if (slope_error_new >= 0):
                y = y + 1
                slope_error_new = slope_error_new - 2 * (x2 - x1)

            pixel_position_array.append(copy.deepcopy(cur_position))
    else:
        # calc_result_array_index = 0
        m_new = math.fabs(2 * (x2 - x1))
        slope_error_new = m_new - math.fabs(x2 - x1)

        x = x1
        if y1 > y2:
            y1, y2 = y2, y1
        for y in reversed(range(y1, y2 + 1)):
            cur_position.vertical = y
            cur_position.horizontal = x
            calc_result_array[1, calc_result_array_index] = cur_position.vertical
            calc_result_array[0, calc_result_array_index] = cur_position.horizontal
            calc_result_array_index += 1

            print("(", x, ",", y, ")\n")

            # Add slope to increment angle formed
            slope_error_new = slope_error_new + m_new

            # Slope error reached limit, time to
            # increment y and update slope error.
            if (slope_error_new >= 0):
                x = x + dirs_x[negative]
                slope_error_new = slope_error_new - math.fabs(2 * (y2 - y1))

            pixel_position_array.append(copy.deepcopy(cur_position))

    use_for_break_point = 0


# driver function
x1 = 34
y1 = 34
x2 = 10
y2 = 2

bresenham(x1, y1, x2, y2)
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
