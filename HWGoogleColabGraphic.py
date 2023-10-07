import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
categories = data['whoAmI'].unique()
category_dict = {category: [1 if value == category else 0 for value in data['whoAmI']] for category in categories}
one_hot_data = pd.DataFrame(category_dict)
print(one_hot_data.head())
