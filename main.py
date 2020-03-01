from app import app
app.config['SECRET_KEY'] = 'super secret key'
if __name__ =='__main__':  
    app.run(debug = True) 