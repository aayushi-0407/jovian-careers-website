
from flask import Flask


app= Flask(__name__) ##creating app

@app.route("/")
def hello_world():
  return "Hello Welcome to out website"

if __name__== "__main__":
  app.run(host='0.0.0.0',debug=True)
