from flask import Flask, jsonify,redirect,request,render_template
import config
import numpy as np
from temp_pred.utils import WeatherPrediction
app = Flask(__name__)

################ Root API ########################################
@app.route('/')
def Home():
   return render_template('weatherindex.html')

##########################################################################
####################### Register API #####################################
##########################################################################

       
@app.route('/weather',methods = ['POST','GET'])
def prediction():
    
    # if request.method == 'POST':
    #     input_data = request.form # Dict
    #     print("*"*90)
    #     print("DATA is :",input_data)
    #     print("*"*90)
    #     Max_TemperatureC = float(input_data['Max_TemperatureC'])
    #     Mean_TemperatureC = float(input_data['Mean_TemperatureC'])
    #     Min_TemperatureC = float(input_data['Min_TemperatureC'])
    #     Dew_PointC = float(input_data['Dew_PointC'])
    #     print("HIiiii")
    #     MeanDew_PointC = float(input_data['MeanDew_PointC'])
    #     Min_DewpointC = float(input_data['Min_DewpointC'])
    #     Max_Humidity = float(input_data['Max_Humidity'])
    #     Mean_Humidity = float(input_data['Mean_Humidity'])
    #     Min_Humidity = float(input_data['Min_Humidity'])
    #     Max_Sea_Level_PressurehPa = float(input_data['Max_Sea_Level_PressurehPa'])
    #     Mean_Sea_Level_PressurehPa = float(input_data['Mean_Sea_Level_PressurehPa'])
    #     Min_Sea_Level_PressurehPa = float(input_data['Min_Sea_Level_PressurehPa'])
    #     Max_VisibilityKm = float(input_data['Max_VisibilityKm'])
    #     Mean_VisibilityKm = float(input_data['Mean_VisibilityKm'])
    #     Min_VisibilitykM = float(input_data['Min_VisibilitykM'])
    #     Max_Wind_SpeedKmph = float(input_data['Max_Wind_SpeedKmph'])
    #     Mean_Wind_SpeedKmph = float(input_data['Mean_Wind_SpeedKmph'])
    #     Precipitationmm = float(input_data['Precipitationmm'])
    #     CloudCover = float(input_data['CloudCover'])
    #     WindDirDegrees = float(input_data['WindDirDegrees'])
    #     print('Max_TemperatureC,Mean_TemperatureC,Min_TemperatureC,Dew_PointC,MeanDew_PointC,Min_DewpointC,Max_Humidity,Mean_Humidity,Min_Humidity,Max_Sea_Level_PressurehPa,Mean_Sea_Level_PressurehPa,Min_Sea_Level_PressurehPa,Max_VisibilityKm,Mean_VisibilityKm,Min_VisibilitykM,Max_Wind_SpeedKmph,Mean_Wind_SpeedKmph,Precipitationmm,CloudCover,WindDirDegrees',Max_TemperatureC,Mean_TemperatureC,Min_TemperatureC,Dew_PointC,MeanDew_PointC,Min_DewpointC,Max_Humidity,Mean_Humidity,Min_Humidity,Max_Sea_Level_PressurehPa,Mean_Sea_Level_PressurehPa,Min_Sea_Level_PressurehPa,Max_VisibilityKm,Mean_VisibilityKm,Min_VisibilitykM,Max_Wind_SpeedKmph,Mean_Wind_SpeedKmph,Precipitationmm,CloudCover,WindDirDegrees)

    #     # prediction = functions.get_weather_prediction(Max_TemperatureC,Mean_TemperatureC,Min_TemperatureC,Dew_PointC,MeanDew_PointC,Min_DewpointC,Max_Humidity,Mean_Humidity,Min_Humidity,Max_Sea_Level_PressurehPa,Mean_Sea_Level_PressurehPa,Min_Sea_Level_PressurehPa,Max_VisibilityKm,Mean_VisibilityKm,Min_VisibilitykM,Max_Wind_SpeedKmph,Mean_Wind_SpeedKmph,Precipitationmm,CloudCover,WindDirDegrees)
    #     prediction = WeatherPrediction(Max_TemperatureC, Mean_TemperatureC, Min_TemperatureC,Dew_PointC,
    #                         MeanDew_PointC, Min_DewpointC, Max_Humidity,Mean_Humidity,  Min_Humidity,  
    #                         Max_Sea_Level_PressurehPa,Mean_Sea_Level_PressurehPa,  
    #                         Min_Sea_Level_PressurehPa,Max_VisibilityKm,  Mean_VisibilityKm,  
    #                         Min_VisibilitykM,Max_Wind_SpeedKmph,  Mean_Wind_SpeedKmph, Precipitationmm,
    #                         CloudCover, WindDirDegrees)
    #     result = Obj.get_weather_prediction()
    #     print("Predicted CLass is :",result)
    #     # print("::::::::::::::::::::::::::::::::::::",prediction)

    #     return render_template('index.html', prediction_text = f"The Predicted weather status is {prediction}")
    # #     # return jsonify({'price': f"The Predicted house price is Rs. {prediction} lakhs"})

    # return render_template("index.html")
    
    
    
    
    # Max_TemperatureC = 6
    # Mean_TemperatureC = 4
    # Min_TemperatureC = 2
    # Dew_PointC = 6
    # MeanDew_PointC = 3
    # Min_DewpointC = 1
    # Max_Humidity = 100
    # Mean_Humidity = 91
    # Min_Humidity = 70
    # Max_Sea_Level_PressurehPa = 1033
    # Mean_Sea_Level_PressurehPa = 1027
    # Min_Sea_Level_PressurehPa = 1014
    # Max_VisibilityKm = 31
    # Mean_VisibilityKm = 10
    # Min_VisibilitykM = 2
    # Max_Wind_SpeedKmph = 19
    # Mean_Wind_SpeedKmph = 10
    # Precipitationmm = 0.148094
    # CloudCover = 5
    # WindDirDegrees = 19
    


    input_data = request.form
    Max_TemperatureC = float(input_data['Max_TemperatureC'])
    Mean_TemperatureC = float(input_data['Mean_TemperatureC'])
    Min_TemperatureC = float(input_data['Min_TemperatureC'])
    Dew_PointC = float(input_data['Dew_PointC'])
    MeanDew_PointC = float(input_data['MeanDew_PointC'])
    Min_DewpointC = float(input_data['Min_DewpointC'])
    Max_Humidity = float(input_data['Max_Humidity'])
    Mean_Humidity = float(input_data['Mean_Humidity'])
    Min_Humidity = float(input_data['Min_Humidity'])
    Max_Sea_Level_PressurehPa = float(input_data['Max_Sea_Level_PressurehPa'])
    Mean_Sea_Level_PressurehPa = float(input_data['Mean_Sea_Level_PressurehPa'])
    Min_Sea_Level_PressurehPa = float(input_data['Min_Sea_Level_PressurehPa'])
    Max_VisibilityKm = float(input_data['Max_VisibilityKm'])
    Mean_VisibilityKm = float(input_data['Mean_VisibilityKm'])
    Min_VisibilitykM = float(input_data['Min_VisibilitykM'])
    Max_Wind_SpeedKmph = float(input_data['Max_Wind_SpeedKmph'])
    Mean_Wind_SpeedKmph = float(input_data['Mean_Wind_SpeedKmph'])
    Precipitationmm = float(input_data['Precipitationmm'])
    CloudCover = float(input_data['CloudCover'])
    WindDirDegrees = float(input_data['WindDirDegrees'])
    
    # # sepal_length = 3
    # # sepal_width = 5
    # # petal_length = 4
    # # petal_width = 1

    Obj = WeatherPrediction(Max_TemperatureC, Mean_TemperatureC, Min_TemperatureC,Dew_PointC,
                            MeanDew_PointC, Min_DewpointC, Max_Humidity,Mean_Humidity,  Min_Humidity,  
                            Max_Sea_Level_PressurehPa,Mean_Sea_Level_PressurehPa,  
                            Min_Sea_Level_PressurehPa,Max_VisibilityKm,  Mean_VisibilityKm,  
                            Min_VisibilitykM,Max_Wind_SpeedKmph,  Mean_Wind_SpeedKmph, Precipitationmm,
                            CloudCover, WindDirDegrees)
    result = Obj.get_weather_prediction()
    print("Predicted CLass is :",result)

    # return jsonify({"Result":f"Predicted Class is : {result}"})
    return render_template('index.html', data=result)


# if __name__ == '__main__':
#     app.run()

if __name__ == "__main__":
    print("Weather Prediction ")
    app.run(host='0.0.0.0', port=config.Port_number,debug=False)