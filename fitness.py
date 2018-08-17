"""
finalproject.py
This is a program which is designed to help peple who need to lose weight
Author: Xuantong Liu, Jiayao Song, Yunan Zhao
Date: 05/02/2017
"""
import random

underweight = ["You BMI is too low. You do not need to lose weight. Bye",
            "It will be unhealthy for you to lose wieght. You are thin enough. Bye",
            "Instead of losing weight, You need to eat more and gain some wegiht! Bye",
            "You are thin enough. Maybe you can try to do some sports, but eat more! Bye"]

normal = ["Your BMI is perfect! You are not necessary to lose weight. Bye",
        "Your BMI is good. Losing weight is not healthy for you. Bye",
        "You can try to do some sports, but promise me, do not lose too much weight. You will be unhealthy. Bye",
        "Your BMI is good. You are healthy and you don't need to lose weight. Bye"]

fat_responses =    {"Classic Dieting": "You can try the classic dieting method. You should eat a lot of fruit, vegetables, whole grains and fish everyday",
                    "Hunger No More": "I recommend you to fill up on fish, chicken, beans, and tofu, just eat more protein",
                    "Fat-Burner:Light": "I recommend you to use the Fat-Burner method. Gently phase into ketesis and trick your body into burning fat instead of sugar",
                    "The 2-Day Blaster": "I recommend you to use the 2-day balster method. You can eat nomrally 5 days a week. For the 2 balster day, eat only low-calorie foods like greens, fruit, and berries",
                    "Whole & Healthy": "You can try the Whole&Healthy method. You should eat only greens, fruit, whole grains, and proten-food in its most natural state"}

sports_calories = {'bicycle':429,'ropejumping':429,
                    'climbingstairs':399,'yoga':147,
                    'basketball':406,'football':443,
                    'volleyball':347,'badminton':332,
                    'tennis':295,'HIIT':575,'fencing':335,
                    'elliptical':527,'walking':295,
                    'running':406,'swimming':406,'dancing':369}

def main():
    """This is the mean function"""
    print("This is a program that can help you to lose weight")
    print('Tell me something about your diet progress')
    user_response = input(">> ")
    while user_response != "bye":
        calculation(user_response);
        user_response = input(">> ");

def calculation(user_response):
    """Takes a number as your weight in kilogram and another number as your height in metric form and calculates the BMI value of your weight"""
    print('It is good to hear about your diet progress' )
    print("Let me test your BMI first. I need to make sure whether you need to lose weight.")
    weight = int(input("Please input your weight in kg "))
    height = int(input("please input your height in cm "))
    BMI = weight*10000/height**2
    if BMI <= 0:
        print("Your input is wrong")
    elif 0<BMI<18.5:
        print(random.choice(underweight))
    elif 18.5<= BMI < 25:
        print(random.choice(normal))
    else:
        diet_plan(user_response);

def diet_plan(user_response):
    """Takes the user's preference of diet as an argument and returns the detailed information about the diet"""
    print("Your BMI is higher than average. I can help you to lose weight")
    print("Which methods do you prefer to lose weight?")
    print("Your answer should include classic/protein/fat/easiest/natural/sports")
    answer = input("answer")
    answers = answer.split()
    for x in answers:
        if x == "classic":
            print(fat_responses["Classic Dieting"])
        elif x == "protein":
            protein(user_response);
        elif x == "fat":
            print(fat_responses["Fat-Burner:Light"])
        elif x == "easiest":
            print(fat_responses["The 2-Day Blaster"])
        elif x == "natural":
            print(fat_responses[ "Whole & Healthy"])
        elif x == "sports":
            sport(user_response);


def sport(user_response):
    """Takes the user's prefered sport as an argument and returns the calories the sport consumes in the unit of kcal/hour"""
    print("Sports are really essential on losing weight!")
    print("Tell me your fav sports. I will tell how many calories it consumes per hour ")
    print("You can choose between badminton/basketball/bicycle")
    print("climbingstairs/dancing/elliptical/fencing/football/HIIT/volleyball")
    respond = input("ropejumping/running/swimming/tennis/walking/yoga ")
    responds = respond.split()
    calories = [sports_calories[a] for a in sports_calories if a in responds]
    print('Your fav sports will help you burn',calories,'per hour')

def protein(user_response):
    """Takes the users's weight as an argument and returns the quantity of protein the user needs to intake per day"""
    print("Good! A protein diet is helpful for your whole diet process.")
    print("Let me calculate how many g of protein you should intake")
    weight = int(input("Please input your weight again in kg e.g.70 "))
    protein1 = 2*weight
    print("You should intake", protein1,"g of protein per day.")
    print(fat_responses['Hunger No More'])

main()
