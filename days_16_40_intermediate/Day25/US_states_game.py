import pandas
from turtle import Screen, shape, mainloop, Turtle

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

# with these functions we can create the data in the 50_states.csv file

# def get_mouse_click_coord(x, y):
#     print(x, y)

# onscreenclick(get_mouse_click_coord)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        # saves state to learn in a csv file for further study

        missing_states = [state for state in states if state not in guessed_states]
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

# improvements :
# include an automatic save of the already guessed states. So you can run the game again later and complete it
# Added the missing states to the map in red
