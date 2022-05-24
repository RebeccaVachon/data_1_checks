from tkinter import N


print ("Hello World")

Flavors = ["Key Lime Pie", "Strawberry Cheesecake", "Cookies and Cream", "S'mores"]

Pets = {
    "rabbit": "Wilson",
    "fish": "Swimmy",
    "dog": "Teddy",
}

morning_routine = ("wake-up", "eat breakfast", "go for a walk", "check email",)

import random
yogurt = random.choice(Flavors)

print ("I like to name my pets after presidents.")
print ("I have a dog named " + Pets["dog"] + " after Theodore Roosevelt. I also have a bunny named " + Pets["rabbit"] + " after Woodrow Wilson." )
print ("Today I will have yogurt for a snack. I bought a variety pack, so each day I get a new flavor. Today I will try " + yogurt + ".")
print ("After I " + (morning_routine[1]) + ", I will " + (morning_routine[2]) + ".")