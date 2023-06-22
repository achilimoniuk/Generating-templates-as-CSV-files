# generating_templates

## Description
The purpose of this code is to generate a CSV file with randomly created attributes. The code utilizes the lovs.py file, which contains a variety of attribute options for some of the attributes. For the remaining attributes, random values will be generated. 

## Files
- `generating.py`: The main file responsible for generating the attributes.
- `functions.py`: This file contains functions necessary for generating random dates, ensuring that the start time is always before the end date.
- `lovs.py`: This file contains lists of values available for some of the attributes.
## Requirements
To run this tool, make sure you have the following packages installed:
- pandas
- numpy
- random
- datetime

## Usage
Prepare the needed files with attributes specifications.
Run step1-compare_url_excel.py: Extract product information from the specified URL.Save the extracted information, including product name, price, and relevant attributes, as a CSV file.
Run step2_issue_classification.py:Compare the prices obtained from the URL with those from the Excel file.Identify any discrepancies or mismatches between the two sources.
Run step3-generate_table.py: Use the obtained results to generate tables in a Microsoft Word document (docx).
Run step4-creating_presentation.py: Utilize the obtained results to create a PowerPoint presentation.
