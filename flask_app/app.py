from flask import Flask, render_template, request
import assignment

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['GET','POST'])
def success():
	
	#if request.method=='POST':
        	#file_=request.form["file_name"]
		#with open('myconfig.txt','w') as f:
			#f.write(file_)
        assignment.myfunction()
	return render_template("success.html")
if __name__ == '__main__':
    app.debug=True
    app.run()
