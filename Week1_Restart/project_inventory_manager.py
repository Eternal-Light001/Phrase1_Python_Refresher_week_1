# STEP (Procedure)


# TEST TABLE (Expectation)
# SCENARIO 1 — the default inventory above:
#   rice_50kg:    12 >= 5      → OK
#   beans_50kg:   3 < 5        → LOW, reorder 7 (5*2-3)
#   palm_oil_5l:  0            → CRITICAL, reorder 6 (3*2-0)
#   garri_50kg:   25 >= 10     → OK
#   tomato_paste: 8 < 15       → LOW, reorder 22 (15*2-8)
#   milk_powder:  40 >= 20     → OK
#   Summary: 6 items | OK: 3 | LOW: 2 | CRITICAL: 1
#
# SCENARIO 2 — change rice_50kg qty to 0 (simulate all sold out):
#   rice_50kg should now be CRITICAL, reorder 10
#   Summary: 6 items | OK: 2 | LOW: 2 | CRITICAL: 2
#
# SCENARIO 3 — change milk_powder qty to 19 (one below threshold):
#   milk_powder should be LOW, reorder 21
#   Summary: 6 items | OK: 2 | LOW: 3 | CRITICAL: 1


# Scripts
# Section 1 — Data (already defined above)
import datetime

inventory = {
    "rice_50kg":    {"qty": 12, "threshold": 5,  "price": 65000, "category": "grain"},
    "beans_50kg":   {"qty": 3,  "threshold": 5,  "price": 45000, "category": "grain"},
    "palm_oil_5l":  {"qty": 0,  "threshold": 3,  "price": 8500,  "category": "oil"},
    "garri_50kg":   {"qty": 25, "threshold": 10, "price": 28000, "category": "grain"},
    "tomato_paste": {"qty": 8,  "threshold": 15, "price": 800,   "category": "canned"},
    "milk_powder":  {"qty": 19, "threshold": 20, "price": 15000, "category": "canned"},
}

# Section 2 — classify_stock(item_data)
def classify_stock(item_data):
    """This is a function used to check the quantity of a product left."""

    if item_data["qty"] == 0:
        return "CRITICAL"
    elif item_data["qty"] < item_data["threshold"]:
        return "LOW"
    else:
        return "OK"

def compute_restock(item_data):
    """This is a function used to compute the quantity of a product to restock."""

    if item_data["qty"] >= item_data["threshold"]:
        return 0
    elif item_data["qty"] < item_data["threshold"] or item_data["qty"] == 0:
        return item_data["threshold"] * 2 - item_data["qty"]





def main():

    app_name = "Light Store Inventory Management System"
    print(f"=== {app_name} ===")

    # counters
    critical_count = 0
    low_count = 0
    ok_count = 0

    for name, item_data in inventory.items():
        status = classify_stock(item_data)
        reorder = compute_restock(item_data)

        print(f"{name}   | {item_data['qty']} | {status} | {reorder}")
        if status == "CRITICAL":
            critical_count += 1
        elif status == "LOW":
            low_count += 1
        else:
            ok_count += 1

    print()  # blank line

    # summary — using comprehensions (Day 7)
    greetings = "=== Inventory Summary ==="
    print(f"{greetings} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")

    print(f"Total items: {len(inventory)}")
    print(f"OK: {ok_count}, LOW: {low_count}, CRITICAL: {critical_count}")
    print(f"Total inventory value: #{sum(item['qty'] * item['price'] for item in inventory.values()):,.2f}")
    print(f"Total restock cost: #{sum(compute_restock(item) * item['price'] for item in inventory.values()):,.2f}")


if __name__ == "__main__":
    main()
