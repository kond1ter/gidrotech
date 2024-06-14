from flask import Flask, render_template

app = Flask("DBWebApp")

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

