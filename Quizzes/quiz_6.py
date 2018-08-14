# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by Ragavendran Lakshminarasimhan and Eric Martin for COMP9021

from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y
            
    # Possibly define other methods
    def equals(self, p):
        if p is None:
            raise PointError('Need a point.')
        else:
            return self.x == p.x and self.y == p.y

    def calculate_distance_btw_points(self, p):
        if p is None:
            raise PointError('Need a point.')
        else:
            return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):        
        # Replace pass above with your code
        if not self.__valid_triangle(point_1, point_2, point_3):
            raise TriangleError('Incorrect input, triangle not created.')        
        self.__point_1 = point_1
        self.__point_2 = point_2
        self.__point_3 = point_3
        self.perimeter = self.__calculate_perimeter_triangle()
        self.area = self.__calculate_area_triangle()
       
    def change_point_or_points(self, *, point_1 = None, point_2 = None, point_3 = None):        
        # Replace pass above with your code
        tmp_point_1 = self.__point_1 if point_1 is None else point_1
        tmp_point_2 = self.__point_2 if point_2 is None else point_2
        tmp_point_3 = self.__point_3 if point_3 is None else point_3
        if not self.__valid_triangle(tmp_point_1, tmp_point_2, tmp_point_3):
            print('Incorrect input, triangle not modified.')    
        else:                    
            self.__point_1 = tmp_point_1
            self.__point_2 = tmp_point_2
            self.__point_3 = tmp_point_3
            self.perimeter = self.__calculate_perimeter_triangle()
            self.area = self.__calculate_area_triangle()

    # Possibly define other methods
    def __valid_triangle(self, point_1, point_2, point_3):
        if point_1 is None or point_2 is None or point_3 is None:
            return False
        if point_1.equals(point_2) or point_1.equals(point_3) or point_2.equals(point_3):
            return False
        side_1 = point_1.calculate_distance_btw_points(point_2)
        side_2 = point_1.calculate_distance_btw_points(point_3)
        side_3 = point_2.calculate_distance_btw_points(point_3)
        return side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1

    def __calculate_perimeter_triangle(self):        
        self.__side_1 = self.__point_1.calculate_distance_btw_points(self.__point_2)
        self.__side_2 = self.__point_1.calculate_distance_btw_points(self.__point_3)
        self.__side_3 = self.__point_2.calculate_distance_btw_points(self.__point_3)
        return self.__side_1 + self.__side_2 + self.__side_3

    def __calculate_area_triangle(self):
        s = self.perimeter / 2
        return sqrt(s * (s - self.__side_1) * (s - self.__side_2) * (s - self.__side_3))
