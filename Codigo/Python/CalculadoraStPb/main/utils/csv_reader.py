import csv
class CsvReader:
    @staticmethod
    def read_csv_to_hashmap_w_headers(file_path, delimiter=';'):
        hashmap = {}
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=delimiter)  # Set the delimiter to ;
            headers = next(csv_reader)  # Get the column headers
            for header in headers:
                hashmap[header] = []  # Initialize an empty array for each column
            for row in csv_reader:
                for i, value in enumerate(row):
                    hashmap[headers[i]].append(value)  # Append the value to the corresponding column
        return hashmap

    @staticmethod
    def read_csv_to_array(file_path, delimiter=';'):
        array = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=delimiter)
            for row in csv_reader:
                array.append(row)
        return array

    @staticmethod
    def write_array_to_csv(file_path, array, delimiter=';'):
        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=delimiter)
            for row in array:
                csv_writer.writerow(row)

    @staticmethod
    def write_hashmap_to_csv(file_path, hashmap, delimiter=';'):
        headers = list(hashmap.keys())
        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=delimiter)
            csv_writer.writerow(headers)
            for i in range(len(hashmap[headers[0]])):
                row = []
                for header in headers:
                    row.append(hashmap[header][i])
                csv_writer.writerow(row)

    @staticmethod
    def get_headers_from_csv(file_path, delimiter=';'):
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter=delimiter)
            return next(csv_reader)