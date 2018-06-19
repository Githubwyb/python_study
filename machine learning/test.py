#coding=utf-8
import numpy as np
from pandas import Series, DataFrame
from sklearn.naive_bayes import GaussianNB

# numbers = [1, 2, 3, 4, 5]
# print(np.mean(numbers))
# print(np.median(numbers))
# print(np.std(numbers))

# d = {
#     'name':Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index = ['a', 'b', 'c', 'd']),
#     'age':Series([22, 38, 26, 35], index = ['a', 'b', 'c', 'd']),
#     'fare':Series([7.25, 71.83, 8.05], index = ['a', 'b', 'd']),
#     'survived?':Series([False, True, True, False], index = ['a', 'b', 'c', 'd'])
# }

# df = DataFrame(d)

# print(type(df))
# print(df['name'])
# print(df[['name', 'age']])
# print(df.loc['a'])
# print(df[df['age'] >= 30])
# print(df['survived?'][df['age'] >= 30])


# countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
#                  'Netherlands', 'Germany', 'Switzerland', 'Belarus',
#                  'Austria', 'France', 'Poland', 'China', 'Korea',
#                  'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
#                  'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
#                  'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

# gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
# bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

# olympic_medal_counts = {
#     'country_name' : Series(countries),
#     'gold' : Series(gold),
#     'silver' : Series(silver),
#     'bronze' : Series(bronze)
# }

# olympic_medal_counts_df = DataFrame(olympic_medal_counts)

# print(olympic_medal_counts_df)

# avg_bronze_at_least_one_gold = olympic_medal_counts_df[olympic_medal_counts_df['gold'] >= 1]['bronze']
# avg_bronze_at_least_one_gold = np.mean(avg_bronze_at_least_one_gold)

# print(avg_bronze_at_least_one_gold)

# avg_medal_count = olympic_medal_counts_df[['gold', 'silver', 'bronze']].apply(np.mean)

# print(avg_medal_count)

# points = np.dot(olympic_medal_counts_df[['gold', 'silver', 'bronze']], [4, 2, 1])

# olympic_points = {
#     'country_name' : Series(olympic_medal_counts_df['country_name']),
#     'points' : Series(points)
# }

# olympic_points_df = DataFrame(olympic_points)

# print(olympic_points_df)


# d = {
#     'one' : Series([1, 2, 3], index = ['a', 'b', 'c']),
#     'two' : Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
# }

# df = DataFrame(d)

# print(df)
# print(df.apply(np.mean))
# print(df['one'].map(lambda x : x >= 1))
# print(df.applymap(lambda x : x >= 1))


# a = [1, 2, 3, 4, 5]
# b = [2, 3, 4, 5, 6]

# print(np.dot(a, b))

# a = [1, 2]
# b = [[2, 4, 6], [3, 5, 7]]

# print(np.dot(a, b))

# a = [[2, 4, 6], [3, 5, 7]]
# b = [[8], [9], [10]]

# print(np.dot(a, b))

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print(clf_pf.predict([[-0.8, -1]]))