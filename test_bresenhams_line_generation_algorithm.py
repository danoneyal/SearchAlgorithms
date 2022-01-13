import bresenhams_line_generation_algorithm as bl
from bresenhams_line_generation_algorithm import PixelPosition
import unittest


# 12 test

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.start_position = PixelPosition()
        self.end_position = PixelPosition()

    # m slope is infinite
    def test_line_search__delta_x_zero__positive_y_direction(self):  #
        x1 = 45
        y1 = 45
        x2 = 45
        y2 = 1
        self.start_position.vertical = y1
        self.start_position.horizontal = x1
        self.end_position.vertical = y2
        self.end_position.horizontal = x2

        bl.BresenhamsLineGenerationAlgorithm().bresenham(start_position=self.start_position,
                                                         end_position=self.end_position)

    def test_line_search__delta_x_zero__negative_y_direction(self):  #
        pass

    # m slope is zero
    def test_line_search__delta_y_zero__positive_x_direction(self):  #
        pass

    def test_line_search__delta_y_zero__negative_x_direction(self):  #
        pass

    # delta_y_smaller_then_delta_x -1<m<1,abs(m)<1
    def test_line_search__delta_y_smaller_then_delta_x__positive_x_positive_y_direction(
            self):  # -1<m<1, abs(m)<1, x1<x2 , y1<y2
        pass

    def test_line_search__delta_y_smaller_then_delta_x__positive_x_negative_y_direction(
            self):  # -1<m<1, abs(m)<1,x1<x2 , y1>y2
        pass

    def test_line_search__delta_y_smaller_then_delta_x__negative_x_positive_y_direction(
            self):  # -1<m<1, abs(m)<1,x1>x2 , y1<y2
        pass

    def test_line_search__delta_y_smaller_then_delta_x__negative_x_negative_y_direction(
            self):  # -1<m<1, abs(m)<1, x1>x2 , y1>y2
        pass

    # delta_y_greater_then_delta_x -1<m<-1, abs(m)>1
    def test_line_search__delta_y_greater_then_delta_x__positive_x_positive_y_direction(
            self):  # -1<m<-1, abs(m)>1, x1<x2 , y1<y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__positive_x_negative_y_direction(
            self):  # -1<m<-1, abs(m)>1, x1<x2 , y1>y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__negative_x_positive_y_direction(
            self):  # -1<m<-1, abs(m)>1, x1>x2 , y1<y2
        pass

    def test_line_search__delta_y_greater_then_delta_x__negative_x_negative_y_direction(
            self):  # -1<m<-1, abs(m)>1, x1>x2 , y1>y2
        pass
