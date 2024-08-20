from flask import Flask, render_template

app=Flask(__name__)
app.secret_key='7pixels'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stacks_n_services/<stack>')
def stack_n_services(stack):

    print("calling the service page with the parameter passed: "+stack)
    # return (stack+"is called")
    return render_template("service-details.html",stack=stack)

@app.route('/homepage')
def homepage():
    return render_template('index.html')









if __name__=='__main__':
    app.run(host='0.0.0.0',port=1052,debug=True)

