import pandas as pd

df = pd.DataFrame({"nome": ["Akira", "Chat"], "nota": [10, 10]})
print(df)
print("\nDescribe:")
print(df.describe(include="all"))
