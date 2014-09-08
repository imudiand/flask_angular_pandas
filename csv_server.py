import os
import sys
from wise_io import app
from pandas import DataFrame

def create_dataframe(input_file):
	return DataFrame.from_csv(input_file, index_col=False, sep=",")

def run_debug(input_file, query):
	app.config['df'] = create_dataframe(input_file)
	app.config['query'] = query
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

def runserver(input_file, query):
	run_debug(input_file, query)

if __name__ == '__main__':
	if len(sys.argv) == 3:
		runserver(sys.argv[1], sys.argv[2])
	elif len(sys.argv) < 3:
		print "Input file or query string not provided"
	else:
		print "Invalid program arguments"