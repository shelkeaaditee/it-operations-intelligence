
import pandas as pd

# Load the synthetic incident dataset
df = pd.read_csv("data/incidents.csv")

# Convert timestamp columns from strings to datetime
timestamp_columns = [
    "created_at",
    "resolved_at",
    "sla_due_at"
]

for column in timestamp_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

print("\n--- Updated Data Types ---")
print(df.dtypes)

print("\n--- Timestamp Conversion Check ---")
print(df[timestamp_columns].isnull().sum())


# 1. Check the number of rows and columns
print("\n--- Dataset Shape ---")
print(df.shape)

# 2. Display the first five records
print("\n--- First Five Records ---")
print(df.head())

# 3. Inspect column names and data types
print("\n--- Dataset Information ---")
df.info()

# 4. Check missing values in each column
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 5. Check duplicate records
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# 6. Check duplicate incident IDs
print("\n--- Duplicate Incident IDs ---")
print(df["incident_id"].duplicated().sum())



# 7. Analyze incident distribution by priority
print("\n--- Incidents by Priority ---")
print(df["priority"].value_counts())

# 8. Analyze incident distribution by category
print("\n--- Incidents by Category ---")
print(df["category"].value_counts())

# 9. Analyze incident distribution by status
print("\n--- Incidents by Status ---")
print(df["status"].value_counts())

# 10. Analyze incidents by support group
print("\n--- Incidents by Support Group ---")
print(df["support_group"].value_counts())



# 11. Analyze monthly incident creation trends

# Extract the month from each incident's creation timestamp
df["created_month"] = df["created_at"].dt.to_period("M")

# Count incidents created in each month
monthly_incidents = (
    df.groupby("created_month")
    .size()
    .sort_index()
)

print("\n--- Monthly Incident Creation Trend ---")
print(monthly_incidents)


import matplotlib.pyplot as plt 

# # Plot monthly incident creation trend
# monthly_incidents.plot(kind="bar")

# plt.title("Monthly Incident Creation Trend")
# plt.xlabel("Month")
# plt.ylabel("Number of Incidents")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# # 12. Analyze monthly incident counts by status

# monthly_status = pd.crosstab(
#     df["created_month"],
#     df["status"]
# )

# print("\n--- Monthly Incidents by Status ---")
# print(monthly_status)

# # Visualize monthly incident counts by status
# monthly_status.plot(kind="bar", figsize=(12, 6))

# plt.title("Monthly Incidents by Status")
# plt.xlabel("Month")
# plt.ylabel("Number of Incidents")
# plt.xticks(rotation=45)
# plt.legend(title="Incident Status")
# plt.tight_layout()
# plt.show()


# 13. Calculate the percentage of each status within each month

monthly_status_pct = pd.crosstab(
    df["created_month"],
    df["status"],
    normalize="index"
) * 100

print("\n--- Monthly Status Distribution (%) ---")
print(monthly_status_pct.round(2))



# 14. Analyze unresolved incidents by category

unresolved_statuses = ["New", "In Progress", "On Hold"]

unresolved_by_category = (
    df[df["status"].isin(unresolved_statuses)]
    .groupby("category")
    .size()
    .sort_values(ascending=False)
)

print("\n--- Unresolved Incidents by Category ---")
print(unresolved_by_category)


# 15. Calculate unresolved incidents as a percentage
# of all incidents in each category

unresolved_df = df[
    df["status"].isin(["New", "In Progress", "On Hold"])
]

total_by_category = df.groupby("category").size()
unresolved_by_category = unresolved_df.groupby("category").size()

unresolved_percentage = (
    unresolved_by_category / total_by_category * 100
).sort_values(ascending=False)

print("\n--- Unresolved Incident Percentage by Category ---")
print(unresolved_percentage.round(2))
