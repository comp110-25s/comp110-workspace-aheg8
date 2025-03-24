"""Exercise 1 is programming a tea party for me and my friends."""

__author__: str = "730821126"


def main_planner(guests: int) -> None:
    """Entry point of the program. Summary ontop, details below."""
    print("A cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """The guests attending the party each require 2 tea bags."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed.
    Each guest requires 2 tea bags and 1.5 treats with each tea."""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea and treats required.
    Each tea bag costs $.50 and each treat costs $.75."""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
