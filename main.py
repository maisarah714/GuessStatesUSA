import turtle
from turtle import Screen, Turtle
import pandas

# to get coordinate by clicking on screen
# def get_coordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_coordinate)
# turtle.mainloop()

image = "blank_states_img.gif"

screen = Screen()
screen.addshape(image)

turtle.shape(image)

correct_state = []
states_data = pandas.read_csv('50_states.csv')
state_list = states_data.state.to_list()
while len(correct_state) < 50:
    guess_state = screen.textinput(title=f"{len(correct_state)}/50 States Correct",
                                   prompt="What's a state name: ").title()

    if guess_state == 'Exit':
        # comprehensive way
        # state_to_learn = []
        # for state in state_list:
        #     if state not in correct_state:
        #         state_to_learn.append(state)
        # compact way
        state_to_learn = [state for state in state_list if state not in correct_state]
        df_state_learn = pandas.DataFrame(state_to_learn)
        df_state_learn.to_csv("state_to_learn.csv")
        break

    if guess_state in state_list and guess_state not in correct_state:
        correct_state.append(guess_state)
        state = states_data[states_data['state'] == guess_state]
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        X_pos = int(state.x)
        Y_pos = int(state.y)
        new_state.goto(X_pos, Y_pos)
        new_state.write(guess_state, font=("Arial", 12, "normal"), align="center")
