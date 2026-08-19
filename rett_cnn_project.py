import pandas as pd

# Full paths to the files in your CNN Project folder
counts_path = r"C:\Users\anbuo\OneDrive\Desktop\CNN Project\GSE271893_raw_counts.txt"
meta_path   = r"C:\Users\anbuo\OneDrive\Desktop\CNN Project\sample_metadata.csv"  # or your exact CSV name

# 1. Load gene expression counts
counts = pd.read_csv(counts_path, sep="\t", index_col=0)

# 2. Load metadata
meta = pd.read_csv(meta_path, index_col=0)

# 3. Check they loaded correctly
print("Counts shape:", counts.shape)
print("Meta shape:", meta.shape)

# 4. Quick look at metadata
print(meta.head())
print("Metadata columns:", meta.columns)
