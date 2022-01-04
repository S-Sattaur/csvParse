import csv

def key(a):
  return int(a[0])

def extract(lst):
  return [int(item[0]) for item in lst]

with open("combined.csv", 'r') as f:
  csv_reader = csv.reader(f, delimiter=',' )
  rowList = list(csv_reader)
  rowList.sort(key=key)

with open("sortedList.csv", 'w') as sortedFile: 
  csv_writer = csv.writer(sortedFile, delimiter=',')
  csv_writer.writerows(rowList)
  
  numList = extract(rowList) 
  res = [ele for ele in range(numList[-1]+1) if ele not in numList]
  
with open("missingValues.csv", 'w') as mV:
  csv_writer = csv.writer(mV, delimiter=',')
  csv_writer.writerow(res) 
