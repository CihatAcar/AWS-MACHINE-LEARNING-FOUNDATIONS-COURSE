# First write an test function that will take care of all the edge cases for your code.
def test_email_validator():
    assert email_validator('juno@email.com') == True
    assert email_validator('juno@email@.com') == False

# Now we can write our function
def email_validator(email):
    if email.count('@') != 0 \
        and email.count('.') != 0:
        return True 
    else:
        return False