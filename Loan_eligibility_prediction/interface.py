from flask import Flask, jsonify,redirect,request
import config
from Loan_eligibility.utils import LoanPrediction
app = Flask(__name__)

@app.route('/home')
def Home():
    return 'Welcome Guys'

       
@app.route('/prediction',methods = ['POST','GET'])
def prediction():

    input_data = request.form
    Dependents = float(input_data['Dependents'])
    Education = float(input_data['Education'])
    Self_Employed = float(input_data['Self_Employed'])
    ApplicantIncome = float(input_data['ApplicantIncome'])
    CoapplicantIncome = float(input_data['CoapplicantIncome'])
    LoanAmount = float(input_data['LoanAmount'])
    Loan_Amount_Term = float(input_data['Loan_Amount_Term'])
    Credit_History = float(input_data['Credit_History'])
    Property_Area = float(input_data['Property_Area'])
    
    # sepal_length = 3
    # sepal_width = 5
    # petal_length = 4
    # petal_width = 1

    Obj = LoanPrediction(Dependents, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area)
    result = Obj.get_predicted_score()
    print("Predicted CLass is :",result)

    return jsonify({"Result":f"Predicted Class is : {result}"})


if __name__ == '__main__':
    app.run()