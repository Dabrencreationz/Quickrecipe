# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user-input ingredients
        user_ingredients = request.form['ingredients']
        
        # Call Spoonacular API to fetch recipes
        api_key = '4505454e0a5c46688289a9e4ebf6e466'
        url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={user_ingredients}&number=5'
        response = requests.get(url)
        recipes = response.json()
        
        return render_template('index.html', recipes=recipes, ingredients=user_ingredients)
    
    return render_template('index.html', recipes=[], ingredients='')

if __name__ == '__main__':
    app.run(debug=True)
