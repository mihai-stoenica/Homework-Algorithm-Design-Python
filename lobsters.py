class Lobster:
    def __init__(self, id, size, value):
        self.id = id
        self.size = size
        self.value = value

class Matrix:
    def __init__(self, no_rows, no_cols):
        self.no_rows = no_rows
        self.no_cols = no_cols
        self.matrix = [[0] * no_cols for _ in range(no_rows)]

    def set_matrix_value(self, row_index, column_index, element_value):
        self.matrix[row_index][column_index] = element_value

    def get_matrix_value(self, row_index, column_index):
        return self.matrix[row_index][column_index]

    def print_matrix(self):
        print("\n === Matrix === \n")
        for row in self.matrix:
            print(' '.join(map(str, row)))


def get_max_value(val1, val2):
    return max(val1, val2)


def generate_value_matrix(no_of_lobsters, net_capacity, lobsters):
    matrix = Matrix(no_of_lobsters + 1, net_capacity + 1)

    for i in range(matrix.no_rows):
        for j in range(matrix.no_cols):
            if i == 0 or j == 0:
                matrix.set_matrix_value(i, j, 0)
            else:
                if j < lobsters[i - 1].size:
                    matrix.set_matrix_value(i, j, matrix.get_matrix_value(i - 1, j))
                else:
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
    matrix = generate_value_matrix(no_of_lobsters, net_capacity, lobsters)

    i = no_of_lobsters
    j = net_capacity

    while i > 0 and j > 0:
        if matrix.get_matrix_value(i - 1, j) == matrix.get_matrix_value(i, j):
            i -= 1
        else:
            print(f"Id: {lobsters[i - 1].id} Size: {lobsters[i - 1].size} Value: {lobsters[i - 1].value}")
            j -= lobsters[i - 1].size
            i -= 1