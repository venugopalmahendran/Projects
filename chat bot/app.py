from flask import Flask, request, jsonify, render_template
from intent_classifier import model
import re


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    intent = model.predict([user_input])[0]


    if intent == "greet":
        return jsonify({"response": "Hello! Welcome to Foodie Bot"})
    elif intent == "show_menu":
        return jsonify({"response": "We have pizza, burger, fries, and coke."})
    elif intent == "order":
        info = extract_food_and_qty(user_input)
        return jsonify({"response": f"Got it!  {info['food']} {info['quantity']} added to your order."})
    elif intent == "goodbye":
        return jsonify({"response": "Thanks for ordering!"})
    else:
        return jsonify({"response": "Sorry, I didn’t get that."})
def extract_food_and_qty(text):
    foods = ["pizza", "burger", "fries", "coke"]

    match = re.search(r"\d+", text)
    quantity = int(match.group()) if match else 1 
  
    found_food = []
    for food in foods:
        if food in text.lower():
            found_food.append(food) 
            break

    if not found_food:
        found_food = "item"

    return {"food": found_food, "quantity": quantity}

   

if __name__ == "__main__":
    app.run(debug=True)
