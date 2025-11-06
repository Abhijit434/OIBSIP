def get_positive_float(prompt):
    while True:
        try:
            raw = input(prompt).strip()
            value = float(raw)
            if value <= 0:
                print("  → Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("  → That doesn't look like a number. Please enter a numeric value (e.g., 70.5).")

def get_height_meters(prompt, min_m=0.5, max_m=2.5):
    while True:
        try:
            raw = input(prompt).strip()
            h = float(raw)
            if h < min_m or h > max_m:
                print(f"  → Please enter a height between {min_m} m and {max_m} m.")
                continue
            return h
        except ValueError:
            print("  → That doesn't look like a number. Please enter a numeric value (e.g., 1.75).")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator 👋")
    print("I'll ask for your weight (kg) and height (m), then compute your BMI.\n")

    try:
        weight = get_positive_float("Enter your weight in kilograms (kg): ")
        height = get_height_meters("Enter your height in meters (m) [e.g., 1.75]: ")

        bmi = weight / (height ** 2)
        category = categorize_bmi(bmi)

        print("\n--- Result ---")
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("---------------")
    except KeyboardInterrupt:
        print("\n\nInput cancelled by user. Exiting.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
