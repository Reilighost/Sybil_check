# Solution for Sybil Hunting

`Sybil_check` is a toolkit designed to help users identify and analyze suspicious wallet activities that may be related to Sybil attacks. It offers two main tools: a **Checkers** and a **Graph creation**.

## Checkers

### Purpose
This tool help determine presence in both .txt file: `eligible_wallet_list.txt` and `exposed_wallets_to_482.txt`.

### How It Works
- Users input wallet details into a `to_check.txt`.
- The first script `Check_in_eligible.py` checks the wallet against a liability list. If the wallet is found on this list, it is marked as 'Eligible' on terminal.
- The second script `Check_in_exposed.py` cross-references the wallet against a Sybil list to determine if it has already exposed in a sybill report (data collected from 0 to 482 report).

## Graph creation

### Purpose
Provides a visual representation of wallet activities to discern genuine users from potential sybill attackers.

### How It Works
- The graph displays ONLY wallet initial trx, on arbitrum network. (nonce [0] tx)
- Wallets are arranged chronologically, with older wallets on the left and newer ones on the right.
- Genuine human users appear as random dots on the graph, while potential Sybil actors often form a flat line due to their automated, rapid transactions.
- Users can zoom into the graph to view individual transactions and can click on any dot to retrieve detailed information about the respective transaction.
- Data that be display: address, value, time, function call, link to both trx and user wallet on arbiscan
---

Toolkit empowers users with necessary tools to efficiently hunt for sybill wallets, fostering a safer and more transparent network environment.
