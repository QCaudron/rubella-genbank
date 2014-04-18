"""
Parses a multi-record .gb GenBank file and returns a CSV containing ID, date, 
and full sequence, having dropped records that contain given keywords.
"""

from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd

# Filename
filename = "sequence.gb"

# Keywords to avoid
avoid = ["vaccine"]

# Results
numAvoided = 0
ID = []
date = []
sequence = []



# Open the sequence file, iterate over records, and collect info
f = open(filename, "r")

for s in SeqIO.parse(f, "genbank") :
	for keyword in avoid :

		# If the metadata contains any of the keywords to avoid
		if keyword in " ".join("%r=%r" % entry for entry in s.annotations.iteritems()).lower() :
			numAvoided += 1
			continue


		ID.append(s.id)
		date.append(s.annotations["date"])
		sequence.append(s.seq)


	print s.annotations["gi"]



pd.DataFrame({"ID" : ID, "date" : date, "sequence" : sequence}).to_csv("sequences.csv", \
													header = ["ID", "date", "sequence"])



print "File parsed. Number of records dropped : %d" % numAvoided
