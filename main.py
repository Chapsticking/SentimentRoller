import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load the CSV file into a DataFrame
csv_file = "Overall_Sentiment_Data_All_Data.csv"
data = pd.read_csv(csv_file)

# Assuming 'Column1.data.body' contains the text to analyze
texts = data['Column1.data.body']

# Define a function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(str(text))
    # Return polarity score (-1 to 1) where < 0 is negative, > 0 is positive, and = 0 is neutral
    return analysis.sentiment.polarity

# Apply sentiment analysis function to each text in the DataFrame
data['Sentiment'] = texts.apply(analyze_sentiment)

# Export the DataFrame with sentiment scores to a new CSV file
output_csv = "Sentiment_Analysis_Results.csv"
data.to_csv(output_csv, index=False)

# Calculate statistics
min_sentiment = data['Sentiment'].min()
max_sentiment = data['Sentiment'].max()
average_sentiment = data['Sentiment'].mean()

# Generate data for the bell curve
x = np.linspace(-1, 1, 100)
mu = average_sentiment
sigma = data['Sentiment'].std()
y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Plot the bell curve
plt.plot(x, y)

# Add lines for average, lowest, and highest sentiment scores
plt.axvline(x=average_sentiment, color='r', linestyle='--', label='Average Sentiment')
plt.axvline(x=min_sentiment, color='g', linestyle='--', label='Lowest Sentiment')
plt.axvline(x=max_sentiment, color='b', linestyle='--', label='Highest Sentiment')

# Add legend and labels
plt.legend()
plt.xlabel('Sentiment Score')
plt.ylabel('Probability Density')

# Show the plot
plt.title('Sentiment Analysis Bell Curve')
plt.grid(True)
plt.show()