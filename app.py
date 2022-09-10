from flask import Flask
# Create app
app = Flask(__name__)

def create_app():
    import views
    app.register_blueprint(views.bp)
    
    return app