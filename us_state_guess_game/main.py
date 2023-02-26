import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("US States Games")
image = "./blank_states_img.gif"                #link to the image
screen.addshape(image)                          #add shape to turtle
turtle.shape(image)

"""#get mouse click on coordination
def get_mouse_click_coor(x,y):
    print(x,y)


turtle.onscreenclick(get_mouse_click_coor) #get got clicked it will listen to function getmouseclickcoor and pass x,y

turtle.mainloop() ##keep the screen open"""


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#print(answer_state)
correct_guess =0
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_state = []


#print(state_list)
while correct_guess < len(state_list):
    if answer_state.title() in state_list:
        correct_guess +=1
        guessed_state.append(answer_state.title())
        row = data[data["state"] == answer_state.title()]
        x_coor = int(row.x)
        y_coor = int(row.y)
        turtle1 = turtle.Turtle()
        turtle1.hideturtle()
        turtle1.penup()
        turtle1.goto(x_coor,y_coor)
        turtle1.write(f"{answer_state.title()}", True, align = "center")  #or answer_state == data.state.item() Grab the first item in the data row
    answer_state = screen.textinput(title=f"{correct_guess}/{len(state_list)} States Correct",
                                        prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break









turtle.exitonclick()
