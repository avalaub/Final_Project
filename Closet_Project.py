"""Virtual interactive closet that allows a user to choose their outfit based
on the weather."""

from argparse import ArgumentParser
import sys
import json

class Closet:
    """This is the closet of items that will reveal what is in it and the options for the item for the corresponding weather"""
    def __init__(self, tops, pants,  shoes, accessories):
        """This will initialize the items that are in the JSON file from the closet and the categories that are listed
        Args:
            tops(str): the tops in the JSON closet
            pants(str): the pants in the JSON closet 
            shoes(str): the shoes in the JSON closet 
            accessories(str): the accessories in the JSON closet 
        
        """
        self.tops = tops
        self.pants = pants
        self.shoes = shoes
        self.accessories = accessories

    def getKeys(self, value):
        """This will reveal what the weather is to the corresponding key of the item in the closet.
        Returns:
            Keys of the items in the dictionary. """
        myList = []
        for item in self.tops:
            val = self.tops[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                for elem in val:
                    if elem == value:
                        myList.append(item)
        for item in self.pants:
            val = self.pants[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                for elem in val:
                    if elem == value:
                        myList.append(item)
        for item in self.shoes:
            val = self.shoes[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                for elem in val:
                    if elem == value:
                        myList.append(item)
        for item in self.accessories:
            val = self.accessories[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                for elem in val:
                    if elem == value:
                        myList.append(item)
            
    def options(self):
        """ This will show what are the options for the category based on the """
        

class Selection(Closet):
    """Child class for Closet, user selects outfit.
    
    Attributes:
        final_top(str): final choice for tops.
        final_pants(str): final choice for pants.
        final_shoes(str): final choice for shoes.
        final_accessories(str): final choice for accessories.
    """
    def weather(self):
        """Weather for today.
        
        Returns:
            user_weather(str): User input for weather.
        """
        user_weather = input("What is the weather today? Please answer sunny, rainy, or cold!")
        self.weather = user_weather
        if isinstance(user_weather, str) == False:
            raise TypeError("Weather is a str; must be sunny, rainy, or cold")
        elif user_weather != "sunny" or user_weather != "rainy" or user_weather != "cold":
            raise ValueError("Weather must be sunny, rainy, or cold")
        else:
            return f"The weather for today is {user_weather}."
    
    def options(self, user_weather, tops, pants, shoes, accessories):
        """User's options based upon the weather.
        
        Args: 
            user_weather(str): User input for weather.
            tops(dict): dictorionary of tops in closet.
            pants(dict): dictorionary of pants in closet.
            shoes(dict): dictorionary of shoes in closet.
            accessories(dict): dictorionary of accessories in closet.
        """
        if user_weather == "sunny":
            options_tops = list(filter(lambda x: tops[x] == "sunny", tops))
            options_pants = list(filter(lambda x: pants[x] == "sunny", pants))
            options_shoes = list(filter(lambda x: shoes[x] == "sunny", shoes))
            options_accessories = \
            list(filter(lambda x: accessories[x] == "sunny", accessories))
        elif user_weather == "rainy":
            options_tops = list(filter(lambda x: tops[x] == "rainy", tops))
            options_pants = list(filter(lambda x: pants[x] == "rainy", pants))
            options_shoes = list(filter(lambda x: shoes[x] == "rainy", shoes))
            options_accessories = \
            list(filter(lambda x: accessories[x] == "rainy", accessories))
        elif user_weather == "cold":
            options_tops = list(filter(lambda x: tops[x] == "cold", tops))
            options_pants = list(filter(lambda x: pants[x] == "cold", pants))
            options_shoes = list(filter(lambda x: shoes[x] == "cold", shoes))
            options_accessories = \
            list(filter(lambda x: accessories[x] == "cold", accessories))
        
        print(f"Since the weather is {user_weather}, these are your options. For tops: \
              {options_tops}, for pants: {options_pants}, for shoes: {options_shoes}, \
              for accessories: {options_accessories}")
    
    def choice(self, final_tops, final_pants, final_shoes, final_accessories):
        """User's choice of clothes.

        Args:
            final_top(str): final choice for tops.
            final_pants(str): final choice for pants.
            final_shoes(str): final choice for shoes.
            final_accessories(str): final choice for accessories.
        
        Side effects:
            redefined `self.tops`
            redefined `self.pants`
            redefined `self.shoes`
            redefined `self.accessories`
        """
        self.tops = final_tops
        self.pants = final_pants
        self.shoes = final_shoes
        self.accessories = final_accessories

        outfit = self.tops + self.pants + self.shoes + self.accessories
    
    def __repr__(self):
        return f"Because of the weather being {self.weather}, you decided upon this outfit: \
        {self.tops} with {self.pants}, {self.shoes}, and {self.accessories}"
        
    def decide():
        print("Are you happy with your outfit?") if
        
    

def main(filepath):
    """Opens the JSON file for reading and loads its contents.
    
    Args:
        filepath (str): string representing path to JSON file containing
        elements of a closet.
    """
    with open(filepath, "r", encoding ="utf-8") as f:
        closet = json.load(f)


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect six mandatory arguments:
        The path to a file of clothing options
        The weather (either rainy, sunny, or cold)
        The top you want to wear from the file of clothing options
        The pants you want to wear from the file of clothing options
        The shoes you want to wear from the file of clothing options
        The accessories you want to wear from the file of clothing options
    
    Args:
         arglist (list of str): command-line arguments.

    Returns:
        namespace: an object with six attributes, filepath, weather, tops,
            pants, shoes, accessories.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="file with clothing options")
    parser.add_argument("weather", help="Weather is rainy, sunny, or cold")
    parser.add_argument("tops", help="top you want to wear")
    parser.add_argument("pants", help="pants you want to wear")
    parser.add_argument("shoes", help="shoes you want to wear")
    parser.add_argument("accessories", help="accessories you want to wear")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.weather, args.tops, args.pants, args.shoes, 
         args.accessories)
