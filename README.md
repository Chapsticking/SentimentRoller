# Sentiment Analysis on Text Data

This Python script performs sentiment analysis on textual data using the TextBlob library. It reads data from a CSV file, calculates sentiment scores for each entry, exports the results, and visualizes the distribution of sentiment scores as a bell curve.

## Prerequisites

Before you can run this script, you need to have Python installed on your system along with the following Python libraries:
- pandas
- numpy
- matplotlib
- textblob

You can install these libraries using pip:

$ pip install -r requirements.txt

## Input Data Format

The script expects a CSV file named "Overall_Sentiment_Data_All_Data.csv" by default. This file should contain a column labeled 'Column1.data.body' which holds the text to be analyzed for sentiment.

## Output

The script will generate a CSV file named "Sentiment_Analysis_Results.csv" containing the original data along with a new 'Sentiment' column that holds the sentiment score for each text. Scores range from -1 (very negative) to 1 (very positive), with 0 being neutral.

Additionally, a plot titled 'Sentiment Analysis Bell Curve' will be displayed, showing the distribution of sentiment scores across the dataset. The plot includes lines indicating the average, lowest, and highest sentiment scores.

## Running the Script

To run the script, simply navigate to the directory containing the script and input data file, and execute the script using Python:

python main.py

You can customize the input and output CSV filenames by modifying the `csv_file` and `output_csv` variables in the script.

This script is released under the MIT License. Feel free to use it or modify it as per your needs.