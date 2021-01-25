import numpy as np
import pandas as pd

a = np.random.randint(10, 80, 20).tolist()
# a = np.random.randint(10, 80, 20)
df = pd.DataFrame(data=a, columns=['origin'])
# a= [39, 20, 56, 30, 53, 62, 46, 61, 40, 70, 37, 39, 66, 51, 74, 71, 39, 20, 14, 39]
# print("a=",a)
# print("\n")
# print(df)

df['hash'] = df['origin'] -1
print(df)
print('\n')

c = []
start = 1

while not df.empty:

    b = []
    d = []
    base = df['hash'].iloc[0]
    # print(base)

    for index, row in df.iterrows():
        # print(row)
        if abs(base - row['hash']) <10:
            b.append(row)
            # print(b)
        else:
            d.append(row)

    b_df = pd.DataFrame(b)
    df = pd.DataFrame(d)

    if len(b_df) > 1:
        c.append(b_df)
        print(df)
        print(c)
        print('\n')


# if len(b)>1:
#     c.append(b)
# #     print('df=', df)
#     print('c=', c)
# #     print('\n')

# while a:
#     b = []
#     d = []
#     base = a[0]
#
#     for item in a:
#         if abs(base - item)<10:
#             b.append(item)
#         else:
#             d.append(item)
#     a = d
#
#     if len(b)>1:
#         c.append(b)
#         print("a=",a)
#         print("c=",c)
#         print("\n")
