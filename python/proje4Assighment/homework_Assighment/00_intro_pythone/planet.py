print('Planetary Weight Calculator')

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * 0.378
    rounded_weight = round(mars_weight, 2)
    print('The equivalent on Mars:', rounded_weight)

if __name__ == '__main__':
    main()
