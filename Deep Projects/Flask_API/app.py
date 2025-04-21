from flask import Flask
from controllers import venue_controller

app = Flask(__name__)

# Register controllers
app.register_blueprint(venue_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)
