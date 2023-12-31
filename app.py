from flask import Flask, render_template, request
from langchain_helper import answer

app = Flask(__name__)
count = 0
datasetLoc = ""

@app.route("/")
def main():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def analytics():
    global count
    if count == 0:
        count += 1
        global datasetLoc
        datasetLoc = request.form['query']
        return "Thank you for providing the dataset location! Please let me know what insights you want!"
    else:
        query = request.form['query']
        return answer(datasetLoc, "from the dataset " + datasetLoc + "" + query)

if __name__ == "__main__":
    app.run()