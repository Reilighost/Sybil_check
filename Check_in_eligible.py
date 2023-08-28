# Define the file path
address_file = 'exposed_wallets_to_482.txt'

# Read the file and get all addresses
with open(address_file, 'r') as f:
    addresses = f.readlines()

# Deduplicate addresses using set and then convert back to list
unique_addresses = list(set(addresses))

# Sort the addresses if needed (optional)
unique_addresses.sort()

# Calculate and print the number of duplicates and unique addresses
num_duplicates = len(addresses) - len(unique_addresses)
print(f"Number of duplicates: {num_duplicates}")
print(f"Number of unique addresses: {len(unique_addresses)}")

# Write the unique addresses back to the file
with open(address_file, 'w') as f:
    f.writelines(unique_addresses)
