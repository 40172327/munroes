from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/add-munroe.html/")
def addm():
  return render_template('add-munroe.html')

@app.route("/munroe-list.html/")
def mlist():
  return render_template('munroe-list.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
