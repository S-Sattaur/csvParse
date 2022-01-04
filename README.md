# csvParse

This is a Python script that takes a large CSV file containing data scraped from Wikiaves, which is a Brazilian website used to save photos of different species, and sorts them into a sorted list of ID values before constructing another file containing all the missing values from the dataset so that those entries can be scraped to complete the dataset.

# Usage

First, combine all of the CSV files with the data into one large CSV file by using the cat command in Bash. The exact command is as follows: 

```bash
cat *.csv > combined.csv
```

The sortWrite.py script then reads in the combined.csv file and sorts it into sortedList.csv, before detecting any missing values from the overall dataset and constructing missingValues.csv to be used for targeted scraping. 
