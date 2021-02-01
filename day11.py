import pandas as pd
import numpy as np

q_df = pd.DataFrame([['male', 'teacher'],
                     ['male', 'engineer'],
                     ['female', None],
                     ['female', 'engineer']], columns=['Sex', 'Profession'])

# 缺失值填入字串'others'
q_df.fillna('others', inplace=True)
print(q_df)
# 更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
# 性別與職業皆屬無法以數值表示的統計資料(一般性)，get_dummies()較適合
sex_mapping = {value: index for index, value in enumerate(set(q_df['Sex']))}
profession_mapping = {value: index for index, value in enumerate(set(q_df['Profession']))}
q_df['Sex label'] = q_df['Sex'].map(sex_mapping)
q_df['Profession label'] = q_df['Profession'].map(profession_mapping)
print(q_df)