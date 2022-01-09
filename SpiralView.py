# import only system from os
import copy
from os import system
# import time to show output for some time period
from time import sleep

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from SpiralIII import *

sleep(1)

import unittest


class TestUser(unittest.TestCase):

    def test_spiral_matrix(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        Row = 200
        Cols = 200
        current_position_row = int(Row / 2)
        current_position_cols = int(Cols / 2)
        delta_radius = 12
        step_size = 8
        fig = plt.figure()
        ax1 = fig.add_subplot(121)

        local_matrix = np.zeros((Row, Cols))
        result = SearchSolution().spiral_matrix(Row, Cols, current_position_row, current_position_cols, step_size,
                                                delta_radius)
        for element in result:
            # cls()
            if 0 <= element[0] < Row and 0 <= element[1] < Cols:  # inside the boundary of the matrix
                local_matrix[element[0]][element[1]] = 1
            # print(local_matrix)
            # sleep(1)

        # Bilinear interpolation - this will look blurry
        ax1.imshow(local_matrix, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()

    def test_spiral_matrix_search_tolerance_5_step_size_1_delta_radius_1(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        tolerance: int = 5
        step_size = 1
        delta_radius = 1

        # test new API for spiral matrix search
        start = PixelPosition()
        start.vertical = tolerance
        start.horizontal = tolerance
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        local_matrix_search = np.zeros((2 * tolerance, 2 * tolerance))

        calc_result_array = np.zeros((2, (2 * tolerance) * (2 * tolerance)))
        calc_result_array_index = 0
        cur_position = PixelPosition()
        pixel_position_array = []
        result = SearchSolution().spiral_matrix_search(start, step_size, delta_radius, tolerance)

        for element in result:
            # cls()
            if 0 <= element.vertical < 2 * tolerance and 0 <= element.horizontal < 2 * tolerance:  # inside the boundary of the matrix
                local_matrix_search[element.horizontal][element.vertical] = 1
                calc_result_array[0, calc_result_array_index] = element.vertical
                calc_result_array[1, calc_result_array_index] = element.horizontal
                calc_result_array_index += 1

                cur_position.vertical = element.vertical
                cur_position.horizontal = element.horizontal
                pixel_position_array.append(copy.deepcopy(cur_position))

            # print(local_matrix_search)
            # sleep(1)

        print(calc_result_array)
        #np.savetxt("res1.csv", calc_result_array, fmt='%i', delimiter=",")
        a = np.loadtxt('tolerance_5_step_size_1_delta_radius_1.csv', delimiter=',')
        if np.array_equal(calc_result_array, a):
            print("test pass")
        else:
            print("test fail")
        ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()

    def test_spiral_matrix_search_tolerance_5_step_size_2_delta_radius_1(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        tolerance: int = 5
        step_size = 2
        delta_radius = 1

        # test new API for spiral matrix search
        start = PixelPosition()
        start.vertical = tolerance
        start.horizontal = tolerance
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        local_matrix_search = np.zeros((2 * tolerance, 2 * tolerance))

        calc_result_array = np.zeros((2, (2 * tolerance) * (2 * tolerance)))
        calc_result_array_index = 0
        cur_position = PixelPosition()
        pixel_position_array = []
        result = SearchSolution().spiral_matrix_search(start, step_size, delta_radius, tolerance)

        for element in result:
            # cls()
            if 0 <= element.vertical < 2 * tolerance and 0 <= element.horizontal < 2 * tolerance:  # inside the boundary of the matrix
                local_matrix_search[element.horizontal][element.vertical] = 1
                calc_result_array[0, calc_result_array_index] = element.vertical
                calc_result_array[1, calc_result_array_index] = element.horizontal
                calc_result_array_index += 1

                cur_position.vertical = element.vertical
                cur_position.horizontal = element.horizontal
                pixel_position_array.append(copy.deepcopy(cur_position))

            # print(local_matrix_search)
            # sleep(1)

        print(calc_result_array)
        #np.savetxt("'tolerance_5_step_size_2_delta_radius_1.csv'", calc_result_array, fmt='%i', delimiter=",")
        a = np.loadtxt('tolerance_5_step_size_2_delta_radius_1.csv', delimiter=',')
        if np.array_equal(calc_result_array, a):
            print("test pass")
        else:
            print("test fail")
        ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()

    def test_spiral_matrix_search_tolerance_5_step_size_2_delta_radius_2(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        tolerance: int = 5
        step_size = 2
        delta_radius = 2

        # test new API for spiral matrix search
        start = PixelPosition()
        start.vertical = tolerance
        start.horizontal = tolerance
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        local_matrix_search = np.zeros((2 * tolerance, 2 * tolerance))

        calc_result_array = np.zeros((2, (2 * tolerance) * (2 * tolerance)))
        calc_result_array_index = 0
        cur_position = PixelPosition()
        pixel_position_array = []
        result = SearchSolution().spiral_matrix_search(start, step_size, delta_radius, tolerance)

        for element in result:
            # cls()
            if 0 <= element.vertical < 2 * tolerance and 0 <= element.horizontal < 2 * tolerance:  # inside the boundary of the matrix
                local_matrix_search[element.horizontal][element.vertical] = 1
                calc_result_array[0, calc_result_array_index] = element.vertical
                calc_result_array[1, calc_result_array_index] = element.horizontal
                calc_result_array_index += 1

                cur_position.vertical = element.vertical
                cur_position.horizontal = element.horizontal
                pixel_position_array.append(copy.deepcopy(cur_position))

            # print(local_matrix_search)
            # sleep(1)

        print(calc_result_array)
        #np.savetxt('tolerance_5_step_size_2_delta_radius_2.csv', calc_result_array, fmt='%i', delimiter=",")
        a = np.loadtxt('tolerance_5_step_size_2_delta_radius_2.csv', delimiter=',')
        if np.array_equal(calc_result_array, a):
            print("test pass")
        else:
            print("test fail")
        ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()


    def test_spiral_matrix_search_tolerance_10_step_size_2_delta_radius_4(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        tolerance: int = 10
        step_size = 2
        delta_radius = 4

        # test new API for spiral matrix search
        start = PixelPosition()
        start.vertical = tolerance
        start.horizontal = tolerance
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        local_matrix_search = np.zeros((2 * tolerance, 2 * tolerance))

        calc_result_array = np.zeros((2, (2 * tolerance) * (2 * tolerance)))
        calc_result_array_index = 0
        cur_position = PixelPosition()
        pixel_position_array = []
        result = SearchSolution().spiral_matrix_search(start, step_size, delta_radius, tolerance)

        for element in result:
            # cls()
            if 0 <= element.vertical < 2 * tolerance and 0 <= element.horizontal < 2 * tolerance:  # inside the boundary of the matrix
                local_matrix_search[element.horizontal][element.vertical] = 1
                calc_result_array[0, calc_result_array_index] = element.vertical
                calc_result_array[1, calc_result_array_index] = element.horizontal
                calc_result_array_index += 1

                cur_position.vertical = element.vertical
                cur_position.horizontal = element.horizontal
                pixel_position_array.append(copy.deepcopy(cur_position))

            # print(local_matrix_search)
            # sleep(1)

        print(calc_result_array)
        #np.savetxt('tolerance_5_step_size_2_delta_radius_4.csv', calc_result_array, fmt='%i', delimiter=",")
        a = np.loadtxt('tolerance_10_step_size_2_delta_radius_4.csv', delimiter=',')
        if np.array_equal(calc_result_array, a):
            print("test pass")
        else:
            print("test fail")
        ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()


    def test_spiral_matrix_search_tolerance_10_step_size_3_delta_radius_4(self):
        cls = lambda: system('cls')
        sol = SearchSolution()
        tolerance: int = 10
        step_size = 3
        delta_radius = 4

        # test new API for spiral matrix search
        start = PixelPosition()
        start.vertical = tolerance
        start.horizontal = tolerance
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        local_matrix_search = np.zeros((2 * tolerance, 2 * tolerance))

        calc_result_array = np.zeros((2, (2 * tolerance) * (2 * tolerance)))
        calc_result_array_index = 0
        cur_position = PixelPosition()
        pixel_position_array = []
        result = SearchSolution().spiral_matrix_search(start, step_size, delta_radius, tolerance)

        for element in result:
            # cls()
            if 0 <= element.vertical < 2 * tolerance and 0 <= element.horizontal < 2 * tolerance:  # inside the boundary of the matrix
                local_matrix_search[element.horizontal][element.vertical] = 1
                calc_result_array[0, calc_result_array_index] = element.vertical
                calc_result_array[1, calc_result_array_index] = element.horizontal
                calc_result_array_index += 1

                cur_position.vertical = element.vertical
                cur_position.horizontal = element.horizontal
                pixel_position_array.append(copy.deepcopy(cur_position))

            # print(local_matrix_search)
            # sleep(1)

        print(calc_result_array)
        #np.savetxt('tolerance_5_step_size_2_delta_radius_4.csv', calc_result_array, fmt='%i', delimiter=",")
        a = np.loadtxt('tolerance_10_step_size_3_delta_radius_4.csv', delimiter=',')
        if np.array_equal(calc_result_array, a):
            print("test pass")
        else:
            print("test fail")
        ax1.imshow(local_matrix_search, interpolation='nearest', cmap=cm.Greys_r)
        plt.show()