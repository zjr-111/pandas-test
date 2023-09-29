import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

raw_data = np.genfromtxt(
  'https://media-zip1.baydn.com/storage_media_zip/qkklny/a77f0c6443b6f5594b8f80d4aa7dfed1.42db6c0445109c28f3e3b9ad444e1ea6.csv',
  delimiter=',',
  skip_header=True,
  dtype=None,
  encoding='utf8'
)

# 处理后的数据
dataset = []

for row in raw_data:
    # 去除空数据
    new_row = [v for v in row if v != '']
    dataset.append(new_row)

te = TransactionEncoder()
encorder = te.fit(dataset)

one_hot_encoded_array = encorder.transform(dataset)
dataset_te = pd.DataFrame(one_hot_encoded_array, columns=encorder.columns_)
# print(dataset)
# 支持度大于0.4
frequent = apriori(dataset_te, min_support = 0.2, use_colnames = True)

# 找出置信度大于0.8的关联规则
rules = association_rules(frequent, metric = 'confidence', min_threshold = 0.6)

# 显示满足条件的规则,按提升度从高到低排序
print(rules.sort_values('lift',ascending=False))