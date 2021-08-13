# Project 25 - U.S. States Game

from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("Name of the States")
image = "blank_states_img.gif"
screen.addshape(image)
img_turtle = Turtle(image)

score = 0

df = pd.read_csv("50_states.csv")
states_list = df["state"].to_list()
guessed_states = []

while score <= 50:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What,s the another state name?")
    answer_state = str(answer).title()

    if answer_state == "Quit" or answer_state == "Exit":
        # states to learn
        # alternative 1
        # missing_states = states_list
        # for g_state in guessed_states:
        #     missing_states.remove(g_state)

        # alternative 2
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        missing_states = [state for state in states_list if state not in guessed_states]

        state_to_learn = {
            "Learning_State": missing_states
        }

        learning_state = pd.DataFrame(state_to_learn)
        learning_state.to_csv("learning_state.csv")
        break

    else:
        for num in range(0, len(states_list)):
            state = states_list[num]
            if answer_state == state:
                state_data = df[df.state == state]
                x_coor = state_data["x"][num]
                y_coor = state_data["y"][num]

                turtle = Turtle()
                turtle.hideturtle()
                turtle.penup()
                turtle.goto(x_coor, y_coor)
                turtle.write(state)

                score += 1
                guessed_state = state_data["state"].item()
                guessed_states.append(guessed_state)


