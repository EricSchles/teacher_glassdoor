from flask import Flask,render_template,request
import pickle

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        complaints = pickle.load(open("complaints","rb"))
        complaint = request.form.get("complaint")
        complaints.append(complaint)
        pickle.dump(complaints,open("complaints","wb"))
        return render_template("index.html",complaints=complaints)
    else:
        complaints = pickle.load(open("complaints","rb"))
        if complaints == []:
            return render_template("index.html")
        else:
            return render_template("index.html",complaints=complaints)

app.run(debug=True)
