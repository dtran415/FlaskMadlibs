from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"

@app.route("/")
def get_inputs():
    """ Get words for madlibs """

    prompts = story.prompts

    return render_template("inputs.html", prompts=prompts)


@app.route("/story")
def generate_story():
    """ Generate a story with the given words """

    text = story.generate(request.args)
    
    return render_template("story.html", text=text)