from event_management import *

# 3 Attendees
person_1=Attendee("Gian", "d00288733@student.dkit.ie")
person_2=Attendee("Michael","michaelsmith@yahoo.ie")
person_3=Attendee("Susan","suswal@outlook.com")

# 3 Venue
venue_1=Venue(1, "Dundalk", 100)
venue_2=Venue(2, "Croke Park", 50000)
venue_3=Venue(3, "Aviva Stadium", 50000)

# 5 events
event_1=Event(1,"Conference","conference",Date(2027,8,26),time(10,0),100,venue_1,False,50.0)
event_2=Event(2,"Concert","concert",Date(2027,8,26),time(20,0),50000,venue_2,True,100.0)
event_3=Event(3,"Workshop","workshop",Date(2027,9,1),time(14,0),200,venue_1,False,75.0)
event_4=Event(4,"Seminar","seminar",Date(2027,9,15),time(10,0),500,venue_3,True,150.0)
event_5=Event(5,"Hackathon","hackathon",Date(2027,10,1),time(9,0),1000,venue_2,False,200.0)

#Changing the email without an @.
check_email = person_1.update_email("d00288733student.dkit.ie")
if not check_email:
    print("Invalid Email")
print(person_1)

#Checking domain name
check_email_2 = person_2.update_email("d00288733@")
if not check_email_2:
    print("Invalid Email")
print(person_2)

# #displaying the events
# print(event_1)
# print("*"*50)
# print(event_2)
# print("*"*50)
# print(event_3)
# print("*"*50)
# print(event_4)
# print("*"*50)
# print(event_5)

dic = {}

#events
dic[event_1.get_event_id()] = event_1
dic[event_2.get_event_id()] = event_2   
dic[event_3.get_event_id()] = event_3
dic[event_4.get_event_id()] = event_4
dic[event_5.get_event_id()] = event_5

print(dic)