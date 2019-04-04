from flask import Flask,render_template,request
from userlevel import old_entry
import webbrowser

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
def htmldata(dt):
    temp = []
    for x in dt:
        t = dt[x]
        tt = x.split("+")
        t["date"] = tt[0]
        t["time"] = tt[1]
        t["stamp"] = x
        temp.append(t)
    return temp

def main_front(uid):
    app = Flask(__name__)
    handle = old_entry(uid)
    print(handle)
    if(handle[0]==0):
        @app.route("/")
        def nope():
            return render_template("no_records.html")
    else:
        @app.route("/")
        def yep():
            cleandata = htmldata(handle[1])
            return render_template("details.html",data = cleandata)
    @app.route('/shutdown') #methods=['POST'])
    def shutdown():
        shutdown_server()
        
        return 'Server shutting down...'
    if __name__ == '__main__':
        print("Nitesh")
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(debug=True)
#main_front("admin")
 #is function ko call  
 #gotcha/