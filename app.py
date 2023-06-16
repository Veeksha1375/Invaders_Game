from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""@app.route('/start_game')
def start_game():
    # Import and execute the game logic from aircanva.py
    import main

    # Run the main function of the game logic
    main.main()

    # Return a response or redirect to another page after the game is finished
    return "Game Over"
"""

if __name__ == '__main__':
    app.run(debug=True)
