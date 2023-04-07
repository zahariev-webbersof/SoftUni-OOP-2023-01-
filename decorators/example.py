from datetime import datetime, timedelta

def validate_profile(func):
    def wrapper(name, email, dob):
        try:
            # Check that dob is in the correct format (YYYY-MM-DD)
            dob = datetime.strptime(dob, "%Y-%m-%d")

            # Check that user is at least 18 years old
            eighteen_years_ago = datetime.now() - timedelta(days=365 * 18)
            if dob > eighteen_years_ago:
                raise ValueError("You must be at least 18 years old to create profile")

        except ValueError as e:
            return str(e)

        # if dob is valid call the original function with the arguments
        return func(name, email, dob)

    return wrapper

@validate_profile
def create_profile(name, email, dob):
    # code create user profile
    return "Profile created successfully"


result = create_profile('Ivan Ivanov', 'ivanov99@yahoo.com', '2012-03-21')
print(result)