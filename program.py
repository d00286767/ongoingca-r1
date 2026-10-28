from event_management import *

# 3 Attendees
person_1=Attendee("Gian", "d00288733@student.dkit.ie")
person_2=Attendee("Michael","michaelsmith@yahoo.ie")
person_3=Attendee("Susan","suswal@outlook.com")

#Changing the email without an @.
check_email = person_1.update_email("d00288733student.dkit.ie")
if not check_email:
    print("Invalid Email")
print(person_1)

#Checking domain name
check_email_2 = person_2.update_email("d00288733@")
if not check_email_2:
    print("Invalid Email")
print(person_1)
