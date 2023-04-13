"""Virtual interactive closet that allows a user to choose their outfit based
on the weather."""

from argparse import ArgumentParser
import json


class Selection(Closet):
    """Child class for Closet, users selects outfit.
    """
    def choice(self):
        """User's choice based upon the weather.
        """
    
    def __repr__(self):
        return f"Because of the weather being {self.weather}, you decided upon this outfit: \
        {self.top} with {self.pants}, {self.shoes}, and {self.accessories}"


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.weather, args.tops, args.pants, args.shoes, args.accessories)


def main(filepath):
    """Opens the JSON file for reading and loads its contents.
    
    Args:
        filepath (str): string representing path to JSON file containing
        elements of a closet.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        closet = json.load(f)