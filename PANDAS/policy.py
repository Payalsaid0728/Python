import pandas as pd
df=pd.read_csv("policies.csv")
# print(df.head())

# high coverage policies
high_coverage=df[df["Coverage"].apply(
    lambda coverage:coverage >1000000
    )]
# print(high_coverage)

# Apply a premium discount
df["DiscountedPremium"]=df["Premium"].apply(
    lambda premium:premium*0.90
)
# print(df)

# Calculate Premium Category
df["PremiumCategory"]=df["Premium"].apply(
    lambda premium:"high"
    if premium >=50000
    else "Normal"
)
# print(df)

# sort policies by  premium from highest to lowest
sorted_policies=df.sort_values(
    by="Premium",
    ascending=False
)
# print(sorted_policies)

# Find average premium per insurance product
avg_premium=(
    df.groupby("Product")["Premium"]
    .apply(lambda x:x.mean())
    )
# print(avg_premium)

# Filter Active Policies: Show only active insurence policies
active_policies=df[
    df["Status"].apply(
        lambda Status:Status=="Active"
    )
]
# print(active_policies)

# CHALLENGE1
# Status = Active AND Coverage > ₹20,00,000
policies = df.apply(
    lambda row: row["Status"] == "Active" and
                row["Coverage"] > 1000000,
    axis=1
)
# print(policies)


# CHALLENGE2
# Apply a 15% premium discount
df["special_premium"]=df["Premium"].apply(
        lambda Premium:Premium *0.85
    )

# print(df)

# CHALLENGE3
df["RiskCategory"]=df["Age"].apply(
    lambda Age: "Senior"
      if Age > 50
      else "middle" if Age >= 35
    else "Young"
)

# print(df)

 # CHALLENGE4
 # SORT POLICIES BY COVERAGE IN DESENDING ORDER
  
sort=sort = df.sort_values(
    by="Coverage",
    ascending=False
)

# print(sort)

# CHALLENGE5
# Average Premium per Product
df["Average_premium"]=df.groupby("Product")["Premium"].apply(
        lambda x: x.mean()
    )
    
# print(df)

# CHALLENGE6
# Average Coverage per Product
df["Average_Coverage"]=df.groupby("Product")["Coverage"].apply(
        lambda x: x.mean()
    )
    
print(df)