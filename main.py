from lobsters import Lobster, Matrix, get_max_value, generate_value_matrix, print_lobsters, print_lobsters_result
from datagenerator import generate_net_capacity, generate_no_of_lobsters, generate_lobsters


def main():
    net_capacity = generate_net_capacity()
    no_of_lobsters = generate_no_of_lobsters()

    lobsters = generate_lobsters(no_of_lobsters)

    print(f"Net capacity: {net_capacity}\nTotal number of lobsters: {no_of_lobsters}\n")

    print_lobsters(lobsters)  # Printing each lobster's id, size, and value

    matrix = generate_value_matrix(no_of_lobsters, net_capacity, lobsters)

    matrix.print_matrix()  # Printing the matrix

    print("\n")

    max_value = matrix.get_matrix_value(no_of_lobsters, net_capacity)
    print(f"The maximum value: {max_value}")

    print("\n")
    print_lobsters_result(no_of_lobsters, net_capacity, lobsters)


if __name__ == "__main__":
    main()
