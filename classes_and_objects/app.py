from flask import Flask, request
from healthcare_program import HealthcareProgram
app = Flask(__name__)
@app.route('/')
def home():
    return '''	
        <h1>Healthcare Program</h1>	
        <form action="/result" method="post">	
            <p>Name: <input type="text" name="name" /></p>	
            <p>Age: <input type="number" name="age" /></p>	
            <p>Weight (kg): <input type="number" name="weight" /></p>	
            <p>Height (m): <input type="number" name="height" step="0.01" /></p>	
            <p>Blood Pressure (mmHg): <input type="text" name="blood_pressure" /></p>	
            <p>Activity: 	
                <select name="activity">	
                    <option value="walking">Walking</option>	
                    <option value="swimming">Swimming</option>	
                    <option value="cycling">Cycling</option>	
                </select>	
            </p>	
            <p><input type="submit" value="Submit" /></p>	
        </form>	
    '''
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    blood_pressure = [int(bp) for bp in request.form['blood_pressure'].split('/')]
    activity = request.form['activity']
    hp = HealthcareProgram(name, age, weight, height, blood_pressure)
    bmi = hp.get_bmi()
    bp_status = hp.get_blood_pressure_status()
    max_hr = hp.get_max_heart_rate()
    target_hr = hp.get_target_heart_rate()
    calories_burned = hp.get_calories_burned(activity)
    return f'''	
        <h1>Healthcare Program - Results</h1>	
        <p>Name: {name}</p>	
        <p>Age: {age}</p>	
        <p>Weight (kg): {weight}</p>	
        <p>Height (m): {height}</p>	
        <p>BMI: {bmi}</p>	
        <p>Blood Pressure: {blood_pressure[0]}/{blood_pressure[1]} ({bp_status})</p>	
        <p>Max Heart Rate: {max_hr}</p>	
        <p>Target Heart Rate: {target_hr[0]} - {target_hr[1]}</p>	
        <p>Calories Burned ({activity}): {calories_burned}</p>	
    '''
if __name__ == '__main__':
    app.run()