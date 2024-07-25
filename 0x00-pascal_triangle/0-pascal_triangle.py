def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle up to the nth row. An empty list
        is returned if n <= 0.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive input

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with a 1

        for j in range(1, i):
            # The value is the sum of the two values above
            #  it in the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the completed row to the triangle

    return triangle  # Return the completed Pascal's triangle
