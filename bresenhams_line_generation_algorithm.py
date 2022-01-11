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


class BresenhamsLineGenerationAlgorithm(object):

    @staticmethod
    def bresenham(x1, y1, x2, y2, step_size=1):
        positive = 0
        negative = 1
        dirs_x = [step_size, -step_size]
        dirs_y = [step_size, -step_size]

        # check if abs(x2-x1) == 0
        calc_result_array_index = 0

        # define the direction of the line
        step_size_y = dirs_y[positive]
        step_size_x = dirs_x[positive]
        if y2 < y1:
            step_size_y = dirs_y[negative]
        if x2 < x1:
            step_size_x = dirs_x[negative]

        # start the Alg
        run = x2 - x1
        if run == 0:
            for y in range(y1, y2 + 1, step_size_y):
                cur_position.vertical = y
                cur_position.horizontal = x1
                # yield cur_position # remove this remark to create a generator

                # for test only
                calc_result_array[1, calc_result_array_index] = cur_position.vertical
                calc_result_array[0, calc_result_array_index] = cur_position.horizontal
                calc_result_array_index += 1

        # check the max distance
        if math.fabs(x2 - x1) > math.fabs(y2 - y1):
            m_new = 2 * (y2 - y1)
            slope_error_new = m_new - (x2 - x1)

            y = y1
            for x in range(x1, x2 + 1, step_size_x):
                cur_position.vertical = y
                cur_position.horizontal = x
                # yield cur_position # remove this remark to create a generator

                # for test only
                calc_result_array[1, calc_result_array_index] = cur_position.vertical
                calc_result_array[0, calc_result_array_index] = cur_position.horizontal
                calc_result_array_index += 1
                print("(", x, ",", y, ")\n")

                # Add slope to increment angle formed
                slope_error_new = slope_error_new + m_new

                # Slope error reached limit, time to
                # increment y and update slope error.
                if (slope_error_new >= 0):
                    y = y + step_size_y
                    slope_error_new = slope_error_new - 2 * (x2 - x1)

                pixel_position_array.append(copy.deepcopy(cur_position))
        else:
            # calc_result_array_index = 0
            m_new = math.fabs(2 * (x2 - x1))
            slope_error_new = m_new - math.fabs(x2 - x1)

            x = x1
            for y in range(y1, y2 + 1, step_size_y):
                cur_position.vertical = y
                cur_position.horizontal = x
                # yield cur_position # remove this remark to create a generator

                # for test only
                calc_result_array[1, calc_result_array_index] = cur_position.vertical
                calc_result_array[0, calc_result_array_index] = cur_position.horizontal
                calc_result_array_index += 1

                print("(", x, ",", y, ")\n")

                # Add slope to increment angle formed
                slope_error_new = slope_error_new + m_new

                # Slope error reached limit, time to
                # increment y and update slope error.
                if (slope_error_new >= 0):
                    x = x + step_size_x
                    slope_error_new = slope_error_new - math.fabs(2 * (y2 - y1))

                pixel_position_array.append(copy.deepcopy(cur_position))

        use_for_break_point = 0

