def calculate_pay():
    base_pay = 20.50
    tax_rate = 16.7597 / 100

    # Input for Sunday to Thursday shifts
    weekday_total = 0.0
    ans = input("Did you work any shifts from Sunday to Thursday? (yes/no): ").strip().lower()
    if ans == "yes":
        print("Enter the hours for each shift from Sunday to Thursday. Type 'done' when finished.")
        while True:
            entry = input("Enter hours for a shift (or type 'done'): ").strip()
            if entry.lower() == 'done':
                break
            try:
                hours = float(entry)
                weekday_total += hours
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Input for Friday and Saturday shifts
    weekend_total = 0.0
    ans = input("Did you work any shifts on Friday and Saturday? (yes/no): ").strip().lower()
    if ans == "yes":
        print("Enter the hours for each shift on Friday and Saturday. Type 'done' when finished.")
        while True:
            entry = input("Enter hours for a shift (or type 'done'): ").strip()
            if entry.lower() == 'done':
                break
            try:
                hours = float(entry)
                weekend_total += hours
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Calculate pay for Sunday-Thursday shifts (weekday bonus rates)
    bonus_weekday_first_4 = 1.50
    bonus_weekday_next = 2.00
    first_4_weekday = min(4, weekday_total) * (base_pay + bonus_weekday_first_4)
    remaining_weekday = max(0, weekday_total - 4) * (base_pay + bonus_weekday_next)
    total_weekday_pay = first_4_weekday + remaining_weekday

    # Calculate pay for Friday-Saturday shifts (weekend bonus rates)
    bonus_weekend_first_4 = 2.50
    bonus_weekend_next = 3.00
    first_4_weekend = min(4, weekend_total) * (base_pay + bonus_weekend_first_4)
    remaining_weekend = max(0, weekend_total - 4) * (base_pay + bonus_weekend_next)
    total_weekend_pay = first_4_weekend + remaining_weekend

    # Total calculations
    total_hours = weekday_total + weekend_total
    total_pay = total_weekday_pay + total_weekend_pay
    net_pay = total_pay * (1 - tax_rate)

    # Print the results
    print("\n--- Pay Summary ---")
    print(f"Total hours worked: {total_hours}")
    print(f"Hours worked from Sunday to Thursday: {weekday_total}")
    print(f"Hours worked on Friday and Saturday: {weekend_total}")
    print(f"Total pay before tax: ${total_pay:.2f}")
    print(f"Net pay after tax: ${net_pay:.2f}")

# Call the function
calculate_pay()
