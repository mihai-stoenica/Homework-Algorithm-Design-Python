from lobsters import generate_value_matrix, print_lobsters, print_lobsters_result
from datagenerator import generate_net_capacity, generate_no_of_lobsters, generate_lobsters


def main():
    # Generate random net capacity and number of lobsters
    net_capacity = generate_net_capacity()
    no_of_lobsters = generate_no_of_lobsters()

    # Generate the list of lobsters
    lobsters = generate_lobsters(no_of_lobsters)

    # Print net capacity and number of lobsters
    print(f"Net capacity: {net_capacity}\nTotal number of lobsters: {no_of_lobsters}\n")

    # Print each lobster's id, size, and value
    print_lobsters(lobsters)

    # Generate the value matrix
    matrix = generate_value_matrix(no_of_lobsters, net_capacity, lobsters)

    # Print the value matrix
    matrix.print_matrix()

    print("\n")

    # Get and print the maximum value possible using all the lobsters and the entire capacity
    max_value = matrix.get_matrix_value(no_of_lobsters, net_capacity)
    print(f"The maximum value: {max_value}")

    print("\n")

    # Print the lobsters used to achieve the maximum value
    print_lobsters_result(no_of_lobsters, net_capacity, lobsters)


if __name__ == "__main__":
    main()
