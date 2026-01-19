import math
from typing import List


def calculate_area(sides: List[float], opposite_angles_degrees: List[float]) -> float:

    '''
    Calculate the area of a quadrilateral using Bretschneider's Formula
    from the lengths of the sides and either pair of OPPOSITE angles.
    Arguments:-
    sides - list in format [a,b,c,d]
    opposite_angles_degrees - list in format [a1,a2]
    '''

    semiperimeter = sum(sides) / 2

    product_semiperimeter_minus_sides = (semiperimeter - sides[0]) * \
                                        (semiperimeter - sides[1]) * \
                                        (semiperimeter - sides[2]) * \
                                        (semiperimeter - sides[3])

    product_sides = math.prod(sides)

    sum_of_radians = math.radians(opposite_angles_degrees[0]) + math.radians(opposite_angles_degrees[1])

    cos_squared = ( math.cos(sum_of_radians / 2 ) ) **2

    area = math.sqrt(product_semiperimeter_minus_sides - product_sides * cos_squared)

    return area