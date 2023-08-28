# Define the file paths
address_file = 'eligible_wallet_list.txt'
to_check_file = 'to_check.txt'

# Open and read the eligible addresses file
with open(address_file, 'r') as f:
    addresses = f.readlines()

# Open and read the addresses that need to be checked
with open(to_check_file, 'r') as f:
    to_check_addresses = f.readlines()

# Remove possible newline characters from each address
addresses = [address.strip() for address in addresses]
to_check_addresses = [address.strip() for address in to_check_addresses]

# Check each address and add the label "Eligible" if it already exists in 'eligible_wallet_list'
output = []
for index, address in enumerate(to_check_addresses, 1):
    status = "Eligible" if address in addresses else ""
    output.append(f"{address} {status}")

# Print the result
for line in output:
    print(line)
