age_list = [47, 12, 28, 52, 35]  # do not name it to ages to avoid confusion age and ages
for i, age in enumerate(age_list):
    if age < 18:
        is_minor = True  # "is" or "has" indicates that this is a condition
        age_list[i] = "minor"
    # some other code
