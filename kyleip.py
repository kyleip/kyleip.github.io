from flask import Flask,render_template,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    author = "Kyle"
    name = "You"
    return render_template('layout.html', author=author, name=name)

# @app.route('/about/')
# def about():
#     return render_template('about.html')

@app.route('/Kyle_Ip_Resume_1208.pdf')
def resume():
    return app.send_static_file('Kyle_Ip_CResume_1208.pdf')

@app.route('/linkedin')
def linkedin():
    return redirect("https://linkedin.com/in/kyle-ip-362767122/")

@app.route('/github')
def github():
    return redirect("https://github.com/kyleip")

if __name__ == '__main__':
    app.run()
