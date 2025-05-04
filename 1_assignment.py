import pandas as pd

# Load the dataset
dataset = pd.read_csv('Walmart.csv')
print(" Dataset Loaded Successfully")

# Preview the dataset
print("\n First 5 Rows:")
print(dataset.head())

print("\n Last 10 Rows:")
print(dataset.tail(10))

# Get dataset insights
print("\n Dataset Shape (Rows, Columns):", dataset.shape)
print("\n Column Data Types:")
print(dataset.dtypes)

print("\n Column Names:")
print(dataset.columns.tolist())

# Dataset values (all rows and columns)
# print(dataset.values)  # Uncomment for full data printout

# Calculate total weekly sales
total_sales = dataset["Weekly_Sales"].sum()
print(f"\n Total Weekly Sales: {total_sales}")

# Copy a single column
weekly_sales = dataset["Weekly_Sales"].copy()
print("\n Copied Weekly Sales Column:")
print(weekly_sales)

# Select specific columns
selected_cols = ['Date', 'Weekly_Sales', 'Fuel_Price']
print("\n Selected Columns:")
print(dataset[selected_cols])

# Insert a new column
dataset.insert(loc=4, column="Description", value="describe")
print("\n Dataset after Inserting 'Description' Column:")
print(dataset.head())

# Handling missing values
print("\n Dropping Rows with Missing Values (Any):")
print(dataset.dropna(how="any"))

print("\n Dropping Rows with Missing Values (All):")
print(dataset.dropna(how="all"))

print("\n Dropping Rows with Missing 'Fuel_Price':")
print(dataset.dropna(subset=["Fuel_Price"]))

print("\n🧹 Dropping Rows with Missing 'Fuel_Price' or 'Temperature':")
print(dataset.dropna(subset=["Fuel_Price", "Temperature"]))

# Filling missing values
print("\n Filling All Missing Values with 0:")
print(dataset.fillna(0))

print("\n Filling Missing 'Fuel_Price' Values with 0:")
print(dataset["Fuel_Price"].fillna(0))

# Statistical summaries
max_temp = dataset["Temperature"].max()
min_fuel_price = dataset["Fuel_Price"].min()

print("\n Highest Temperature Recorded:", max_temp)
print("⛽ Lowest Fuel Price Recorded:", min_fuel_price)
