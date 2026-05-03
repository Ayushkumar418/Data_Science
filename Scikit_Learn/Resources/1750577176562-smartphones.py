import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of rows
num_rows = 1000

# Generate data
data = {
    'camera': np.random.randint(8, 201, size=num_rows),         # Megapixels (8 to 200)
    'age': np.random.randint(0, 4, size=num_rows),              # Age in years (0 to 3)
    'ram': np.random.choice([4, 6, 8, 12, 16], size=num_rows),  # RAM in GB
    'cpu_score': np.random.randint(40, 101, size=num_rows),     # CPU benchmark score (40 to 100)
    'slot_sd': np.random.randint(0, 2, size=num_rows),          # SD card slot (0 = no, 1 = yes)
    'sims': np.random.choice([1, 2], size=num_rows),            # Number of SIMs
    'price': np.random.randint(8000, 70001, size=num_rows)      # Price in INR (₹8,000 to ₹70,000)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("smartphone_data.csv", index=False)

# Display first few rows
print(df.head())
