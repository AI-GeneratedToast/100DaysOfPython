import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
screen.setup(height=600, width=750)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# State data
data = pandas.read_csv("50_states.csv")
states = data.state
states_list = states.tolist()

points = 0
game_on = True
while game_on:
    answer = turtle.textinput(title=f"{points}/50 States Correct", prompt="What's the name of the state")
    answer = answer.lower()

    for states in states_list:
        if answer == states.lower():
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == states]
            x = int(state_data.x)
            y = int(state_data.y)
            t.goto(x, y)
            t.write(answer)

            points += 1
            states_list.remove(states)

        if points == 50:
            print("You guessed all the states , congratulations !")
            game_on = False

        if answer == "Exit" :
            missing_states = [state for state in states_list]
            print(f"Theres {len(missing_states)} states missing")


turtle.mainloop()
