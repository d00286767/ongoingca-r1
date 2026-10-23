from datetime import date


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
                last=len(portion)
                if portion[last-1].isalnum():
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
            #Counts the number of items in the list
            end=len(section)
            #IT checks if there is text after the .
            if section[end-1].isalnum():
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
    def __init__(self,attendee: Attendee, event: str, book_date:date, cancelled: bool):
        Booking.book_count+=1
        self.__book_id=Booking.book_count
        self.cancelled=cancelled

        current=date.today()

        if current>book_date:
            self.book_date=book_date
        else:
            self.book_date=None

        if attendee is not None:
            self.attendee=attendee

        if event is not None:
            self.event=event

    def change_attendee(self,person)-> bool:
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


person=Attendee("Gian", "d00288733@student.dkit.ie")
print(person)
person.update_email("giangallego@gmail.com")
print(person)
mydate=date(2026, 5, 26)
check=Booking(person,"conference",mydate,True)
