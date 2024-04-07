from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    spisok=['список']
    main_data={
    'Город':'Чебоксары',
    'Район':'Московский',
    'Компания':'iserv'
    }
    context={'name':'Egor',
             'age':'14',
             'spes':'nothing'}
    return render_template('index.html',main_data=main_data,**context,**spisok)
@app.route('/contacts/')
def contacts():
    developer_name='Ilon Mask'
    developer_money='Владеет компанией'
    return render_template('contacts.html',name=developer_name,money=developer_money)
@app.route('/results/')
def results():
    data=[]
    return render_template('results.html',data=data)
if __name__ == "__main__":
    app.run(debug=True)