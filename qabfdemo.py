import bretschneidersformula as bf


def main():

    print("---------------------------------------")
    print("| codedrome.com                       |")
    print("| Calculating Areas of Quadrilaterals |")
    print("| With Bretschneider's Formula        |")
    print("---------------------------------------\n")

    quadrilateral_1 = {
        "sides": [8, 17, 12, 9],
        "opposite_angles_degrees": [61.92751306, 90.0],
        # OR
        # "opposite_angles_degrees": [143.1301024, 64.94238459],
        "area": 0
    }

    quadrilateral_1["area"] = bf.calculate_area(quadrilateral_1["sides"],
                                                                   quadrilateral_1["opposite_angles_degrees"])

    print(quadrilateral_1)

    #------------------------------------------------------

    quadrilateral_2 = {
        "sides": [9, 15, 5, 13],
        "opposite_angles_degrees": [53.13010235, 67.38013505],
        # OR
        # "opposite_angles_degrees": [112.6198649, 126.8698976],
        "area": 0
    }

    quadrilateral_2["area"] = bf.calculate_area(quadrilateral_2["sides"],
                                                                   quadrilateral_2["opposite_angles_degrees"])

    print(quadrilateral_2)


if __name__ == "__main__":

    main()