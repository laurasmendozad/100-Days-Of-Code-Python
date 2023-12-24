''' U.S. States Game '''
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = r"ProjectsPerDay\Day 025\Project - U.S. States Game\blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
score = 0
guessed_states = []
states = pd.read_csv(r"ProjectsPerDay\Day 025\Project - U.S. States Game\50_states.csv")
all_states = states.state.to_list()

while score < len(states.state)-1:
    answer_state = screen.textinput(title=f"{score}/{len(states.state)} States Correct",
                                prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states = pd.DataFrame(missing_states)
        missing_states.to_csv("ProjectsPerDay\Day 025\Project - U.S. States Game\states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = states[states["state"] == answer_state]
        guessed_states.append(answer_state)
        t.color('black')
        style = ('Courier', 8, 'normal')
        t.goto(int(state.x),int(state.y))
        t.write(answer_state, font=style, align='center')
        score += 1

screen.exitonclick()
