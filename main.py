import turtle
import pandas as pd

window = turtle.Screen()
window.title("U.S. States Game")
image = "blank_states_img.gif"
window.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

myturtle = turtle.Turtle()
myturtle.hideturtle()
myturtle.penup()


while len(guessed_states) < 50:
    answer_state = window.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another "
                                                                                             "state's name? ").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x_coordinate = state_data.x.item()
        y_coordinate = state_data.y.item()
        myturtle.goto(x_coordinate, y_coordinate)
        myturtle.write(arg=state_data.state.item())
        all_states.remove(answer_state)

df_of_missing_states = pd.DataFrame(all_states)
df_of_missing_states.to_csv("states_to_learn.csv")
