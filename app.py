from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def analytics():
    query = request.form["query"]
    return analytics(query)

if __name__ == "__main__":
    app.run()