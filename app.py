from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Aqui você pode passar dados como a "Nossa História" para o HTML
    historia = "Nossa jornada começou na escola..."
    return render_template('index.html', historia=historia)

if __name__ == '__main__':
    app.run(debug=True)
