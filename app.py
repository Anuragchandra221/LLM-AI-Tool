from flask import Flask, render_template, request, jsonify
import os
import pathlib
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method=="GET"):
        return render_template('home.html')
    else:
        print(request.form)
        text_input = request.form['message']
        print(text_input)
        # return render_template('home.html', data=text_input)
        processed_text = "You entered: " + text_input
        # return jsonify(result = processed_text )
        
    return jsonify({'result': processed_text})


if __name__=="__main__":
    app.run(debug=True)