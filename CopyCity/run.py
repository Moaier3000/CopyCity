from app import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = app.config["SESSION_SECRET_KEY"]
    app.run(debug=True)
