import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display_html

# URL to scrape
url_to_scrape = 'https://trend.nl7za.com/%d8%b3%d8%a4%d8%a7%d9%84-%d9%88%d8%ac%d9%88%d8%a7%d8%a8/%d8%a7%d9%82%d9%88%d9%8a-%d8%a7%d8%b3%d8%a6%d9%84%d8%a9-%d8%af%d9%8a%d9%86%d9%8a%d8%a9-%d9%88%d8%a7%d8%ac%d8%a7%d8%a8%d8%aa%d9%87%d8%a7-%d9%85%d8%b9-%d8%a7%d9%84%d8%ae%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa/'
response = requests.get(url_to_scrape)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing questions and answers
table = soup.find('table')

# Extract rows from the table
rows = table.find_all('tr')

# Initialize lists to store questions, answers, and scores
questions = []
answers = []
scores = []

# Iterate through each row skipping the header row
for row in rows[1:]:
    # Extract columns (cells) from the row
    columns = row.find_all('td')

    # Extract question and answer
    question = columns[0].get_text(strip=True)
    answer = columns[1].get_text(strip=True)

    # Assign a relevance score (1 for correct, 0 for incorrect)
    # score = 1 if input(f"Is the answer to the question '{question}' ('{answer}') correct? (yes/no): ").lower() == 'yes' else 0
    score = float(input(f"Enter the score (between 0 and 10) for answer to the question '{question}' ('{answer}'): "))

    # Check if the entered score is within the valid range
    while score < 0 or score > 10:
        print("Invalid score. Please enter a score between 0 and 10.")
        score = float(input(f"Enter the score (between 0 and 10) for the question '{question}': "))

    # Append to lists
    questions.append(question)
    answers.append(answer)
    scores.append(score)

# Create a DataFrame
df = pd.DataFrame({'Question': questions, 'Answer': answers, 'Score': scores})

# Display the DataFrame as an HTML table
display_html(df, raw=True)

# Save the DataFrame to a CSV file
# df.to_csv('QuestAnsScore.csv', index=False)
# Save the DataFrame to a CSV file with utf-8-sig encoding
df.to_csv('QuestAnsScore.csv', index=False, encoding='utf-8-sig')

