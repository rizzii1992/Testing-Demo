import numpy as np
import pickle

file_path = r'temp_pred/artifact/weather_prediction.pkl'

class WeatherPrediction():
    def __init__(self, Max_TemperatureC, Mean_TemperatureC, Min_TemperatureC,
        Dew_PointC, MeanDew_PointC, Min_DewpointC, Max_Humidity,
        Mean_Humidity,  Min_Humidity,  Max_Sea_Level_PressurehPa,
        Mean_Sea_Level_PressurehPa,  Min_Sea_Level_PressurehPa,
        Max_VisibilityKm,  Mean_VisibilityKm,  Min_VisibilitykM,
        Max_Wind_SpeedKmph,  Mean_Wind_SpeedKmph, Precipitationmm,
        CloudCover, WindDirDegrees):
        self.Max_TemperatureC = Max_TemperatureC
        self.Mean_TemperatureC = Mean_TemperatureC
        self.Min_TemperatureC = Min_TemperatureC
        self.Dew_PointC = Dew_PointC
        self.MeanDew_PointC = MeanDew_PointC
        self.Min_DewpointC = Min_DewpointC
        self.Max_Humidity = Max_Humidity
        self.Mean_Humidity = Mean_Humidity
        self.Min_Humidity = Min_Humidity
        self.Max_Sea_Level_PressurehPa = Max_Sea_Level_PressurehPa
        self.Mean_Sea_Level_PressurehPa = Mean_Sea_Level_PressurehPa
        self.Min_Sea_Level_PressurehPa = Min_Sea_Level_PressurehPa
        self.Max_VisibilityKm = Max_VisibilityKm
        self.Mean_VisibilityKm = Mean_VisibilityKm
        self.Min_VisibilitykM = Min_VisibilitykM
        self.Max_Wind_SpeedKmph = Max_Wind_SpeedKmph
        self.Mean_Wind_SpeedKmph = Mean_Wind_SpeedKmph
        self.Precipitationmm = Precipitationmm
        self.CloudCover = CloudCover
        self.WindDirDegrees = WindDirDegrees
        
    

    def get_model(self):
        with open( file_path,'rb') as f:
            self.model = pickle.load(f)

    def get_weather_prediction(self):
        self.get_model()
        input_array = np.array([self.Max_TemperatureC,self.Mean_TemperatureC,self.Min_TemperatureC,
                                self.Dew_PointC,self.MeanDew_PointC, self.Min_DewpointC, 
                                self.Max_Humidity, self.Mean_Humidity,self.Min_Humidity ,
                                self.Max_Sea_Level_PressurehPa,self.Mean_Sea_Level_PressurehPa,
                                self.Min_Sea_Level_PressurehPa,self.Max_VisibilityKm,  
                                self.Mean_VisibilityKm, self.Min_VisibilitykM,self.Max_Wind_SpeedKmph,  
                                self.Mean_Wind_SpeedKmph, self.Precipitationmm,self.CloudCover, 
                                self.WindDirDegrees],ndmin = 2)
        print(input_array)
        predicted_class = self.model.predict(input_array)[0]
        
        classes = { 0 : "Low", 
                    1 : "Medium",
                    2 : "High"}

        result = classes[predicted_class]
        return result

if __name__ == "__main__":
    Obj = WeatherPrediction(12,8,4,11,7,3,94,88,78,1033,1027,1020,18,9,5,39,21,0.010623,7,209)
    result = Obj.get_weather_prediction()
    print("Predicted CLass is :",result)
