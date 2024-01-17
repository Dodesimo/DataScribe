from flask import Flask, render_template, request
from langchain_helper import answer
from pandasai_helper import generateGraph, getImagePath

app = Flask(__name__, static_folder='exports')
count = 0
datasetLoc = ""

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/chat")
def chat():
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

@app.route("/graphgen", methods=["GET","POST"])
def graphgen():
    if request.method == "POST":
        link = request.form.get("datasetLink")
        query = request.form.get("query")
        generateGraph(link, query)
        filePath = getImagePath()
        return render_template("graphgensuccess.html", path=filePath)
    else:
        return render_template("graphgen.html")

if __name__ == "__main__":
    app.run()