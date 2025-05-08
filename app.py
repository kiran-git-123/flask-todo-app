from flask import Flask,render_template,request,redirect,url_for

#app instance from the Flask class

app =   Flask(__name__,template_folder='templates')

tasks = []

@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)


@app.route('/add',methods=['POST','GET'])
def create_new_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('home'))


@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))    


if __name__ == '__main__':
    app.run(debug=True)