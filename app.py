from flask import Flask
from housing.logger import logging


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("We are testing logging module")
    return "Hello this is Yuvraj Kishor Narwade"


if __name__=="__main__":
    app.run(debug=True)