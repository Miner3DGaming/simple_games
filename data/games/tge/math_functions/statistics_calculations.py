from math import sqrt, log2

from .. import NUMPY
NUMPY = False
if NUMPY:
    from numpy import corrcoef as np_corrcoef


def average_grade(grades: list) -> float:
    """
    Calculate the average grade from a list of grades.

    Parameters:
    grades (list): A list of numerical grades.

    Returns:
    float: The average grade calculated by summing all grades and dividing by the number of grades.
    """
    return sum(grades) / len(grades)


def median_grade(grades: list) -> float:
    """
    Calculate the median grade from a list of grades.

    Parameters:
    grades (list): A list of numerical grades.

    Returns:
    float: The median grade from the provided list of grades.
    """
    return sorted(grades)[len(grades) // 2]


def mode_grade(grades: list) -> float:
    """
    Calculate the mode (most frequent grade) from a list of grades.

    Parameters:
    grades (list): A list of numerical grades.

    Returns:
    float: The mode (most frequent grade) from the input list of grades.
    """
    return max(set(grades), key=grades.count)


def standard_deviation(grades: list) -> float:
    """
    Calculate the standard deviation of a list of grades.

    Parameters:
        grades (list): A list of numerical grades for which to calculate the standard deviation.

    Returns:
        float: The standard deviation of the grades.
    """
    return sqrt(sum([(x - average_grade(grades)) ** 2 for x in grades]) / len(grades))

def median(grades: list) -> float:
    """
    Calculate the median value of a list of grades.

    Parameters:
        grades (list): A list of numeric grades.

    Returns:
        float: The median grade of the given grades.
    """
    return sorted(grades)[len(grades) // 2]

def median_absolute_deviation(data):
    """
    Calculate the Median Absolute Deviation (MAD) of a given dataset.

    The Median Absolute Deviation (MAD) is a robust measure of statistical dispersion
    that calculates the median of the absolute deviations from the median.

    Parameters:
    data (array-like): Input data for which MAD is to be calculated.

    Returns:
    float: The Median Absolute Deviation (MAD) of the input data.
    """
    median_a = median(data)
    deviations = abs(data - median_a)
    mad = median(deviations)
    return mad

if NUMPY:
    def correlation(data1, data2):
        """
        Calculate the correlation coefficient between two sets of data.

        Parameters:
        data1 (array-like): The first set of data.
        data2 (array-like): The second set of data.

        Returns:
        float: The correlation coefficient between data1 and data2.
            The correlation coefficient ranges from -1 to 1, where:
            - 1 indicates a perfect positive linear relationship,
            0 indicates no linear relationship, and
            1 indicates a perfect negative linear relationship.
        """
        return np_corrcoef(data1, data2)[0][1]

def calculate_entropy(grades: list) -> float:
    """
    Calculate the entropy of a given list of grades.

    Entropy is a measure of disorder or uncertainty in a dataset. In the context
    of grades, higher entropy indicates a more diverse distribution of grades.

    Parameters:
    grades (list): A list of numerical values representing grades.

    Returns:
    float: The entropy of the grade distribution. The entropy is calculated using
    the formula: entropy = -sum(p(x) * log2(p(x))) for each grade x in the list,
    where p(x) is the proportion of occurrences of grade x in the dataset.
    """
    return sum(x * log2(x) for x in grades)

def median_absolute_error(grades: list) -> float:
    """
    Calculate the Median Absolute Error (MedAE) for a set of grades.

    The Median Absolute Error (MedAE) is a robust metric to evaluate the accuracy
    of predictions by calculating the median of the absolute differences between each
    grade and the median grade of the given set.

    Parameters:
    grades (list): A list of numerical grades or values.

    Returns:
    float: The Median Absolute Error (MedAE) calculated for the input grades.
    """
    return median(abs(x - median_grade(grades)) for x in grades)
