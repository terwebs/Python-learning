import os
import csv
import argparse


# Get users arguments using argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", required=True,
                    help="csv input file(with extension)", type=str)
parser.add_argument("-o", "--output_file", required=True,
                    help="csv output file (without extension)", type=str)
parser.add_argument("-r", "--row_limit", required=True,
                    help="row limit to split csv at", type=int)
args = parser.parse_args()
	
chunks = []
file_rows = [] 

def validate_file(file_name):
        # return True if file name exists
        return os.path.exists(file_name)

def file_reader(file_name):
        with open(file_name, "rb") as my_file:
                my_file_reader = csv.reader(my_file)
                # add the rows form the file opened
                for row in my_file_reader:
                        file_rows.append(row)

def validate_rows(file_name, row_split):
        if len(file_rows[1:]) >= row_split: # excludes the header
                return True

def split_row(row_split):
        row_start = 1
        row_end = row_split

        for chunk in range(len(file_rows)/row_split): # number of files depending on the row limit
                chunks.append([])
                chunks[chunk].extend(file_rows[row_start: row_end + 1]) # add segment of rows
                row_start += row_split
                row_end += row_split

def file_writer(output_name):
        for chunk in chunks: # create the csv for each chunk
                with open("{}-{}.csv".format(output_name, chunks.index(chunk)), "wb") as my_output_file:
                        my_file_writer = csv.writer(my_output_file)
                        my_file_writer.writerow(file_rows[0])
                        my_file_writer.writerows(chunk)

def csv_split(args):
        file_name = args.input_file
        row_split = args.row_limit
        output_name = args.output_file

        if not validate_file(file_name) == True:
                print "File does not exist"
                return None

        file_reader(file_name)

        if not validate_rows(file_name, row_split) == True:
                print "Row limit needs to be <= {}".format(len(file_rows[1:]))
                return None

        split_row(row_split)
        file_writer(output_name)

csv_split(args)
                
                

        
        
        
                
                                






        
