from flask import Flask, render_template, request, jsonify
from main import minifier

app = Flask(__name__)

# homepage route
@app.route("/")
def index():
	return render_template("index.html")

# ajax form submission route
@app.route("/format_text", methods=["POST"])
def formatText():
	data = request.get_json()
	inputText = data["text"]
	formattedText = minifier(inputText)
	return jsonify({"formattedText": formattedText})



if __name__ == "__main__":
	app.run()
