"""Virtual interactive closet that allows a user to choose their outfit based
on the weather."""

from argparse import ArgumentParser
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt


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
        """This will reveal what the weather is to the corresponding key of the item in the closet
        Returns:
            Keys of the items in the dictionary 
        """
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
                myList.extend([item for elem in val if elem == value])
        for item in self.pants:
            val = self.pants[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                myList.extend([item for elem in val if elem == value])
        for item in self.shoes:
            val = self.shoes[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                myList.extend([item for elem in val if elem == value])
        for item in self.accessories:
            val = self.accessories[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:
                myList.extend([item for elem in val if elem == value])
        return myList
            
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
    def weather(self, dfweather = None):
        """Weather for today.
        
        Returns:
            user_weather(str): User input for weather.
        """
        while True:
            if dfweather == None:
                try:
                    user_weather = input("What is the weather today? Please answer sunny, rainy, or cold!")
                    if user_weather not in ['sunny', 'rainy', 'cold']:
                        raise TypeError("Weather is another string; must be sunny, rainy, or cold")
                    return user_weather
                    #break
                except TypeError as error:
                    print(error)
            else:
                user_weather = dfweather
    
    def temperature(self, df):
        """Prints a dataframe based on how many days into the future the user
            chooses 
        
        Args:
            df: the dataframe 
        
        Returns:
            "rainy" (string): if the number in the "precip" column in the csv file is 
                higher than 70
            "sunny" (string): if the number in the "high" column in the csv file is 
                higher than 60
            "cold" (string): if the number in the "precip" column in the csv file is 
                lower than 60
        """
        day = int(input("Do you want to plan your outfit for a future data. If so, what day?")) - 1
        
        print(df.iloc[day])
        cold = df.iloc[day][1]
        sunny = df.iloc[day][2]
        rainy = df.iloc[day][3]
        
        if rainy > 70:
            print("The day you chose is Rainy")
            return "rainy"
        elif sunny > 60:
            print("The day you chose is Sunny")
            return "sunny"
        elif cold < 60:
            print("The day you chose is Cold")
            return "cold"
    
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
    
    def choice(self, options_tops, options_pants, options_shoes, options_accessories):
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
        final_tops = input("What top would you like to wear? Please type answer in lower case!")
        if final_tops not in options_tops:
            raise ValueError("Given answer not in options.")
        final_pants = input("What pants would you like to wear? Please type answer in lower case!")
        if final_pants not in options_pants:
            raise ValueError("Given answer not in options.")
        final_shoes = input("What shoes would you like to wear? Please type answer in lower case!")
        if final_shoes not in options_shoes:
            raise ValueError("Given answer not in options.")
        final_accessories = input("What accessory would you like to wear? Please type answer in lower case!")
        if final_accessories not in options_accessories:
            raise ValueError("Given answer not in options.")
        self.tops = final_tops
        self.pants = final_pants
        self.shoes = final_shoes
        self.accessories = final_accessories

        outfit = (self.tops, self.pants, self.shoes, self.accessories)
        return outfit
    
    def __repr__(self):
        return f"You decided upon this outfit: \
        {self.tops} with {self.pants}, {self.shoes}, and {self.accessories}"
        
    def decide(self, closet:Closet):
        user_decision = input("Are you happy with your outfit? Please answer yes or no.")

        while user_decision != "yes":
            print("Glad you like your outfit!") if user_decision == "yes" else iteration(closet, df)
            break
        

def iteration(closet:Closet, df):
    decision = int(input("""
    1: Select outfit for today
    2: Select outfit for a certain number of days after today
    """))
    if decision == 1:
        select = Selection(closet.tops, closet.pants, closet.shoes, 
                           closet.accessories)
        user_weather = select.weather()
        select.options(user_weather, closet.tops, closet.pants, 
                       closet.shoes, closet.accessories)
        select.choice(closet.tops, closet.pants, closet.shoes, 
                      closet.accessories)
        print(repr(select))
        select.decide(closet)
    elif decision == 2:
        select = Selection(closet.tops, closet.pants, closet.shoes, 
                           closet.accessories)
        odweather = select.temperature(df)
        select.weather(odweather)
              
def graph(file):
    df = pd.read_csv(file)
    
    plt.bar(df["day"], df["precip"])
    plt.show()
    
def main(filepath1, filepath2):
    """Opens the JSON file for reading and loads its contents.
    
    Args:
        filepath (str): string representing path to JSON file containing
        elements of a closet.
    """
    graph(filepath2)    
    with open(filepath1, "r", encoding ="utf-8") as f:
        closetdata = json.load(f)
        closet = Closet(closetdata['tops'], closetdata['pants'], 
                        closetdata['shoes'], closetdata['accessories'])
        print(closet)

        df = pd.read_csv(filepath2)
        iteration(closet, df)


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect two mandatory arguments:
        The path to a file of clothing options
        The path to the csv file with temperature
    
    Args:
         arglist (list of str): command-line arguments.

    Returns:
        namespace: an object with two attributes, filepath, filepath2
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="file with clothing options")
    parser.add_argument("filepath2", help="file with weather data")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.filepath2)
