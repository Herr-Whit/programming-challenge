# Problem Analysis
The tasks in question involve loading data in csv format and identifying a datapoint with the maximum difference between given columns and returning a specific value from that row. 

# Approach
## Scratch in Jupyter Notebook (The Data-Scientists Approach)
Initially I will try to solve the problem within jupyter notebooks. 
This allows me to examine the data I load from the csv, compare it to the original file and explore it. I am interested in the following
- Datatypes
- File size (number of columns/rows)
- Null values
- Outliers
- Encoding errors

I will use the pandas package for loading and processing the data. My initial idea is to implement the computations as 
matrix operations and reductions. 
This approach will allow me to familiarize myself with the data and attempt a specific solution.

The scratch_attempt notebook details the solution to the first challenge (weather). The logic is incorporated in 
`solutions/specific/weather_solution.py`.
## Generalize the Problem
The common factors of the football and weather challenges are the file format and most elements of the computation.
The differences are the file names and the data itself.
### The Computation
Let A be a Matrix and i, j indicate column indices. Both tasks follow the form:

MAX(A<sub>i</sub> - A<sub>j</sub>)

_I would like to keep the concrete reduction function (in this case MAX) flexible_.
## Identify Concerns

## Design Architecture
TODO
## Implement
TODO