import re

#, "Theorie.sc45": ["Methode", "PHILOSOPHIE"]

filenames = {"Arbeit.sc45": ["ARBEIT:"]}

export = {}

def make_pretty(line):
	return line.replace('\x00', '').replace('\x01', '').replace('\x02', '').replace('\x03', '').replace('\x04', '').replace('\x05', '').replace('\x06', '').replace('\x07', '').replace('\x08', '').replace('\x09', '').replace('\x10', '').replace('\x11', '').replace('\x12', '').replace('\x13', '').replace('\x14', '').replace('\x15', '')

for file in filenames:

	selectedFile = open(file, "r")

	lines = selectedFile.readlines()

	for category in filenames[file]:
		for i, line in enumerate(lines):
			if category in line:
				if line[0] == '\x00' and lines[i+2][0] == "D":
					export[make_pretty(line)] = {"body": make_pretty(lines[i+2])}
	print(export)