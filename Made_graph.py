import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def fetch_nonce_zero_transactions(limit=50000):
    # Connect to the database
    conn = sqlite3.connect('nonce_zero_transactions.db')
    cursor = conn.cursor()

    # Fetch a limited set of transactions with nonce = 0, including additional fields and the hash
    cursor.execute(
        """SELECT hash, wallet, MIN(blockNumber) as min_block, value, functionName, timeStamp 
           FROM transactions WHERE nonce = 0 GROUP BY wallet LIMIT ?""",
        (limit,))
    data = cursor.fetchall()

    conn.close()

    return data

def on_pick(event):
    # Get the index of the selected point
    ind = event.ind[0]

    # Extract point attributes
    txn_hash = df.iloc[ind]['hash']
    wallet = df.iloc[ind]['wallet']
    blockNumber = df.iloc[ind]['blockNumber']
    value = df.iloc[ind]['value']
    functionName = df.iloc[ind]['functionName']
    timeStamp = df.iloc[ind]['timeStamp']

    # Display the attributes, including the hash
    print(f"{wallet} | {value} | {timeStamp} | {functionName if functionName else 'N/A'} | https://arbiscan.io/address/{wallet} | https://arbiscan.io/tx/{txn_hash}")

def on_key(event):
    if event.key == 'enter':
        # Print 3 empty lines to "clear" the output
        for _ in range(3):
            print("\n")

# Fetch a limited data set
nonce_zero_transactions = fetch_nonce_zero_transactions()

# Convert the data to a DataFrame
df = pd.DataFrame(nonce_zero_transactions, columns=['hash', 'wallet', 'blockNumber', 'value', 'functionName', 'timeStamp'])

# Sort the DataFrame by block number
df = df.sort_values(by='blockNumber')

# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))
sc = ax.scatter(df['blockNumber'], range(len(df['wallet'])), picker=True)
ax.set_ylabel('Wallet Index (sorted by Block Number)')
ax.set_xlabel('Block Number')
ax.set_title('Transactions with nonce=0 by wallet indices and blocks')

# Connect events
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('key_press_event', on_key)

plt.tight_layout()
plt.show()
