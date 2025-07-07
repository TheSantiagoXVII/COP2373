import csv
#Function made to run the grades made in the other functions.
def read_and_display_grades():
    filename = 'grades.csv'

    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Format the header and the data.
    header = rows[0]
    data = rows[1:]

    # Format the columns of the grades.
    col_widths = [len(h) for h in header]
    for row in data:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Print header
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(header))
    separator = "-+-".join('-' * col_widths[i] for i in range(len(header)))
    print(header_line)
    print(separator)

    # Print rows
    for row in data:
        row_line = " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row))
        print(row_line)
#call the main function.
if __name__ == "__main__":
    read_and_display_grades()
