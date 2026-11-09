
# ==========================================
# TSE-analytics
# Price History Exploration
# ==========================================

# 1. Import libraries
import pandas as pd
import finpy_tse as fpy

# 2. Fetch stock price history
df = fpy.get_price_history(stock='خودرو', start_date='1404-01-01', end_date='1405-01-01', ignore_date=False)

# 3. Explore the dataset
print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 5 rows ---")
print(df.tail())

print("\n--- Dataset shape ---")
print(df.shape)

print("\n--- Column names ---")
print(df.columns)

print("\n--- Data types ---")
print(df.dtypes)


# 4. Inspect the index
print("\n--- Index information ---")
print("Index:", df.index)
print("Index name:", df.index.name)
print("Index data type:", df.index.dtype)
print("Index class:", type(df.index))


# 5. Check date range
print("\n--- Date range ---")
print("First date:", df.index.min())
print("Last date:", df.index.max())


# 6. Data quality checks
print("\n--- Missing values ---")
print(df.isna().sum())

print("\n--- Duplicate dates ---")
print(df.index.duplicated().sum())


# 7. Statistical summary
print("\n--- Statistical summary ---")
print(df.describe())