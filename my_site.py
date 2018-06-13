from app import app

"Only for tests, don't use in production!"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)