import csv
# Mapper function
def mapper(file_path):
    """
    Reads the CSV file and emits (passenger_id, 1) for each row.
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            passenger_id = row[0]  # Extract passenger ID (first column)
            yield passenger_id, 1
