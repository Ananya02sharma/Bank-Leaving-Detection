from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

@app.route('/predict_bank_leaving', methods=['GET', 'POST'])
def predict_bank_leaving():
    geography = str(request.form['geography'])
    creditscore= int(request.form['creditscore'])
    gender = int(request.form['gender'])
    age = int(request.form['age'])
    tenure = int(request.form['tenure'])
    balance = float(request.form['balance'])
    numofproducts = int(request.form['numofproducts'])
    hascrcard = int(request.form['hascrcard'])
    isactivemember = int(request.form['isactivemember'])
    estimatedsalary = float(request.form['estimatedsalary'])

    response = jsonify({
        'estimated_price': util.get_estimated_decision(geography,creditscore,gender,age,tenure,balance,numofproducts,hascrcard,isactivemember,estimatedsalary)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Bank Prediction...")
    util.load_saved_artifacts()
    app.run()