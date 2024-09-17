from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# homepage route
@app.route("/")
def index():
	return render_template("index.html")

# ajax form submission route
@app.route("/format_text", methods=["POST"])
def format_text():
	data = request.get_json()
	input_text = data["text"]
	formatted_text = input_text.upper()
	return jsonify({"formatted_text": formatted_text})



if __name__ == "__main__":
	app.run(debug=True)
