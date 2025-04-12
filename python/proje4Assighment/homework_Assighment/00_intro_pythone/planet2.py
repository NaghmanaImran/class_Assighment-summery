# Milestone 2: All Planets

print("Planetary Weight Calculator")

def main():
    # Earth weight input
    earth_weight = float(input("Enter a weight on Earth: "))

    # Planet input
    planet = input("Enter a planet: ")

    # Gravity factors for each planet
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14,
    }

    # Check if planet exists in dictionary
    if planet in gravity_factors:
        weight_on_planet = earth_weight * gravity_factors[planet]
        rounded_weight = round(weight_on_planet, 2)  # ✅ Use `round`, not `Rounded`

        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Invalid planet name.")

# ✅ This part should be outside the function block (fixed indentation)
if __name__ == "__main__":
    main()
