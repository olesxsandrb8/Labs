import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_csv_content(data):
    if data:
        for row in data:
            print(','.join(row))

def search_and_save_results(data, search_countries, output_file):
    if data:
        results = [row for row in data if row[2] in search_countries]
        if results:
            try:
                with open(output_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(results)
                print(f"Results saved to {output_file}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No matching results found.")

input_file_path = 'data_file.csv'

csv_data = read_csv(input_file_path)
display_csv_content(csv_data)

search_countries = input("Enter countries (comma-separated) to search: ").split(',')
output_file_path = 'search_results.csv'

search_and_save_results(csv_data, search_countries, output_file_path)
