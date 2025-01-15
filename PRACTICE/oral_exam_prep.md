# Statistical Data Processing Course Summary

This summary includes the key topics from Weeks 1 to 6 of the Statistical Data Processing course, with Python syntax, examples, and detailed explanations.

---

## Week 1: Introduction to Data Science

### Data Types in Python

Data in Python is categorized into different types based on its structure:

- **Structured Data**: Tabular data like CSV files and Excel sheets.
- **Semi-Structured Data**: JSON, XML, and YAML files.
- **Unstructured Data**: Raw text files, images, videos, and other media.

#### Example: Reading Data
To work with data, you often need to load it into Python. Here's how you can read a CSV file:

```python
import pandas as pd

# Reading a CSV file
data = pd.read_csv("example.csv")
print(data.head())
```
Explanation:
- `pd.read_csv("example.csv")`: Reads the CSV file into a DataFrame.
- `data.head()`: Displays the first 5 rows of the DataFrame.

---

## Week 2: DataFrames & Visualizing Data with Plots

### DataFrames in Pandas
DataFrames are a core structure in Pandas for handling tabular data. 

#### Common Operations
1. **Sorting**: Arranging rows based on column values.
```python
sorted_data = data.sort_values(by="column_name")
```
Explanation: Sorts the DataFrame by the values in `column_name`.

2. **Selecting Columns**: Picking specific columns from the DataFrame.
```python
selected_columns = data[["column1", "column2"]]
```
Explanation: Creates a new DataFrame with only `column1` and `column2`.

3. **Filtering Rows**: Keeping rows that meet certain conditions.
```python
filtered_data = data[data["column_name"] > 10]
```
Explanation: Selects rows where the values in `column_name` are greater than 10.

4. **Mutating**: Adding new columns or modifying existing ones.
```python
data["new_column"] = data["column1"] + data["column2"]
```
Explanation: Creates a new column `new_column` as the sum of `column1` and `column2`.

5. **Grouping and Aggregating**: Summarizing data by categories.
```python
grouped_data = data.groupby("category_column").mean()
```
Explanation: Groups data by `category_column` and calculates the mean for each group.

### Visualizing Data with Matplotlib
Visualization is key to understanding data patterns.

#### Example: Creating Common Plots
```python
import matplotlib.pyplot as plt

# Histogram
data["column"].plot(kind="hist")
plt.title("Histogram of Column")
plt.show()

# Scatter Plot
data.plot.scatter(x="column1", y="column2")
plt.title("Scatter Plot")
plt.show()
```
Explanation:
- `kind="hist"`: Creates a histogram to show the distribution of values.
- `plot.scatter(x, y)`: Visualizes the relationship between two variables.

---

## Week 3: Exploratory Data Analysis (EDA) & Processing Data

### EDA: Steps and Code Examples
EDA involves systematically exploring data to summarize its main characteristics.

#### Key Steps
1. **Formulating Questions**
   Example: What is the average value of `column1`?

2. **Visualizing Data**
```python
data["column1"].plot(kind="box")
plt.title("Box Plot of Column1")
plt.show()
```
Explanation: A box plot shows the distribution and identifies potential outliers.

3. **Summary Statistics**
```python
print(data.describe())
```
Explanation: Generates statistics like mean, standard deviation, and quartiles.

### Data Cleaning

1. **Handling Missing Values**
```python
# Replace NaN with 0
data.fillna(value=0, inplace=True)

# Drop rows with NaN in a specific column
data.dropna(subset=["column"], inplace=True)
```
Explanation:
- `fillna(value=0)`: Fills missing values with 0.
- `dropna(subset=["column"])`: Removes rows where `column` has missing values.

2. **Addressing Outliers**
```python
q1 = data["column"].quantile(0.25)
q3 = data["column"].quantile(0.75)
iqr = q3 - q1
filtered_data = data[(data["column"] >= q1 - 1.5 * iqr) & (data["column"] <= q3 + 1.5 * iqr)]
```
Explanation: Uses the Interquartile Range (IQR) to filter out extreme outliers.

---

## Week 4: Joining Data, SQL, and Regular Expressions (RegEx)

### Joining Data in Pandas
Combining datasets is crucial when working with related information.

#### Example: Merge DataFrames
```python
merged_data = pd.merge(data1, data2, on="common_column", how="inner")
```
Explanation:
- `on="common_column"`: Specifies the column to join on.
- `how="inner"`: Keeps only rows with matching values in both datasets.

### SQL Basics
SQL is used to manage and query relational databases.

#### Example: Basic Query
```python
import sqlite3

# Connect to a database
conn = sqlite3.connect("example.db")

# Query the database
query = "SELECT column1, column2 FROM table WHERE column1 > 10"
result = pd.read_sql_query(query, conn)
```
Explanation:
- `sqlite3.connect()`: Establishes a connection to the database.
- `pd.read_sql_query(query, conn)`: Executes the query and returns the result as a DataFrame.

### Regular Expressions (RegEx)
RegEx is used for pattern matching in strings.

#### Example: Validating an Email
```python
import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@test.com"
if re.match(pattern, email):
    print("Valid email")
```
Explanation:
- `re.match(pattern, email)`: Checks if the email matches the pattern.

---

## Week 5: Retrieving Data from the Web

### REST APIs
REST APIs allow you to interact with online services.

#### Example: Making a GET Request
```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
print(data)
```
Explanation:
- `requests.get(url)`: Sends a GET request to the specified URL.
- `response.json()`: Converts the response to a Python dictionary.

### Web Scraping
Extracting data from websites is useful when APIs are unavailable.

#### Example: Scraping HTML
```python
from bs4 import BeautifulSoup

html = "<html><body><h1>Example</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
```
Explanation:
- `BeautifulSoup(html, "html.parser")`: Parses the HTML content.
- `soup.h1.text`: Extracts the text inside the `<h1>` tag.

---

## Week 6: Functional Programming

### Functional Programming in Python
Functional programming treats computation as the evaluation of mathematical functions.

#### Key Functions
1. **Map**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```
Explanation: Applies the function `lambda x: x**2` to each element of the list.

2. **Filter**
```python
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```
Explanation: Keeps elements where the condition `x % 2 == 0` is `True`.

3. **Reduce**
```python
from functools import reduce

total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 10
```
Explanation: Combines elements in the list using the function `x + y`.

#### Higher-Order Functions
```python
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x: x + 2, 5))  # Output: 9
```
Explanation: `apply_twice` applies the given function `func` to `x` two times.

---

