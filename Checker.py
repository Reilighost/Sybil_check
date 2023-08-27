address_file = 'Exposed_wallets_407.txt'
to_check_file = 'to_check.txt'

with open(address_file, 'r') as f:
    addresses = f.readlines()

with open(to_check_file, 'r') as f:
    to_check_addresses = f.readlines()

# Уберем возможные символы новой строки
addresses = [address.strip() for address in addresses]
to_check_addresses = [address.strip() for address in to_check_addresses]

# Проверяем адреса и добавляем метку "Already Exposed" к уже существующим адресам
output = []
for index, address in enumerate(to_check_addresses, 1):
    status = "Exposed" if address in addresses else ""
    output.append(f"{address} {status}")

# Выводим результат
for line in output:
    print(line)
