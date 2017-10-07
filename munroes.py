from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def addm():
  return render_template('addmn.html')

@app.route('/listmn.html', methods=['GET','POST'])
def listmn():
  return render_template('listmn.html', t1=request.form['t1'],
  t2=request.form['t2'])


if __name__ == "__main__":
  app.run(host='0.0.0.0')
