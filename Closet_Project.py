"""Virtual interactive closet that allows a user to choose their outfit based
on the weather."""
from argparse import ArgumentParser
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt


class Closet:
    """Closet of all clothing items available for the user to choose based upon 
    the weather.
    
    Attributes:
        tops(str): the tops defined in the JSON file.
        pants(str): the pants defined in the JSON file.
        shoes(str): the shoes defined in the JSON file.
        accessories(str): the accessories defined in the JSON file.
    """
    
    
    def __init__(self, tops, pants,  shoes, accessories):
        """Initializes the tops, pants, shoes, and accessories attributes.
        
        Args:
            tops(str): the tops defined in the JSON file.
            pants(str): the pants defined in the JSON file.
            shoes(str): the shoes defined in the JSON file.
            accessories(str): the accessories defined in the JSON file.
            
        Side effects:
            Sets attributes tops, pants, shoes, and accessories.
        """
        self.tops = tops
        self.pants = pants
        self.shoes = shoes
        self.accessories = accessories

    
    def getKeys(self, value, choice):
        """Matches the weather selected to the corresponding key of the item in
        the JSON file.
        
        Args:
            value(str): clothing items in the JSON file.
        
        Side effects:
            appends myList with instances of items in the JSON file.
            prints myList which is a list containing the clothing items of the
            JSON file that correspond with the weather the user selects.
        """
        myList = []
        for item in choice:
            val = choice[item]
            if isinstance(val, str):
                if value == val:
                    myList.append(item)
            else:    
                myList.extend([item for elem in val if elem == value])
        print(myList)
        return myList
            

class Selection(Closet):
    """Child class for Closet, user selects outfit.
    
    Attributes:
        final_top(str): final choice for tops.
        final_pants(str): final choice for pants.
        final_shoes(str): final choice for shoes.
        final_accessories(str): final choice for accessories.
    """
    
    def weather(self, dfweather = None):
        """Prompts user to input the weather from the options sunny, rainy, or
        cold.
        
        Args:
            dfweather (str):
            
        Raises:
            TypeError: Weather is another string; must be sunny, rainy, or cold
        
        Side effects:
            prints error.
        
        Returns:
            user_weather(str): User input for weather.
        """
        while True:
            if dfweather == None:
                try:
                    user_weather = input("Is the weather today sunny, rainy, or cold? Please answer in lowercase! ")
                    if user_weather not in ['sunny', 'rainy', 'cold']:
                        raise TypeError("Weather is another string; must be sunny, rainy, or cold.")
                    return user_weather
                except TypeError as error:
                    print(error)
            else:
                user_weather = dfweather
    
    
    def temperature(self, df):
        """Uses the dataframe established in graph function to allow the user to
        plan their outfit for a future day.
        
        Args:
            df
            
        Returns:
            rainy(str):
            sunny(str):
            cold(str):
        """
        
        day = int(input("How many days ahead would you like to plan your outfit for?")) - 1
        weatherdf = dict()
        i = 0
        while i < len(df.iloc[day]):
            if i == 0:
                weatherdf["day"] = df.iloc[day][0]
            elif i == 1:
                weatherdf["low"] = df.iloc[day][1]
            elif i == 2:
                weatherdf["high"] = df.iloc[day][2]
            else:
                weatherdf["precip"] = df.iloc[day][3]
            i += 1
        print(weatherdf)
        cold = df.iloc[day][1]
        sunny = df.iloc[day][2]
        rainy = df.iloc[day][3]
        
        if rainy > 70:
            print("The day you chose is Rainy!")
            return "rainy"
        elif sunny > 60:
            print("The day you chose is Sunny!")
            return "sunny"
        elif cold < 60:
            print("The day you chose is Cold!")
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
        
        
    
    
    def choice(self, options_tops, options_pants, options_shoes, options_accessories):
        """User's choice of clothes.

        Args:
            final_top(str): final choice for tops.
            final_pants(str): final choice for pants.
            final_shoes(str): final choice for shoes.
            final_accessories(str): final choice for accessories.
            
        Raises:
            ValueError: Given answer not in options.
        
        Side effects:
            redefined `self.tops`
            redefined `self.pants`
            redefined `self.shoes`
            redefined `self.accessories`
            
        Returns:
            outfit(str): self.tops, self.pants, self.shoes, self.accessories
        """
        #print(f"For tops:{options_tops}")
        #print(f"For pants:{options_pants}")
        #print(f"For shoes:{options_shoes}")
       # print(f"For accessories:{options_accessories}")
        
        final_tops = input("What top would you like to wear? Please type your answer in lower case! ")
        
        if final_tops not in options_tops:
            raise ValueError("Given answer not in options.")
        final_pants = input("What pants would you like to wear? Please type your answer in lower case! ")
        
        if final_pants not in options_pants:
            raise ValueError("Given answer not in options.")
        final_shoes = input("What shoes would you like to wear? Please type your answer in lower case! ")
        
        if final_shoes not in options_shoes:
            raise ValueError("Given answer not in options.")
        final_accessories = input("What accessory would you like to wear? Please type your answer in lower case! ")
        
        if final_accessories not in options_accessories:
            raise ValueError("Given answer not in options.")
        
        self.tops = final_tops
        self.pants = final_pants
        self.shoes = final_shoes
        self.accessories = final_accessories

        outfit = (self.tops, self.pants, self.shoes, self.accessories)
        return outfit
    
    
    def __repr__(self):
        """
        
        Returns:
        """
        return f"""You decided upon this outfit:
        {self.tops}, {self.pants}, {self.shoes}, and {self.accessories}
        """
        
    
    def decide(self, closet, df):
        """
        """
        user_decision = input("Are you happy with your outfit? Please answer yes or no.")


        print("Glad you like your outfit!") if user_decision == "yes" else iteration(closet, df)
        
def iteration(closet:Closet, df:pd.read_csv("march_weather.csv")):
    """Allows user to choose if they would like to select an outfit for the
    current day or a day in the near future.
    
    Args:
        closet:Closet:
        df:pd.read_csv("march_weather.csv"):
        
    Side effects:
        prints statement "Welcome to Virtual Closet!".
        
    """
    print("Welcome to Virtual Closet!")
    decision = int(input("""
    1: Please type 1 if you would like to select an outfit for today!
    2: Please type 2 if you would like to select an outfit for a certain number of days after today!
    """))
    
    if decision == 1:
        select = Selection(closet.tops, closet.pants, closet.shoes, closet.accessories)
        user_weather = select.weather()
        select.getKeys(user_weather, closet.tops)
        select.getKeys(user_weather, closet.pants)
        select.getKeys(user_weather, closet.shoes)
        select.getKeys(user_weather, closet.accessories)
        select.choice(closet.tops, closet.pants, closet.shoes, closet.accessories)
        print(repr(select))
        select.decide(closet, df)
    
    elif decision == 2:
        select = Selection(closet.tops, closet.pants, closet.shoes, closet.accessories)
        odweather = select.temperature(df)
        select.getKeys(odweather, closet.tops)
        select.getKeys(odweather, closet.pants)
        select.getKeys(odweather, closet.shoes)
        select.getKeys(odweather, closet.accessories)
        select.choice(closet.tops, closet.pants, closet.shoes, closet.accessories)
        print(repr(select))
        select.decide(closet, df)
        
                   
def graph(file):
    """
    """
    
    df = pd.read_csv(file)
    
    plt.bar(df["day"], df["precip"])
    plt.xlabel('day')
    plt.ylabel('percip')
    plt.show() 

    
def main(filepath1, filepath2):
    """Opens the JSON file for reading and loads its contents.
    
    Args:
        filepath1(str): string representing path to JSON file containing
        elements of a closet.
        filepath2(str): graph containing data from a csv file.
    """
    graph(filepath2)    
    with open(filepath1, "r", encoding ="utf-8") as f:
        closetdata = json.load(f)
        closet = Closet(closetdata['tops'], closetdata['pants'], closetdata['shoes'], closetdata['accessories'])
        df = pd.read_csv(filepath2)
        iteration(closet, df)



def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect six mandatory arguments:
        The path to a file of clothing options
    
    Args:
         arglist (list of str): command-line arguments.

    Returns:
        namespace: an object with six attributes, filepath, weather, tops,
            pants, shoes, accessories.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="file with clothing options")
    parser.add_argument("filepath2", help="file with weather data")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath, args.filepath2)
