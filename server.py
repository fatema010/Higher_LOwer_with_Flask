from flask import Flask
import random
number = random.randint(0,9)
print(number)

app = Flask(__name__)
@app.route("/")
def hello():
    return '<h1 style="text-align: center">"Guess a number between 0 and 9" </h1>'\
           '<img align="middle" width="350" src = "https://media4.giphy.com/media/Cnj6KKwag9FshBuJK5/giphy.gif?cid=790b7611ab96b47502ff5a1f2a665b4988cc56dd3ddee322&amp;rid=giphy.gif&amp" height = "320">'
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return '<h1 style="color:blue"> Too High, Try again!</h1>'\
                "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)