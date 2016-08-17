from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')  # render homepage

@app.route('/about')
def about():
    return render_template('about.html')  # render homepage

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
