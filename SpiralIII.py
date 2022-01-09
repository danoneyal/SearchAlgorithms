import itertools as itr
import math


class PixelPosition:
    vertical: int #y
    horizontal: int #x


class SearchSolution(object):

    @staticmethod
    def spiral_archimedean(offset_x: float, offset_y: float, factor: float, max_radius: int):
        smooth_factor = 20.0
        a = 0
        i: int = 0
        while i < max_radius:
            angle = i / smooth_factor * math.pi
            x = offset_x + (angle * factor + a) * math.cos(angle)  # dx  theta * cos(theta)
            y = offset_y + (angle * factor + a) * math.sin(angle)  # dy  theta * sin(theta)
            raduis = angle * factor + a
            i = i + 1
            yield x, y, raduis

    @staticmethod
    def spiral_matrix_search(start: PixelPosition, step_size: int, delta_radius: int, tolerance: int):
        current_position = PixelPosition()
        if delta_radius < step_size:  # delta radius must me bigger then the step size
            step_size = delta_radius
        if delta_radius % step_size != 0:
            step_size = step_size - delta_radius % step_size

        # list that defines the direction on movement
        # dirs = [(0, step_size), (step_size, 0), (0, -step_size), (-step_size, 0)]
        # writing notation :  (x=cols,y=row)
        dirs = [(step_size, 0), (0, step_size), (-step_size, 0), (0, -step_size)]
        current_position_cols = start.vertical
        current_position_row = start.horizontal
        break_value: bool = True
        steps = 1  # measure the amount of time the for loop will execute for each increment
        increment = delta_radius  # each 2 steps increment by delta_radius
        current_position.vertical = current_position_cols
        current_position.horizontal = current_position_row
        yield current_position  # current_position_row, current_position_cols  # keep track of the position

        # direction index that defines and correct direction , each step the direction is changed
        # using itertools
        dir_iter = itr.cycle(dirs)
        while break_value:
            direction = next(dir_iter)
            search_len: int = int(increment / step_size)
            for i in range(search_len):
                current_position_cols, current_position_row = current_position_cols + direction[
                    0], current_position_row + direction[1]
                x_distance = math.fabs(current_position_cols - start.vertical)
                y_distance = math.fabs(current_position_row - start.horizontal)
                if x_distance < tolerance and y_distance < tolerance:  # inside the tolerance
                    current_position.vertical = current_position_cols
                    current_position.horizontal = current_position_row
                    yield current_position
                    # yield current_position_row, current_position_cols
                else:
                    break_value = False
            if steps % 2 == 0:  # run the for loop twice for each increment size
                increment += delta_radius
            steps += 1
        current_position.vertical = current_position_cols
        current_position.horizontal = current_position_row
        yield current_position
        # yield current_position_row, current_position_cols

    @staticmethod
    def spiral_matrix(rows, cols, current_position_row, current_position_cols, step_size, delta_radius):
        """
        :type rows: int the number of rows in the matrix
        :type cols: int the number of cols in the matrix
        :type current_position_row: int the cols starting point in the matrix
        :type current_position_cols: int the raw starting point in the matrix
        :type step_size: int the step size
        :type delta_radius: int the radius of the loop
        :rtype: List[List[int]] the current position in the matrix
        """
        # writing notation :  (row,cols)
        # list that defines the direction on movement
        # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if delta_radius < step_size:  # delta radius must me bigger then the step size
            step_size = delta_radius
        if delta_radius % step_size != 0:
            step_size = step_size - delta_radius % step_size

        dirs = [(0, step_size), (step_size, 0), (0, -step_size), (-step_size, 0)]

        # direction index that defines and correct direction , each step the direction is changed
        break_value: bool = True
        total = rows * cols  # keep track of the total to know that we are done
        steps = 1  # measure the amount of time the for loop will execute for each increment
        increment = delta_radius  # each 2 steps increment by delta_radius
        yield current_position_row, current_position_cols  # keep track of the position
        counter = 1
        dir_iter = itr.cycle(dirs)  # (dir_idx + 1) % 4  # look for itertools
        # using itertools

        while break_value:  # counter < total:
            direction = next(dir_iter)
            len: int = int(increment / step_size)
            for i in range(len):
                current_position_row, current_position_cols = current_position_row + direction[
                    0], current_position_cols + direction[1]
                if 0 <= current_position_row < rows and 0 <= current_position_cols < cols:  # inside the boundary of the matrix
                    # counter += step_size
                    yield current_position_row, current_position_cols
                    counter += 1
                else:
                    break_value = False
            if steps % 2 == 0:  # run the for loop twice for each increment size
                increment += delta_radius
            steps += 1
        yield current_position_row, current_position_cols
