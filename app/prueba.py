from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def server_info():
   personas = [
       {
           "nombre": "Hector",
           "apellidos": "Mendoza Cortez"
       },
       {
           "nombre": "Tadeo",
           "apellidos": "Lopez Chavez"
       }
   ]
   return jsonify(personas)

   if __name__ == "__main__":
       app.run()
