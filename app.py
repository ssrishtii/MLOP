from flask import *
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('adder.html')

def sum(n1,n2):
    return str(n1+n2)


@app.route('/sum', methods=['POST'])
def addition():
    n1=int(request.form['first_number'])
    n2=int(request.form['second_number'])
    return sum(n1,n2)
if __name__=='__main__':
        app.run()

