import csv


class CsvReader:
    def __init__(self):
        pass

    def read_csv_to_hashmap(self, file_path):
        hashmap = {}
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')  # Set the delimiter to ;
            headers = next(csv_reader)  # Get the column headers
            for header in headers:
                hashmap[header] = []  # Initialize an empty array for each column
            for row in csv_reader:
                for i, value in enumerate(row):
                    hashmap[headers[i]].append(value)  # Append the value to the corresponding column
        return hashmap
    