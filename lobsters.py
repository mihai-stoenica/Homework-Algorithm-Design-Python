
class Lobster:
    def __init__(self, id, size, value):
        self.id = id
        self.size = size
        self.value = value


class Matrix:
    def __init__(self, no_rows, no_cols):
        self.no_rows = no_rows
        self.no_cols = no_cols
        # Initialize a 2D list (matrix) with all values set to 0
        self.matrix = [[0] * no_cols for _ in range(no_rows)]

    def set_matrix_value(self, row_index, column_index, element_value):
        # Set the value at the specified row and column in the matrix
        self.matrix[row_index][column_index] = element_value

    def get_matrix_value(self, row_index, column_index):
        # Get the value at the specified row and column in the matrix
        return self.matrix[row_index][column_index]

    def print_matrix(self):
        # Print the entire matrix row by row
        print("\n === Matrix === \n")
        for row in self.matrix:
            print(' '.join(map(str, row)))


def get_max_value(val1, val2):
    return max(val1, val2)


def generate_value_matrix(no_of_lobsters, net_capacity, lobsters):
    # Generate a matrix with values representing the maximum value using the first i lobsters not exceeding size j
    matrix = Matrix(no_of_lobsters + 1, net_capacity + 1)

    for i in range(matrix.no_rows):
        for j in range(matrix.no_cols):
            if i == 0 or j == 0:
                # Initialize the first row and column with 0
                matrix.set_matrix_value(i, j, 0)
            else:
                if j < lobsters[i - 1].size:
                    # If the lobster's size is greater than the current capacity, use the value from the row above
                    matrix.set_matrix_value(i, j, matrix.get_matrix_value(i - 1, j))
                else:
                    # Otherwise, choose the maximum value between not using the lobster and using it
                    matrix.set_matrix_value(
                        i, j,
                        get_max_value(
                            matrix.get_matrix_value(i - 1, j),
                            lobsters[i - 1].value + matrix.get_matrix_value(i - 1, j - lobsters[i - 1].size)
                        )
                    )

    return matrix


def print_lobsters(lobsters):
    for lobster in lobsters:
        print(f"Id: {lobster.id} Size: {lobster.size} Value: {lobster.value}")


def print_lobsters_result(no_of_lobsters, net_capacity, lobsters):
    # Print the details of the lobsters used to achieve the maximum value
    matrix = generate_value_matrix(no_of_lobsters, net_capacity, lobsters)

    i = no_of_lobsters
    j = net_capacity

    while i > 0 and j > 0:
        if matrix.get_matrix_value(i - 1, j) == matrix.get_matrix_value(i, j):
            # If the current value is the same as the one above, the lobster was not used
            i -= 1
        else:
            # If the current value is different, the lobster was used
            print(f"Id: {lobsters[i - 1].id} Size: {lobsters[i - 1].size} Value: {lobsters[i - 1].value}")
            j -= lobsters[i - 1].size
            i -= 1
