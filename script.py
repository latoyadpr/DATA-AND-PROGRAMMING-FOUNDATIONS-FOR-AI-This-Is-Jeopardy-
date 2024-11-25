import pandas as pd
pd.set_option('display.max_colwidth', -1)


import pandas as pd

# Load the data into a DataFrame
jeopardy_data = pd.read_csv('jeopardy.csv')

# Display the first few rows
print(jeopardy_data.head())

# Display the column names
print(jeopardy_data.columns)

# Rename columns to remove leading spaces
jeopardy_data.rename(columns=lambda x: x.strip(), inplace=True)


def filter_questions(dataframe, words):
    # Convert words to lowercase for case-insensitive matching
    words = [word.lower() for word in words]
    
    # Filter the DataFrame
    filtered_data = dataframe[dataframe['Question'].apply(
        lambda question: all(word in question.lower() for word in words)
    )]
    
    return filtered_data

# Example usage
filtered_questions = filter_questions(jeopardy_data, ["King", "England"])
print(filtered_questions['Question'])


import re

def filter_questions(dataframe, words):
    # Convert words to lowercase for case-insensitive matching
    words = [word.lower() for word in words]
    
    # Create a regex pattern to match whole words
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words) + r')\b'
    
    # Filter the DataFrame
    filtered_data = dataframe[dataframe['Question'].apply(
        lambda question: all(re.search(pattern, question.lower()) for word in words)
    )]
    
    return filtered_data

# Example usage
filtered_questions = filter_questions(jeopardy_data, ["King", "England"])
print(filtered_questions['Question'])



def convert_value_to_float(value):
    # Remove dollar signs and commas
    value = value.replace('$', '').replace(',', '')
    # Convert "no value" to 0
    if value == "no value":
        return 0.0
    return float(value)

# Apply the conversion to the "Value" column
jeopardy_data['Float Value'] = jeopardy_data['Value'].apply(convert_value_to_float)

# Use the updated DataFrame in the filtering function
filtered_questions = filter_questions(jeopardy_data, ["King"])
average_value = filtered_questions['Float Value'].mean()

print(f"Average value of questions containing 'King': {average_value}")


def count_unique_answers(dataframe, words):
    # Filter the DataFrame for questions containing the specified words
    filtered_data = filter_questions(dataframe, words)
    
    # Count the unique answers
    answer_counts = filtered_data['Answer'].value_counts()
    
    return answer_counts

# Example usage
unique_answer_counts = count_unique_answers(jeopardy_data, ["King"])
print(unique_answer_counts)


