from langchain_google_genai import ChatGoogleGenerativeAI
from flask import Flask,render_template,request,jsonify
import re

app = Flask(__name__)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key="AIzaSyCIVBaz92tPavPPOID2WNdS4d_TFrh9RHU",temperature=0.7)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/bat_ai",methods=["POST"])
def ai():
    userinput=request.json["message"]
    response=model.invoke(userinput)
    clean_text=re.sub(r'[^A-Za-z0-9\s]','',response.content)
    return jsonify({"response":clean_text})

if __name__ == "__main__":
    app.run(debug=True)


