from event_management import *

# 3 Attendees
person_1=Attendee("Gian", "d00288733@student.dkit.ie")
person_2=Attendee("Michael","michaelsmith@yahoo.ie")
person_3=Attendee("Susan","suswal@outlook.com")

# 3 Venue
venue_1=Venue(1, "Dkit", 100)
venue_2=Venue(2, "Croke Park", 50000)
venue_3=Venue(3, "Aviva Stadium", 50000)

# 5 events
event_1=Event(1,"Conference","conference",Date(2027,8,26),time(10,0),100,venue_1,False,50.0)
event_2=Event(2,"Concert","convention",Date(2027,8,26),time(20,0),50000,venue_2,True,100.0)
event_3=Event(3,"Workshop","workshop",Date(2027,9,1),time(14,0),200,venue_1,False,75.0)
event_4=Event(4,"Seminar","workshop",Date(2027,9,15),time(10,0),500,venue_3,True,150.0)
event_5=Event(5,"Hackathon","conference",Date(2027,10,1),time(9,0),1000,venue_2,False,200.0)

# 5 Bookings
booking_1=Booking(person_1,event_1,Date(2026,5,4),False)
booking_2=Booking(person_2,event_2,Date(2026,7,25),True)
booking_3=Booking(person_3,event_3,Date(2026,8,16),False)
booking_4=Booking(person_1,event_4,Date(2026,3,12),True)
booking_5=Booking(person_2,event_5,Date(2026,2,21),False)

#Display Venues

print("Venues:")
for place in [venue_1,venue_2,venue_3]:
    print(f"{place.name}")
print(" ")

#Display bookings
print("Current Bookings")
print("-"*50)
for part in [booking_1,booking_2,booking_3,booking_4,booking_5]:
    print(f"Name:{part.attendee.name}")
    print(f"Title: {part.event.title}")
    print(f"Event_Type: {part.event.event_type}")
    print(" ")

print("Changing the emails")
#Changing the email without an @.
check_email = person_1.update_email("d00288733student.dkit.ie")
if not check_email:
    print("Invalid Email, there is no @")
print(person_1)

print("-"*50)
#Checking domain name
check_email_2 = person_2.update_email("d00288733@")
if not check_email_2:
    print("Invalid Email, no domain name")
print(person_2)
print("*"*50)


#displaying the events
for event in [event_1, event_2, event_3, event_4, event_5]:
    print(event)
    print("*"*50)

#cancel a event
event_3.cancel_event()

#Cancel a booking
print("Before changing booking")
print(booking_3)
booking_3.cancel_booking()
print("After changing booking")
print(booking_3)
print(" ")
print("-"*50)

#display all the active events
print("*"*50)
print("Active Events:")
for event in [event_1, event_2, event_3, event_4, event_5]:
    if event.cancelled == False:
        print(event)
        print("*"*50)

#Display cancelled Bookings
for result in [booking_1,booking_2,booking_3,booking_4,booking_5]:
    if result.cancelled==True:
        print(result)
print("-"*50)

#Display bookings of specific attendee
for specific in [booking_1,booking_2,booking_3,booking_4,booking_5]:
    if specific.attendee.name==person_1.name:
        print(specific)