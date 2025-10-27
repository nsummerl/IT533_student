# IT 533 — Chapter 11 Activity
# Author: Nick Summerlee
# Proffesor: Heiden

# 1) Chained assignment: initialize related config values
debug = logging_enabled = verbose = False
retry_count = timeout_s = 0
if not verbose:
    print("Verbose mode is currently OFF; keeping defaults.")

# 2) Tuple swap: correct reversed first/last names
first_name, last_name = "Doe", "Jane"
last_name, first_name = first_name, last_name
print(f"[Swap Fix] Corrected name: {first_name} {last_name}")

# 3) Starred unpacking: parse variable-length payload
payload = ["device-7", 23.4, 23.6, 23.7, "OK"]
device_id, *aux_readings, status = payload
print(f"[Parse] device_id={device_id}, aux_readings={aux_readings}, status={status}")

# 4) Augmented assignment: calculate shopping cart total
cart_prices = [19.99, 5.00, 12.50, 3.25]
subtotal = 0.0
for price in cart_prices:
    subtotal += price
tax_rate = 0.06
total = subtotal
total += subtotal * tax_rate
print(f"[Cart] subtotal=${subtotal:.2f}, total=${total:.2f}")

# 5) Attribute and index assignment: update user cache
class Profile:
    def __init__(self, username):
        self.username = username
        self.online = False

cache = {"jane": Profile("jane")}
cache["jane"] = cache.get("jane", Profile("jane"))
cache["jane"].online = True
print("[User]", cache["jane"].username, "online =", cache["jane"].online, sep=" | ", end=" \n")

if __name__ == "__main__":
    pass
