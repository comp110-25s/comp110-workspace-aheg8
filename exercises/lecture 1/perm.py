def perimeter(length=10, width=5) -> float:
    """Calculates the perimeter of a rectangle."""
    return 2 * length + 2 * width


print(perimeter(length=10, width=5))


def fuel_needed(distance: int, mpg: int) -> float:
    distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
