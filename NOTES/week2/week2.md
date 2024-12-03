# Week 2
## Concepts
Introduces dataframes (often written as df in code) as a tool for managing and analyzing tabular data. 

Key operations include:

- **Sorting** 
- **Selecting** 
- **Filtering**
data to narrow down and organize information efficiently.
- **Mutating** (modifying data, eg. adding new variable from existing data),
- **Grouping** 
for more targeted analysis.

### Piping
Having a dataframe going through many operations in a single code block instead of having many lines. Can basically see the entire workflow. 
`df \ [[]] \ .groupby() \ .sum()`

### Data Visualization
Explains the importance of visualizing data for clearer insights, covering the use of different plot types:

- **Line Charts** – useful for trends over time.
- **Bar Plots** – helpful for comparing categorical data.

Selecting the right plot type depends on the analysis golas, enhancing data interpretation.

## From Tutorial
Instead of defining new function, can simply write a single line variable definition:
`relevant_df = df[["Country", "Gold", "Silver", "Bronze", "Total"]]`
after already having read the file:
`df = pd.read_csv("filename")`
we can mutate data by adding a new variable `total` which sums over a certain axis. 

