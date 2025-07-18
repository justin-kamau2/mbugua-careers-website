from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 100,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 150,000'
  },
  {
    'id':3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 120,000'
  },
  {
    'id':4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

#Registering a path/route part of url after domain name
@app.route("/")
def hello_world():
  return render_template("home.html",
                        jobs=JOBS,
                        company_name="PataTech")

@app.route("/apps/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5002, debug=True)
