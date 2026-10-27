from datetime import date as Date, time
from sqlite3 import Time


class Attendee:
    counter:int=0
    valid:bool=False

    symbols:list[str]=["!",",","£","$","%","^","&","*","(",")","_","-","+","=","]","[","{","}",":",";","/","?","<",">","|","¬","``"]
    def __init__(self,name: str, email:str | None=None):
        """
        This function will take in the name and email and store the values,
        it will be given a unique id and there is a valid email check
        and if it is invalid it will be set as None.

        Args:
           name (str): Attendee's name.
            email (str | None): Attendee's email.
        """
        Attendee.counter+=1

        self.__attendee_id=Attendee.counter
        self.name=name

        if email is not None:
            check_1:int=email.count("@")
            check_2:int=email.count(".")
            if len(email)>=8 and len(email)<=50 and check_1==1 and check_2>=1 and email.islower():
                portion:list[str]=email.split(".")
                last:int=len(portion)
                if portion[last-1].isalpha():
                    Attendee.valid=True
                for x in email:
                    if x in Attendee.symbols:
                        print("Invalid email")
                        Attendee.valid=False
        
        if Attendee.valid:
            self.email=email
        else:
            self.email=None
    
    def update_email(self,new_email:str)->bool:
        """
        This function will take in the new email and check if the email
        has the correct length, no symbols that are in the list, the email
        should contain at least a . and only one @, the email is in lowercase,
        and there should be text after the final . of the email. 

        Args:
            new_email (str) - New email to be added.

        Returns:
            True - If it passes the checks
            False - If it fails the checks
        """
        for part in new_email:
            if part in Attendee.symbols:
                return False
        look_1:int=new_email.count("@")
        look_2:int=new_email.count(".")
        if len(new_email)>=8 and len(new_email)<=50 and look_1==1 and look_2>=1 and new_email.islower():
            #Splits the email to check if there is text after the final .
            section:list[str]=new_email.split(".")
            #Splitting to check domain
            after: list[str]=new_email.split("@")
            #Counts the number of items in the list
            end: int=len(section)
            #IT checks if there is text after the . and if there is a domain
            if section[end-1].isalpha() and len(after[1])>0:
                self.email=new_email
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self) -> str:
        """
        This function will return a string that contains information
        of the Attendee.

        Args:
            self.name = Name of the Attendee.
            self.email= Email of the Attendee.

        Returns:
            A string that contains the Attendee's name and Attendee's email.
        """
        return f"Name: {self.name}, Email {self.email}"





        
class Booking:
    book_count: int= 0
    def __init__(self,attendee: Attendee, event: str, book_date:Date, cancelled: bool):
        """
                This function will take in the attendee, event,
                booking date and cancelled.It will do checks on the booking date to check if the
                dates are not in the future and the event and attendee to ensure it is None.The
                values are stored in the Booking  objectvariables.The Booking id gives each object
                a unique id.

                Args:
                    attendee = Stores the Attendee Object
                    event = Stores the Event Object
                    book_date = Stores the booking date
                    cancelled = Stores a boolean.
        """
        Booking.book_count+=1
        self.__book_id=Booking.book_count
        self.cancelled=cancelled

        current: Date=Date.today()

        if current>book_date:
            self.book_date=book_date
        else:
            self.book_date=None

        if attendee is not None:
            self.attendee=attendee

        if event is not None:
            self.event=event

    def change_attendee(self,person: Attendee | None)-> bool:
        """
                This function will change the attendee on the booking
               and return a bool.

               Args:
                   person = Stores the attendee object.
               Returns:
                   True or false and if the object is not none, the value
                   stored in the attendee variable will store the person
                   variable.
        """
        if person is not None:
            self.attendee=person
            return True
        return False

    def cancel_booking(self)->bool:
        """
                 This function will cancel the booking by changing the cancelled
                 field to True.

                 Returns:
                     If the cancelled field is not set to True, it will set it to True
                     and return True.If it is set to True, it returns False because there
                     is no change created.
        """
        if not self.cancelled:
            self.cancelled=True
        return False

    def __str__(self)-> str:
        """
                     This function will return a string that contain the Booking Information,
                     the if statement will check if the event is cancelled and store yes or no
                     in the answer variable.

                     Returns:
                         It returns a string containing the Booking Information.
        """
        if self.cancelled:
            answer: str="Yes"
        else:
            answer="No"

        return ("Details below:\n"
                f"{self.attendee}:\n"
                f"Date: {self.book_date}\n"
                f"Event: {self.event}\n"
                f"Cancelled: {answer}\n"
                " ")

class Event:
    def __init__(self,Event_id:int,title:str,event_type:str,date:Date,start_time:Time,capacity:int,venue:Venue,cancelled:bool,ticketprice:float):
        """
        This function will take in the Event_id, title, event_type, date, start_time, capacity, venue, cancelled and ticketprice and store the values.
        It will check if the date is in the future and if the event_type is valid and if the capacity is less than or equal to the venue capacity. If any of these checks fail, the corresponding attribute will be set to None.
        
        
        Args:
            Event_id (int): Event's unique id.
            title (str): Event's title.
            event_type (str): Type of the event.
            date (Date): Event's date.
            start_time (Time): Event's start time.
            capacity (int): Maximum number of attendees.
            venue (Venue): Event's venue.
            cancelled (bool): Whether the event is cancelled.
            ticketprice (float): Price of each ticket.
        
        
        Returns:
            None
            """
        self._Event_id = Event_id
        self.title = title
        self.start_time = start_time
        self.venue = venue.name
        self.cancelled = cancelled
        self.ticketprice = ticketprice

        current = Date.today()
        if date >= current:
            self.date = date
        else:
            self.date = None

        lis_events = ["workshop","open day","conference","convention"]
        if event_type in lis_events:
            self.event_type = event_type
        else:
            self.event_type = None

        venue_capacity = venue.capacity()
        if venue.valid and venue_capacity is not None and 0 < capacity <= venue_capacity:
            self._capacity = capacity
        else:
            self._capacity = None

    def update_scheduling_detials(self,new_date:Date,new_time:Time):
        """
        This function will take in the new date and new time and check if the new date is in the future. If it is, it will update the date and start time of the event. 
        
        Args:
            new_date (Date): New date for the event.
            new_time (Time): New start time for the event.

        Returns:
            None
        """
        current = Date.today()
        if new_date >= current:
            self.date = new_date
            self.start_time = new_time

    def change_venue(self,new_venue:Venue) -> bool:
        """
        This function will take in the new venue and check if the new venue is valid and if the new venue's capacity is greater than or equal to the current event's capacity. 
        If both conditions are met, it will update the venue of the event and return True. Otherwise, it will return False.
        
        args:
            new_venue (Venue): New venue for the event.
        Returns:
            True - If the new venue is valid and has enough capacity.
            False - If the new venue is invalid or does not have enough capacity.
        """
        new_capacity = new_venue.capacity()
        if (new_venue.valid and new_capacity is not None and
                self._capacity is not None and new_capacity >= self._capacity):
            self.venue = new_venue.name
            return True
        else:
            return False
    def change_type(self,new_event_type:str) -> bool:
        """
        This function will take in the new event type and check if the new event type is valid. 
        If it is, it will update the event type of the event and return True. Otherwise, it will return False.

        args:
            new_event_type (str): New event type for the event.
        Returns:
            True - If the new event type is valid.
            False - If the new event type is not valid.
        """
        lis_events = ["workshop","open day","conference","convention"]
        if new_event_type in lis_events:
            self.event_type = new_event_type
            return True
        else:
            return False
    def cancel_event(self) -> bool:
        """
        This function will check if the event can be cancelled.
        If the event date is in the past or the event is already cancelled, it will return False.
        If the event can be cancelled, it will set the cancelled attribute to True and return True.

        Returns:
            True - If the event is successfully cancelled.
            False - If the event cannot be cancelled.
        """
        current = Date.today()
        if self.date is None or current >= self.date or self.cancelled:
            return False
        self.cancelled=True
        return True
    def __str__(self) -> str:
        """
        This function will return a string containing the Event Information and check if it is cancelled.

        returns:
            A string containing the Event Information.
        """
        if self.cancelled:
            answer="Yes"
        else:
            answer="No"
        return ("Event Information\n"
                f"Event_id: {self._Event_id}\n"
                f"Title: {self.title}\n"
                f"Date: {self.date}\n"
                f"Start Time: {self.start_time}\n"
                f"Venue: {self.venue}\n"
                f"Event Type: {self.event_type}\n"
                f"Capacity: {self._capacity}\n"
                f"Cancelled: {answer}\n"
                f"Ticket Price: {self.ticketprice}\n")

    

            






class Venue:
    def __init__(self,Venue_id:int,name:str,Capacity:int):
        """
        This function will take in the Venue_id, name and Capacity and store the values.
        
        
        Args:
            Venue_id (int): Venue's unique id.
            name (str): Venue's name.
            Capacity (int): Venue's capacity.
            valid (bool): Store's the boolean value
        
        returns:
            False - If the capacity is less than or equal to 0.
            True - If the capacity is greater than 0, it will store all the values  in the object variables.
        """
        
        self._Venue_id = Venue_id
        self.name = name
        
        

        if Capacity <= 0:
            self.valid = False
            self._Capacity = None
        else:
            self.valid = True
            self._Capacity = Capacity
            

    def venue_id(self) -> int:
        """
        This function will return the Venue_id of the Venue object.
        
        Returns:
            Venue_id (int): Venue's unique id.
        """
        return self._Venue_id

    def capacity(self) -> int:
        """
        This function will return the capacity of the Venue object.
        
        Returns:
            Capacity (int): Venue's capacity.
        """
        return self._Capacity
    def __str__(self) -> str:
        """
        This function will return a string containing the Venue Information.
        
        Returns:
            A string containing the Venue Information.
        """
        return ("Venue Information\n"
                f"VenueID: {self._Venue_id}\n"
                f"Name: {self.name}\n"
                f"Capacity: {self._Capacity}")
    
    
venue=Venue(1,"DkIT",100)
event=Event(1,"Conference","conference",Date(2027,8,26),time(10,0),100,venue,False,50.0)

event.update_scheduling_detials(Date(2027,5,27),time(11,0))
print(event)
print("*"*50)
event.change_venue(Venue(2,"DkIT",200))
print(event)
print("*"*50)
event.change_type("workshop")
print(event)


        
















person=Attendee("Gian", "d00288733@student.dkit.ie")
print(person)
person.update_email("giangallego@gmail.com")
print(person)
mydate=Date(2026, 5, 26)
check=Booking(person,"conference",mydate,False)
print(check)
check.cancel_booking()
print(check)