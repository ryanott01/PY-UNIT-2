from abc import ABC, abstractmethod
from pprint import pprint
import csv


with open("sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        pprint(row)

def get_icecreams(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_icecream(file, name):
    for icecream in get_icecreams(file):
        if icecream["name"] == name:
            return icecream
    return None

def add_icecream_dictionary(file, icecream):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "sprinkles", "topping"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(icecream)

def write_new_csv(file, icecreams):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "sprinkles", "topping"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for icecream in icecreams:
            if (icecreams == "epic"):
                return
            elif hasattr(icecream, "sprinkles"):
                writer.writerow({"size": icecream.size, "name": icecream.name, "price": icecream.price, "flavor": icecream.flavor, "topping": icecream.topping, "sprinkles": icecream.sprinkles})
            else:
                writer.writerow({"size": icecream.size, "name": icecream.name, "price": icecream.price, "flavor": icecream.flavor, "topping": icecream.topping})

def add_icecream(file, icecreams):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "sprinkles", "topping"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(icecream, "sprinkles"):
            writer.writerow({"size": icecream.size, "name": icecream.name, "price": icecream.price, "flavor": icecream.flavor, "topping": icecream.topping, "sprinkles": icecream.sprinkles})
        else:
            writer.writerow({"size": icecream.size, "name": icecream.name, "price": icecream.price, "flavor": icecream.flavor, "topping": icecream.topping})


class Icecream(ABC):
    def __init__(self, name, price, flavor, topping):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.topping = topping
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self):
        return self.price

class Regular(Icecream):
    size = "regular"
    def __init__(self, name, price, flavor, topping):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.topping = topping
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


class Mini(Icecream):
    size = "mini"
    def __init__(self, name, price, flavor, topping):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.topping = topping
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return quantity * self.price


# my_icecream_mini = Mini("Chocolate Brownie", 1.99, "Chocolate", "Brownie")

# my_icecream_regular = Regular("Chocolate Brownie", 3.99, "Chocolate", "Brownie")

# my_icecream_regular.add_sprinkles("Chocolate", "Brownie Crumbs")

# print(my_icecream_regular.sprinkles)

# print(my_icecream_mini.name)
# print(my_icecream_mini.size)
# print(my_icecream_mini.price)


# icecream_list =[
#     my_icecream_mini,
#     my_icecream_regular
# ]

# write_new_csv("sample.csv", icecream_list)
