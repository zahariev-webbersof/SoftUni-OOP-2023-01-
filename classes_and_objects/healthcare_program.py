class HealthcareProgram:
    def __init__(self, name, age, weight, height, blood_pressure):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.blood_pressure = blood_pressure

    def get_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def get_blood_pressure_status(self):
        if self.blood_pressure[0] < 120 and self.blood_pressure[1] < 80:
            return 'Low'
        elif 120 <= self.blood_pressure[0] <= 139 and 80 <= self.blood_pressure[1] <= 89:
            return 'Prehypertension'
        elif 140 <= self.blood_pressure[0] <= 159 and 90 <= self.blood_pressure[1] <= 99:
            return 'Stage 1 high blood pressure '
        elif self.blood_pressure[0] >= 160 and self.blood_pressure[1] >= 100:
            return 'Stage 2 hypertension'
        else:
            'Normal'

    def get_max_heart_rate(self):
        max_heart_rate = 220 - self.age
        return max_heart_rate

    def get_target_heart_rate(self):
        max_heart_rate = self.get_max_heart_rate()
        lower_target = max_heart_rate * 0.50
        upper_target = max_heart_rate * 0.85
        return round(lower_target, 2), round(upper_target, 2)

    def get_calories_burned(self, activity):
        if activity.lower() == 'walking':
            calories_per_minute = 4.5 * (self.weight / 2.2) / 200
        elif activity.lower() == 'swimming':
            calories_per_minute = 7 * (self.weight / 2.2) / 200
        elif activity.lower() == 'running':
            calories_per_minute = 11.5 * (self.weight / 2.2) / 200
        else:
            raise ValueError('Invalid activity')

        return round(calories_per_minute * 30 * 2)

