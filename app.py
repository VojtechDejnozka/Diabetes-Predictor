from flask import Flask, render_template, request
from predictor import predict_diabetes

app = Flask(__name__)

# Valid ranges for each field (used for validation and hints)
# required=True  → user MUST provide a value before prediction runs
FIELD_RULES = {
    "glucose":           {"min": 0,   "max": 300,  "label": "Plasma Glucose",              "unit": "mg/dL",  "required": True},
    "blood_pressure":    {"min": 0,   "max": 200,  "label": "Diastolic Blood Pressure",    "unit": "mm Hg",  "required": True},
    "skinfold":          {"min": 0,   "max": 100,  "label": "Triceps Skinfold Thickness",  "unit": "mm",     "required": False},
    "insulin":           {"min": 0,   "max": 850,  "label": "2-Hour Serum Insulin",        "unit": "µU/mL",  "required": False},
    "bmi":               {"min": 0,   "max": 80,   "label": "Body Mass Index (BMI)",       "unit": "kg/m²",  "required": True},
    "diabetes_pedigree": {"min": 0.0, "max": 2.5,  "label": "Diabetes Pedigree Function",  "unit": "",       "required": False},
    "age":               {"min": 21,  "max": 120,  "label": "Age",                         "unit": "years",  "required": True},
}


def parse_and_validate(form):
    """Parse form data, validate ranges and return (values_dict, errors_list)."""
    values = {}
    errors = []

    for field, rules in FIELD_RULES.items():
        raw = form.get(field, "").strip()

        if raw == "":
            if rules.get("required"):
                errors.append(f"{rules['label']} is required.")
            values[field] = None
            continue

        try:
            value = float(raw)
        except ValueError:
            errors.append(f"{rules['label']}: must be a number.")
            values[field] = None
            continue

        if value < rules["min"] or value > rules["max"]:
            errors.append(
                f"{rules['label']}: value {value} is outside the expected range "
                f"({rules['min']} – {rules['max']})."
            )
        else:
            values[field] = value

    return values, errors


def build_result(raw_prediction, values):
    """Turn the model's 'true'/'false' into a rich result dict."""
    is_diabetic = raw_prediction == "true"

    # ── risk factors present in this individual's data ──────────────────────
    risk_flags = []
    if values.get("glucose") and values["glucose"] > 140:
        risk_flags.append("Elevated plasma glucose")
    if values.get("bmi") and values["bmi"] >= 30:
        risk_flags.append("BMI in the obese range (≥ 30)")
    if values.get("age") and values["age"] >= 45:
        risk_flags.append("Age ≥ 45")
    if values.get("blood_pressure") and values["blood_pressure"] >= 90:
        risk_flags.append("High diastolic blood pressure (≥ 90 mm Hg)")
    if values.get("insulin") and values["insulin"] > 200:
        risk_flags.append("Elevated serum insulin")
    if values.get("diabetes_pedigree") and values["diabetes_pedigree"] > 0.5:
        risk_flags.append("Notable family history of diabetes")

    return {
        "is_diabetic": is_diabetic,
        "verdict":     "High Risk – Diabetes Indicated" if is_diabetic else "Low Risk – No Diabetes Indicated",
        "color":       "danger" if is_diabetic else "success",
        "icon":        "⚠️" if is_diabetic else "✅",
        "advice": (
            "The model suggests a <strong>high likelihood of diabetes</strong>. "
            "Please consult a healthcare professional for a proper clinical evaluation."
        ) if is_diabetic else (
            "The model does <strong>not indicate diabetes</strong> based on the provided values. "
            "Continue maintaining a healthy lifestyle and schedule regular check-ups."
        ),
        "risk_flags": risk_flags,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result  = None
    errors  = []
    values  = {f: "" for f in FIELD_RULES}

    if request.method == "POST":
        values, errors = parse_and_validate(request.form)

        if not errors:
            raw = predict_diabetes(
                glucose=values.get("glucose"),
                blood_pressure=values.get("blood_pressure"),
                skinfold=values.get("skinfold"),
                insulin=values.get("insulin"),
                bmi=values.get("bmi"),
                diabetes_pedigree=values.get("diabetes_pedigree"),
                age=values.get("age"),
            )
            result = build_result(raw, values)

        # Keep form filled with submitted text values for re-display
        values = {f: request.form.get(f, "") for f in FIELD_RULES}

    return render_template(
        "index.html",
        fields=FIELD_RULES,
        values=values,
        result=result,
        errors=errors,
    )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
