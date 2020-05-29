# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image 
# is 4 bytes, write a method to rotate the image by 90 degrees counterclockwise.
# Can you do this in place?

from typing import List


def main():
    m = [[1]]
    rotate_matrix(m)
    print_matrix(m)
    m2 = [
        [1, 2], 
        [3, 4]
    ]
    rotate_matrix(m2)
    print_matrix(m2)
    m3 = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
    rotate_matrix(m3)
    print_matrix(m3)


def rotate_matrix(mat: List[List[int]]):
    n = len(mat)
    # rotate each square "layer", starting from outer layer and moving inward
    for i in range(n // 2):
        for j in range(n - 2 * i):
            # four-way swap matrix entries in layer in-place
            coords = [(i, j)]
            for k in range(1, 4):
                coords.append(rotate_coord(coords[k - 1][0], coords[k - 1][1], n))
            temp = mat[coords[3][0]][coords[3][1]]
            for k in reversed(range(1, 4)):
                mat[coords[k][0]][coords[k][1]] = mat[coords[k - 1][0]][coords[k - 1][1]]
            mat[coords[0][0]][coords[0][1]] = temp


def rotate_coord(x: int, y: int, n: int) -> (int, int):
    # find counterclockwise rotated coordinates in n-by-n matrix
    center = (n - 1) / 2
    x -= center
    y -= center
    x, y = -1 * y, x
    x += center
    y += center
    return int(x), int(y)


def print_matrix(m: List[List[int]]):
    for i in range(len(m)):
        print(m[i])
    print()


def checkeq(x, y):
    print("passed") if x == y else print("FAILED")


if __name__ == "__main__":
    main()
