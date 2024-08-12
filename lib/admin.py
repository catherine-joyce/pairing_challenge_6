"""
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.
"""
import datetime

def give_access(date):
    def check_format(date):
        try: 
            date_item_list = date.split("-")
            date_item_list = [len(i) for i in date_item_list]
            if date_item_list == [4,2,2]:
                return True
            else:
                raise Exception("String is not in the correct format")
        except:
            raise Exception("String is not in the correct format")
    
    if check_format(date):
        now = datetime.datetime.now()
        now = datetime.datetime.strftime(now, "%Y-%m-%d")

        now = [int(i) for i in now.split("-")]
        date = [int(i) for i in date.split("-")]
        now_year, now_month, now_day = now
        date_year, date_month, date_day = date
        age = 0
        if date_month < now_month:
            age = now_year - date_year
        elif date_month == now_month:
            if now_day >= date_day:
                age = now_year - date_year
            else:
                age = now_year - date_year - 1
        else:
            age = now_year - date_year -1
    
    if age <= 0:
        return "User can't be born after today"
    return "Access has been granted" if age >= 16 else f"Access has been denied. You are {age} years old and you need to be at least 16 years old for access."
        

