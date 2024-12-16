# Python Commands Summary

This document compiles Python commands and examples based on the lecture materials. Each section provides explanations and context to ensure clarity and usability. Detailed comments are provided for each command to ensure you understand the purpose and usage.

---

## Week 1: Introduction to Software, GitHub, and Markdown

### Setting Up the Environment
To create a Python environment and install essential packages, use the following commands:

```bash
# Add conda-forge channel and create a new environment
conda config --add channels conda-forge
conda create --name py_env pandas numpy matplotlib jupyterlab -y
```

- **`conda config`**: Adds the conda-forge channel to access a broader range of packages.
- **`conda create`**: Creates a new Python environment named `py_env` with essential libraries for data analysis and visualization, including:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical computations.
  - `matplotlib`: For creating static, animated, and interactive visualizations.
  - `jupyterlab`: A user-friendly interface for interactive coding and visualization.

This step ensures you have a dedicated and isolated environment for your project.

---

## Week 2: DataFrames & Visualizing Data with Plots

### Working with DataFrames
DataFrames are essential for handling tabular data. The following commands demonstrate common operations with detailed explanations:

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 40],
    'Height(cm)': [165, 170, 175, 160],
    'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Artist']
}
df = pd.DataFrame(data)
```
- **Creating a DataFrame**: `pd.DataFrame` converts a dictionary into a tabular format for analysis.

```python
# Sorting by a column
df_sorted = df.sort_values('Height(cm)', ascending=True)
```
- **Sorting**: `sort_values` arranges rows based on a column's values.

```python
# Selecting specific columns
selected_columns = df[['Name', 'Age']]
```
- **Selecting columns**: Extract only the columns you need.

```python
# Filtering rows where Age > 30
filtered_df = df[df['Age'] > 30]
```
- **Filtering rows**: Use logical conditions to subset data.

```python
# Adding a new column
df['Height(m)'] = df['Height(cm)'] / 100
```
- **Adding a column**: Create new variables based on existing data.

```python
# Grouping by a column and counting occurrences
age_group = df.groupby('Age').size()
```
- **Grouping**: Aggregate data by categories.

### Visualizing Data
Visualization helps interpret data effectively. Below is an example of a stacked bar chart:

```python
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Country': ['USA', 'UK', 'Germany'],
    'Gold': [10, 8, 6],
    'Silver': [7, 6, 5],
    'Bronze': [6, 5, 4]
}
df = pd.DataFrame(data)

# Plotting a stacked bar chart
df.set_index('Country').plot(kind='bar', stacked=True)
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('Medal Counts by Country')
plt.show()
```
- **Visualization**: Use `matplotlib` to create plots, with detailed control over labels, titles, and styles.

---

## Week 3: Exploratory Data Analysis & Processing Data

### Exploratory Data Analysis (EDA)
Explore your dataset using these commands:

```python
# Display the first few rows
print(df.head())
```
- **Previewing data**: Inspect the first rows of the DataFrame.

```python
# Summary statistics
print(df.describe())
```
- **Descriptive statistics**: Summarize numerical columns.

```python
# Checking for missing values
print(df.isnull().sum())
```
- **Missing values**: Identify incomplete data.

### Processing Data
Prepare your data for analysis by handling issues like missing values and outliers:

```python
# Filling missing values with 0
df_filled = df.fillna(0)
```
- **Fill missing data**: Replace `NaN` values with specified values.

```python
# Removing duplicates
df_unique = df.drop_duplicates()
```
- **Remove duplicates**: Eliminate repeated rows.

```python
# Detecting outliers using the IQR method
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Age'] < (Q1 - 1.5 * IQR)) | (df['Age'] > (Q3 + 1.5 * IQR))]
```
- **Outliers**: Use the Interquartile Range (IQR) method to detect extreme values.

---

## Week 4: Joining Data, SQL, and Introduction to RegEx

### Joining DataFrames
Merge two DataFrames using a common column:

```python
# Merging two DataFrames
merged_df = pd.merge(df1, df2, on='common_column', how='inner')
```
- **Merge**: Combine datasets by matching rows based on a key column.

### Interacting with SQLite Databases

```python
import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('database.db')

# Reading a table into a DataFrame
df = pd.read_sql_query("SELECT * FROM table_name", conn)

# Writing a DataFrame to a SQL table
df.to_sql('table_name', conn, if_exists='replace', index=False)

# Closing the connection
conn.close()
```
- **SQL interaction**: Use SQLite to manage relational data within Python.

### Using Regular Expressions (RegEx)

```python
import re

# Finding all words in a string
pattern = r'\b[A-Za-z]+\b'
text = 'Sample text with several words.'
matches = re.findall(pattern, text)
print(matches)
```
- **RegEx**: Extract patterns from text using the `re` library.

---

## Week 5: Retrieving Data from the Web

### Making API Requests

```python
import requests

# Sending a GET request
response = requests.get('https://api.example.com/data')

# Checking the response status
if response.status_code == 200:
    data = response.json()
    print(data)
```
- **API requests**: Interact with web APIs to retrieve JSON data.

### Web Scraping

```python
from bs4 import BeautifulSoup

# Sending a GET request
response = requests.get('https://www.example.com')

# Parsing the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all paragraph texts
paragraphs = [p.text for p in soup.find_all('p')]
print(paragraphs)
```
- **Web scraping**: Extract information from websites using `BeautifulSoup`.

---

## Week 6: Functional Programming

### Using Pure Functions

```python
# Pure function example
def add(a, b):
    return a + b
```
- **Pure functions**: Functions without side effects, ideal for functional programming.

### Higher-Order Functions

```python
# Applying a function to a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))

# Filtering even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```
- **Higher-order functions**: Use `map` and `filter` to apply transformations and filters to lists.

### Functional Composition

```python
from functools import reduce

# Composing functions
def add_one(x):
    return x + 1

def square(x):
    return x * x

# Using reduce to apply functions sequentially
functions = [add_one, square]
result = reduce(lambda acc, func: func(acc), functions, 5)
print(result)
```
- **Composition**: Combine multiple functions into a single operation for clean and reusable logic.