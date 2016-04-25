import sys

for line in sys.stdin:
  data = line.strip().split('.');
  if len(data) == 4:
	  if data[0].isdigit() and data[1].isdigit() and data[2].isdigit() and data[3].isdigit():
              print line
