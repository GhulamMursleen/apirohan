import flask
from werkzeug.utils import secure_filename
from flask import  abort,request,send_file,jsonify, make_response
from Untitled import Model
model=Model()

from flask_cors import CORS, cross_origin
app = flask.Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/recommend', methods = ['GET', 'POST'])
def append_file():
    
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      print("coming",request.form["id"])
      if request.form["id"]!="":
          id=str(request.form["id"])
          print(id,type(id))
          response=model.recommendation(id)
          return _corsify_actual_response(jsonify(response))
      else:
          return "error"
   else:
      return "error"
@app.route('/newsfeed', methods = ['GET', 'POST'])
def replace_file():
    
   #print("coming",request)
   if request.method == "OPTIONS": # CORS preflight
        print("optionho")
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      data = request.form["typ"]
      print("coming",data)
      #typ="News"
      response=model.newsfeed(data)
      return _corsify_actual_response(jsonify(response))
   else:
      return "error"


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    #response.headers.add('Access-Control-Allow-Headers', "*")
    #response.headers.add('Access-Control-Allow-Methods', "*")
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 8000, threaded=True,debug=True, use_reloader=True)