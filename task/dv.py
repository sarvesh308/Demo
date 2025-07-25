# NumPy Basics
"""

import numpy as np
# 1D Array
a=np.array([1,2,3,4,5])
print(a)

# 2D Array
b=np.array([[1,2,3],[4,5,6]])
print(b)

# zero array
c=np.zeros((2,3))
print(c)

# ones array
d=np.ones((2,3))
print(d)

# full array
e=np.full((2,3),7)
print(e)    

# arange
f=np.arange(0,10,2)
print(f)    

#eye
g=np.eye(3)
print(g)

# Linear space
h=np.linspace(0,1,5)
print(h)

# Random array
i=np.random.random((2,2))
print(i)

# array attributes
arr=np.array([[1,2,3],[4,5,6]])
print("Shape:", arr.shape)
print("Size:", arr.size)    
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)

# Indexing and slicing
arr=np.array([[1,2,3],[4,5,6]])
print(arr[0,1])
print(arr[:,1])

# Mathematical operations
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])
print(arr1+arr2)
print(arr1*arr2)
print(np.sum(arr1))
print(np.mean(arr1))
print(np.std(arr1))
print(np.max(arr2))

# Reshape and Flatten
arr=np.array([[1,2,3],[4,5,6]])
print(arr.reshape(3,2))
print(arr.flatten())    

"""
# Pandas basics
"""
import pandas as pd

# series
a=pd.Series([1,2,3,4,5],['a','b','c','d','e'])
print(a)

# DataFrame
data={
    'Name:': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df=pd.DataFrame(data)
print(df)

# Reading CSV
df=pd.read_csv('output.csv')
print(df)

# Writing CSV
df.to_csv('output.csv', index=False)

# Writing Excel
df.to_excel('output.xlsx', index=False)
df.to_excel('output.xlsx', index=False, sheet_name='Sheet1')

# reading Excel
df=pd.read_excel('output.xlsx')
print(df)

# View and indexing
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.shape)   # Shape of DataFrame
print(df.columns) # Column names

print(df.iloc[0])  # Accessing a row by index   
print(df.info())  # DataFrame info
print(df.describe())  # Descriptive statistics

# Filtering rows
print(df[df['age'] > 10])
print(df[df['loc'] == 'chennai'])

# Adding and modifying columns
df['Age + 5'] = df['age'] + 5
print(df)
df['salary'] = [50000, 60000]
print(df)

# Deleting columns
df.drop('salary', axis=1, inplace=True)
print(df)   

# Renaming columns
df.rename(columns={'age': 'Age'}, inplace=True) 
print(df)

# Grouping data
grouped = df.groupby('loc').mean()
print(grouped)

# Merging DataFrames
data2 = {
    'Name': ['Alice', 'Bob'],
    'Salary': [70000, 80000]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='Name', how='inner')   
print(merged_df)

# Concatenating DataFrames
df3 = pd.DataFrame({ 
    'Name': ['David', 'Eve'],
    'Age': [28, 32],
    'City': ['Miami', 'Seattle']
})  
concat_df = pd.concat([df, df3], ignore_index=True)
print(concat_df)

"""

# Matplotlib basics

import matplotlib.pyplot as plt
# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x,y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Bar plot
x = ['A', 'B', 'C', 'D']
y = [3, 7, 2, 5]
plt.bar(x, y)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x, y, color='red')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color='green', edgecolor='black')
plt.title('Histogram')  
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()