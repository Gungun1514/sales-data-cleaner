# sales-data-cleaner
CSV to JSON ETL mini project 
# Sales Data Cleaner – CSV to JSON ETL
# 1. Project Title & Goal:
Sales Data Cleaner is a Python script that cleans messy CSV sales data, removes duplicates, converts USD prices to INR, and generates a clean JSON report.
---
# 2. Setup Instructions
#Requirements
- Python 3.x installed

#Commands to Run
The files `main.py` and `sales.csv` are in the same folder.
Open terminal / CMD in that folder and run:

'''bash'''
python main.py

# 3. The Logic (How I thought):
Why did you choose this approach?

I used Python’s built-in csv and json modules because they are lightweight, do not require any external libraries, and are perfect for simple ETL tasks.

The flow of the program is:
Read data from CSV file
Remove $ symbols and quotes
Convert price to float
Remove duplicate rows based on Product and Price
Convert USD to INR using rate 1 USD = 83 INR
Save the cleaned data into a JSON file

This approach keeps the solution simple and easy to run locally.

# What was the hardest bug you faced, and how did you fix it?
The main issue occurred when the CSV file contained a header row (Price), which caused a ValueError while converting to float.

Fix:
I removed the header row from the CSV file so that only numeric values are processed, which resolved the error.


# 4.Screenshot of output:
![Output](output.png)

# 5.Future Improvements: 
If I had 2 more days, I would:

Use Pandas for faster data processing
Add proper input validation and error handling
Build a small UI to upload CSV and download JSON
Support multiple currency conversions

