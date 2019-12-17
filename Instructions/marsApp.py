# Import dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrapeMars
import os

# Create istance of flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/marsApp.py'
mongo = PyMongo(app)
# mongo = PyMongo(app, uri="mongodb://localhost:27017")

@app.route('/')
def home(): 
    # Find data that was stored by scrapeMars.py
    marsInfo = mongo.db.marsInfo.find_one()

    # Return template and data
    return render_template('Mission_To_Mars.html', marsInfo=marsInfo)

# Route that will trigger scrape function
@app.route('/scrape')
def scrape(): 
    # Run scrapped functions
    marsInfo = mongo.db.marsInfo
    marsData = scrapeMars.marsNews()
    marsData = scrapeMars.marsFeaturedImage()
    marsData = scrapeMars.marsWeather()
    marsData = scrapeMars.marsFacts()
    marsData = scrapeMars.marsHemis()
    marsInfo.update_one({}, {"$set": marsData}, upsert=True)

    return redirect('/', code=302)

if __name__ == '__main__': 
    app.run(debug= True)
