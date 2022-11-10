import numpy as np
import pickle

file_path = r'Loan_eligibility/artifacts/loan_eligibility_prediction.pkl'

class LoanPrediction():
    def __init__(self, Dependents, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area):
        self.Dependents = Dependents
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area
    

    def get_model(self):
        with open( file_path,'rb') as f:
            self.model = pickle.load(f)

    def get_predicted_score(self):
        self.get_model()
        input_array = np.array([self.Dependents,self.Education,self.Self_Employed,
                                self.ApplicantIncome,self.CoapplicantIncome, self.LoanAmount, 
                                self.Loan_Amount_Term, self.Credit_History,self.Property_Area],ndmin = 2)
        print(input_array)
        predicted_class = self.model.predict(input_array)[0]
        
        classes = { 0 : "N", 
                    1 : "Y" }

        result = classes[predicted_class]
        return result

if __name__ == "__main__":
    Obj = LoanPrediction(1,0,4583,1508,128,360,1,0,0)
    result = Obj.get_predicted_score()
    print("Predicted CLass is :",result)
