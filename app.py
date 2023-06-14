from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Brno',
  'salary': 'Kc. 100000'
}, {
  'id': 2,
  'title': 'Data analyst',
  'location': 'Opava',
}, {
  'id': 3,
  'title': 'Data analyst',
  'location': 'Praha',
  'salary': 'Kc. 100000'
}]


@app.route("/")
def Hello_world():
  return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
