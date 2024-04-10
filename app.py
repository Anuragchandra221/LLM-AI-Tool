from flask import Flask, render_template, request, jsonify
import os
import pathlib
from flask import request
from sql_llm import sql_to_llm

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method=="GET"):
        return render_template('home.html')
    else:
        print(request.form)
        text_input = request.form['message']
        username = "root"
        password = "root"
        host = "localhost"
        database =  "atliq_tshirts"

        sql_res = sql_to_llm(username, password, host, database, text_input)
        # print("ti", text_input)
        # return render_template('home.html', data=text_input)
        processed_text = sql_res["result"]
        # print("pre", processed_text) 
        return jsonify(result = processed_text )
        
    # return jsonify({'result': processed_text})


if __name__=="__main__":
    app.run(debug=True)