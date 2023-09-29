import helper
from  flask import Flask,request,render_template,redirect
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
app=Flask(__name__)
@app.get("/")
def index():
    return render_template("index.html")
@app.get('/search')
def display():
    args=request.args.get('n')
    args2=request.args.get('an')
    length=helper.getlen(args,args2)
    hi='No match found!'
    if args=='' and  args2=='':
        return render_template("index.html")
    if length==0:
        return render_template("index.html",hi=hi)
    else:
        graphJSON=helper.chartshow(args,args2)
        show=helper.result(args,args2)
        resultarg=helper.result1(args,args2)
        graphJSON2=helper.chartshow2(resultarg)
        return render_template("index.html",tables=[show.to_html()],graphJSON=graphJSON,graphJSON2=graphJSON2 )
        
if __name__=='__main__':
    app.run(debug=True)
