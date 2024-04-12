from math import sqrt

from tge.math_functions.math_functions import get_pi

def volume_of_cuboid(length: int, width: int, height: int) -> int:
    return length * width * height

def volume_of_cube(side: int) -> int:
    return side ** 3

def volume_of_sphere(radius: int) -> int:
    return (4 / 3) * 3.14159 * (radius ** 3)

def volume_of_sphere_with_accuracy(radius: float, accuracy: int) -> float:
    return (4 / 3) * get_pi(accuracy) * (radius ** 3)

def volume_of_cylinder(radius: int, height: int) -> int:
    return (3.14159 * (radius ** 2) * height)

def volume_of_cylinder_with_accuracy(radius: float, height: float, accuracy: int) -> float:
    return (get_pi(accuracy) * (radius ** 2) * height)

def area_of_square(side: int) -> int:
    return side ** 2

def area_of_rectangle(length: int, width: int) -> int:
    return length * width

def area_of_circle(radius: int) -> int:
    return (3.14159 * (radius ** 2))

def area_of_circle_with_accuracy(radius: float, accuracy: int) -> float:
    return (get_pi(accuracy) * (radius ** 2))

def area_of_trapezoid(base_length: int, base_width: int, height: int) -> int:
    return ((base_length + base_width) * height) / 2

def volume_of_pyramid(base_length: int, base_width: int, height: int) -> int:
    return (base_length * base_width * height) / 3

def linear_regression_slope(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2 - y1) / (x2 - x1)

def surface_area_of_cylinder(radius, height):
    # Calculate the slant height
    slant_height = sqrt(radius ** 2 + height ** 2)

    # Calculate the surface area
    surface_area = 3.14159 * radius * slant_height

    return surface_area

def surface_area_of_cylinder_with_accuracy(radius, height, accuracy):
    # Calculate the slant height
    slant_height = sqrt(radius ** 2 + height ** 2)

    # Calculate the surface area
    surface_area = get_pi(accuracy) * radius * slant_height

    return surface_area

def surface_area_of_sphere(radius):
    # Calculate the surface area
    surface_area = 4 * 3.14159 * (radius ** 2)

    return surface_area

def surface_area_of_sphere_with_accuracy(radius, accuracy):
    # Calculate the surface area
    surface_area = get_pi(accuracy) * (radius ** 2)

    return surface_area

def surface_area_of_cube(side_length):
    surface_area = 6 * (side_length ** 2)
    return surface_area

def surface_area_of_rectangle(length, width):
    surface_area = length * width
    return surface_area

def surface_area_of_cuboid(length, width, height):
    surface_area = 2 * (length * width + width * height + height * length)
    return surface_area

def volume_of_cone(radius, height):
    return (1 / 3) * 3.14159 * (radius ** 2) * height

def volume_of_cone_with_accuracy(radius, height, accuracy):
    return (1 / 3) * get_pi(accuracy) * (radius ** 2) * height

def surface_area_of_cone(radius, height):
    base_area = 3.14159 * radius**2
    side_area = 3.14159 * radius * sqrt(radius**2 + height**2)
    surface_area = base_area + side_area
    return surface_area

def surface_area_of_cone_with_accuracy(radius, height, accuracy):
    base_area = get_pi(accuracy) * radius**2
    side_area = get_pi(accuracy) * radius * sqrt(radius**2 + height**2)
    surface_area = base_area + side_area
    return surface_area

def area_of_ellipse(radius, height):
    return 3.14159 * radius * height

def area_of_ellipse_with_accuracy(radius, height, accuracy):
    return get_pi(accuracy) * radius * height

def area_of_oval(width, height):
    rectangle_area = width * height
    triangle_area = (width - height) * height / 2
    area = rectangle_area + triangle_area
    return area

def area_of_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

def calculate_distance_between_two_points(x: int, y: int) -> int:
    """
    Calculate the distance between two points using the Euclidean formula.
    
    :param x: An integer representing the x-coordinate of the first point.
    :param y: An integer representing the y-coordinate of the second point.
    :return: An integer representing the distance between the two points.
    """
    return ((x - y) ** 2) ** 0.5

def calculate_distance_between_three_points(x: int, y: int, z: int) -> int:
    """
    Calculate the distance between three points in a 3D space.
    
    :param x: An integer representing the x-coordinate of the first point.
    :param y: An integer representing the y-coordinate of the second point.
    :param z: An integer representing the z-coordinate of the third point.
    
    :return: An integer representing the distance between the three points.
    """
    return ((x - z) ** 2 + (y - z) ** 2) ** 0.5

def calculate_distance_between_four_points(x: int, y: int, z: int, a: int) -> float:
    """
    Calculates the distance between four points represented by their x, y, and z coordinates.
    
    :param x: An integer representing the first point.
    :param y: An integer representing the second point.
    :param z: An integer representing the third point.
    :param a: An integer representing the fourth point.
    
    :return: A float representing the distance between the four points.
    """
    return ((x - a) ** 2 + (y - a) ** 2 + (z - a) ** 2) ** 0.5

def calculate_distance_between_five_points(x: int, y: int, z: int, a: int, b: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - a) ** 2) ** 0.5

def calculate_distance_between_six_points(x: int, y: int, z: int, a: int, b: int, c: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2) ** 0.5

def calculate_distance_between_seven_points(x: int, y: int, z: int, a: int, b: int, c: int, d: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2 + (d - a) ** 2) ** 0.5

def calculate_distance_between_eight_points(x: int, y: int, z: int, a: int, b: int, c: int, d: int, e: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2 + (d - e) ** 2 + (e - a) ** 2) ** 0.5

def calculate_distance_between_nine_points(x: int, y: int, z: int, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2 + (d - e) ** 2 + (e - f) ** 2 + (f - a) ** 2) ** 0.5

def calculate_distance_between_ten_points(x: int, y: int, z: int, a: int, b: int, c: int, d: int, e: int, f: int, g: int) -> int:
    return ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2 + (d - e) ** 2 + (e - f) ** 2 + (f - g) ** 2 + (g - a) ** 2) ** 0.5

def calculate_distance_between_points(*points):
    if len(points) < 2:
        return 0.0  # Return 0 if there are less than two points
    
    total_distance = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance
    
    return total_distance

def vector_magnitude(vector: list) -> float:
    return sqrt(vector[0]**2 + vector[1]**2)

def hamming_distance(string1: str, string2: str) -> int:
    return sum(ch1 != ch2 for ch1, ch2 in zip(string1, string2))
