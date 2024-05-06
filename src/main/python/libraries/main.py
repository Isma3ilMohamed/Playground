import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# 0-d array or a scalar
np_arr0 = np.array(20)
# 1-d array
np_arr1 = np.array([10, 20, 30, 40, 50])
# 2-d array
np_arr2 = np.array([[10, 20, 30, 40], [90, 80, 70, 60]])
# 3-d array
np_arr3 = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])

# print('A 0-d array (scalar):\n', np_arr0,
#       '\n\nA 1-d array:\n', np_arr1,
#       '\n\nA 2-d array:\n', np_arr2,
#       '\n\nA 3-d array:\n', np_arr3)

a = np.array([3, 4.5, 5.1])
b = np.array([4, 5.2, 6])

# print("Addition of a and b:",np.add(a,b),
#       "\nMultiplication of a and b:", np.multiply(a,b),
#       "\nSubtraction of b from a:", np.subtract(a,b),
#       "\nDivision of a by b:", np.divide(a,b),
#       "\na raised to b is:", np.power(a,b),
#       "\nMod of a and b:", np.mod(a,b),
#       "\nRemainder from a/b:", np.remainder(a,b),
#       "\nRounded array a is:", np.round_(a,1),
#       "\nFloor of array a is:", np.floor(a),
#       "\nSquare root of array a is:", np.sqrt(a))


# Note capital S in Series
series_list = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
series_np = pd.Series(np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# Printing the results
# print('The index array from a series:', series_list.index,
#       '\nThe values array from a series: ', series_list.values)
#
# print("A pandas series list:\n", series_list,
#       "\nA pandas series using a Numpy array:\n", series_np)
series_index = pd.Series(np.array([10, 20, 30, 40, 50]), index=['a', 'b', 'c', 'd', 'e'])
# print("\nA pandas series with indexing in letters:\n", series_index)


dict = {'one': pd.Series([1.2, 2.3, 3.4], index=['a', 'b', 'c']),
        'two': pd.Series([1.5, 2.4, 3.2, 4.1], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(dict)
# print("Dataframe from a dictionary of Series is:\n", df)

df1 = pd.DataFrame(dict, index=['d', 'b', 'a'])
# print("Dataframe from a dictionary of Series with custom indices is:\n", df1)

my_dict = {
    'name': ["a", "b", "c", "c", "e"],
    'age': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(my_dict,
                  index=[
                      "First",
                      "Second",
                      "Third",
                      "Fourth",
                      "Fifth"])

# print("\nThe DataFrame is:\n", df)

# Getting 1D data as a Series from a DataFrame
series_name = df.name
# print("\nThe name Series from the DataFrame is:\n", series_name)

series_age = df.age
# Getting the mean value, size, unique items and lists out of a Series
# print("\nGetting mean value from the Series (age): ", series_age.mean(),
#       "\nGetting size of the Series (age): ", series_age.size,
#       "\nGetting unique values in the Series (name): ", series_name.unique(),
#       "\nGetting a list from the Series (name): ", series_name.tolist())


digit_data = load_digits()

print(digit_data.data.shape)
plt.gray()
plt.matshow(digit_data.images[4])
plt.show()
plt.savefig('output/iris_dataset_image.png', dpi=300)