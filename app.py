from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f7f6; }
        .container { background: white; padding: 20px; border-radius: 8px; max-width: 400px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h2 { color: #333; }
        input[type="number"], select { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; background-color: #28a745; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #218838; }
        .result { margin-top: 15px; font-weight: bold; color: #007bff; font-size: 16px; }
    </style>
</head>
<body>
<div class="container">
    <h2>Temperature Converter (V1)</h2>
    <form method="POST" action="/convert">
        <label>Enter Temperature:</label>
        <input type="number" step="any" name="temperature" required>
        <label>Conversion Type:</label>
        <select name="type">
            <option value="c_to_f">Celsius to Fahrenheit</option>
        </select>
        <button type="submit">Convert</button>
    </form>
    {% if result %}
    <div class="result">Result: {{ result }}</div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE, result=None)

@app.route("/convert", methods=["POST"])
def convert():
    try:
        temp = float(request.form.get("temperature"))
        conv_type = request.form.get("type")
        
        if conv_type == "c_to_f":
            result = f"{temp}°C = {(temp * 9/5) + 32:.2f}°F"
        else:
            result = "Unsupported conversion scheme."
            
        return render_template_string(HTML_TEMPLATE, result=result)
    except Exception:
        return render_template_string(HTML_TEMPLATE, result="Calculation error.")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
