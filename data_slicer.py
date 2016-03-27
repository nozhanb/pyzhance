	
			
def data_slicer(input_file = None, column_number = None, 
						outputPath = os.getcwd(), input_format = None, 
						output_format = None, output_file = None):
	import numpy
	import datetime
	# name of the file
	# name/number of the column(s)
	# format to read (format of the input data)
	# format to convert to (format of the output data)
	# name of the file to be written to (the output file)
	
	for name in input_file:
		for column in column_number:
			numpy.genfromtxt(fname = input_file, usecols = column_number)
	
