import csv, json, sys, os

def csv2json(csv_input_filename, json_output_filename):

	csv_file = open(csv_input_filename, 'r')
	json_file = open(json_output_filename, 'w')

	reader = csv.reader(csv_file)
	field_names = tuple(next(reader))
	reader = csv.DictReader(csv_file, field_names)

	json_file.write('[')
	for row in reader:
	    json.dump(row, json_file)
	    json_file.write(',\n')
	json_file.seek(0,2)
	json_file.truncate()
	json_file.write(']')

args = sys.argv
csv2json(args[1], args[2])