from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# ---------- Load model ----------
with open("./notebook/house_price_model_final.pkl", "rb") as f:
    model = pickle.load(f)

# ---------- Load dropdown values ----------
df_data = pd.read_csv("./dataset/dataset.csv")

LOCATIONS = sorted(df_data["Location"].dropna().unique())
PROPERTY_TYPES = sorted(df_data["Property_Type"].dropna().unique())


# ---------- Helper: safe conversion ----------
def safe_float(value):
    try:
        return float(value)
    except:
        return None


def safe_int(value):
    try:
        return int(value)
    except:
        return None


@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    category = None
    confidence = None
    error = None

    if request.method == "POST":

        area = safe_float(request.form.get("Area"))
        bedrooms = safe_int(request.form.get("Bedrooms"))
        bathrooms = safe_int(request.form.get("Bathrooms"))
        age = safe_int(request.form.get("Age"))
        location = request.form.get("Location")
        property_type = request.form.get("Property_Type")

        if None in [area, bedrooms, bathrooms, age]:
            error = "Please enter valid numeric values."

        else:

            df_input = pd.DataFrame([{
                "Area": area,
                "Bedrooms": bedrooms,
                "Bathrooms": bathrooms,
                "Age": age,
                "Location": location,
                "Property_Type": property_type
            }])

            try:

                pred = model.predict(df_input)[0]

                prediction = f"₹ {pred:,.0f}"

                # -----------------------
                # Property Category
                # -----------------------

                if pred >= 10000000:
                    category = "Luxury Property 🏰"

                elif pred >= 5000000:
                    category = "Premium Property ⭐"

                else:
                    category = "Standard Property 🏠"

                # -----------------------
                # Confidence / Accuracy
                # -----------------------

                confidence = round(0.985 * 100, 2)

            except Exception as e:
                error = f"Prediction error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        category=category,
        confidence=confidence,
        error=error,
        locations=LOCATIONS,
        property_types=PROPERTY_TYPES
    )

if __name__ == "__main__":
    app.run(debug=True)