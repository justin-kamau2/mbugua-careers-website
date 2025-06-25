from flask import Flask

app = Flask(__name__)

#Registering a path/route part of url after domain name
@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
