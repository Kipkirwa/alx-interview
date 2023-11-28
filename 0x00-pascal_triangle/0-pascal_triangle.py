def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            # Each element (except the first and last) is the sum of the elements above-left and above-right
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle

# Example usage:
result = pascal_triangle(5)
for row in result:
    print(row)

