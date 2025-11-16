import json
import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# --- CONFIGURATION ---
RECIPE_FILE = '/recipes.json'

app = Flask(__name__)
# Enable CORS for development, allowing the HTML to access the API.
CORS(app) 

# --- API ENDPOINTS ---

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Reads and returns the list of all recipes."""
    try:
        with open(RECIPE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": f"Recipe file not found at {RECIPE_FILE}"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in recipe file"}), 500

@app.route('/recipes', methods=['POST'])
def save_recipes():
    """Receives and saves the entire list of recipes."""
    try:
        updated_recipes = request.json
        if not isinstance(updated_recipes, list):
            return jsonify({"error": "Payload must be a list of recipes"}), 400
        
        # Write the data back to the file with indentation for readability
        with open(RECIPE_FILE, 'w', encoding='utf-8') as f:
            json.dump(updated_recipes, f, indent=2, ensure_ascii=False)
            
        return jsonify({"message": "Recipes updated successfully!"}), 200
    except Exception as e:
        app.logger.error(f"Error saving recipes: {e}")
        return jsonify({"error": f"Failed to save recipes: {e}"}), 500

@app.route('/editor')
def serve_editor():
    """Serves the dedicated editor HTML file."""
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'editor.html')

if __name__ == '__main__':
    # You will run the server by executing this Python script.
    print(f"Server running. Open http://127.0.0.1:5000/editor to edit recipes.")
    app.run(debug=True)
