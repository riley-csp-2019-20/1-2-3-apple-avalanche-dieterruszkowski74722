#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" 
ground_height =-200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
screen_width =400
screen_height =400

current_letter = "A"
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

active_letters = []
apple_list = []
number_of_apples = 5



current_letter = "A"


wn = trtl.Screen()
wn.addshape(apple_image) 
wn.setup(width=1.0, height=1.0)


wn.bgpic("tree.gif")
# apple = trtl.Turtle()
# apple.penup()
wn.tracer(False)

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list )
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, screen_width/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter)
    active_letters.append(current_letter)


def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  active_apple.showturtle()
  wn.update()

def drop_apple(letter):
  wn.tracer(True)
  index = active_letters.index(letter)
  active_letters.pop(index)

  active_apple = apple_list.pop(index)

  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  active_apple.hideturtle()
  wn.tracer(False)
  reset_apple(active_apple)

  apple_list.append(active_apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

for i in range(number_of_apples):
    active_apple = trtl.Turtle(shape = apple_image)
    active_apple.penup()
    reset_apple(active_apple)
    apple_list.append(active_apple)



def check_letter_a():
    if ("A" in active_letters):
        drop_apple("A")

def check_letter_b():
    if ("B" in active_letters):
        drop_apple("B")

def check_letter_c():
    if ("C" in active_letters):
        drop_apple("C")

def check_letter_d():
    if ("D" in active_letters):
        drop_apple("D")

def check_letter_e():
    if ("E" in active_letters):
        drop_apple("E")

def check_letter_f():
    if ("F" in active_letters):
        drop_apple("F")

def check_letter_g():
    if ("G" in active_letters):
        drop_apple("G")

def check_letter_h():
    if ("H" in active_letters):
        drop_apple("H")

def check_letter_i():
    if ("I" in active_letters):
        drop_apple("I")

def check_letter_j():
    if ("J" in active_letters):
        drop_apple("J")

def check_letter_k():
    if ("K" in active_letters):
        drop_apple("K")

def check_letter_l():
    if ("L" in active_letters):
        drop_apple("L")

def check_letter_m():
    if ("M" in active_letters):
        drop_apple("M")

def check_letter_n():
    if ("N" in active_letters):
        drop_apple("N")

def check_letter_o():
    if ("O" in active_letters):
        drop_apple("O")

def check_letter_p():
    if ("P" in active_letters):
        drop_apple("P")

def check_letter_q():
    if ("Q" in active_letters):
        drop_apple("Q")

def check_letter_r():
    if ("R" in active_letters):
        drop_apple("R")

def check_letter_s():
    if ("S" in active_letters):
        drop_apple("S")

def check_letter_t():
    if ("T" in active_letters):
        drop_apple("T")

def check_letter_u():
    if ("U" in active_letters):
        drop_apple("U")

def check_letter_v():
    if ("V" in active_letters):
        drop_apple("V")

def check_letter_w():
    if ("W" in active_letters):
        drop_apple("W")

def check_letter_x():
    if ("X" in active_letters):
        drop_apple("X")

def check_letter_y():
    if ("Y" in active_letters):
        drop_apple("Y")

def check_letter_z():
    if ("Z" in active_letters):
        drop_apple("Z")




wn.onkeypress(check_letter_a, "a")
wn.onkeypress(check_letter_b, "b")
wn.onkeypress(check_letter_c, "c")
wn.onkeypress(check_letter_d, "d")
wn.onkeypress(check_letter_e, "e")
wn.onkeypress(check_letter_f, "f")
wn.onkeypress(check_letter_g, "g")
wn.onkeypress(check_letter_h, "h")
wn.onkeypress(check_letter_i, "i")
wn.onkeypress(check_letter_j, "j")
wn.onkeypress(check_letter_k, "k")
wn.onkeypress(check_letter_l, "l")
wn.onkeypress(check_letter_m, "m")
wn.onkeypress(check_letter_n, "n")
wn.onkeypress(check_letter_o, "o")
wn.onkeypress(check_letter_p, "p")
wn.onkeypress(check_letter_q, "q")
wn.onkeypress(check_letter_r, "r")
wn.onkeypress(check_letter_s, "s")
wn.onkeypress(check_letter_t, "t")
wn.onkeypress(check_letter_u, "u")
wn.onkeypress(check_letter_v, "v")
wn.onkeypress(check_letter_w, "w")
wn.onkeypress(check_letter_x, "x")
wn.onkeypress(check_letter_y, "y")
wn.onkeypress(check_letter_z, "z")



wn.listen() 


trtl.mainloop()