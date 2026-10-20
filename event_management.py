class Attendee:
    counter:int=0
    valid:bool=False

    symbols:list[str]=["!",",","£","$","%","^","&","*","(",")","_","-","+","=","]","[","{","}",":",";","/","?","<",">","|","¬","``"]
    def __init__(self,name: str, email:str | None=None):
        """
        This function will take in the name and email and store the it,
        it will be given a unique id and there is a valid email check
        and if it is invalid it will be set as None.

        Args:
            name (str): Attendee's name.
            email (str | None): Attendee's email.
        """
        Attendee.count+=1

        self.__attendee_id=Attendee.count
        self.name=name

        if email is not None:
            check_1:[str]=email.count("@")
            check_2[str]=email.count(".")
            
            if len(email)>=8 and len(email)<=50 and check_1==1 and check_2<=3 and email.islower():
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
        for part:str in new_email:
            if part in Attendee.symbols:
                return False
        look_1[str]=new_email.count("@")
        look_2:str=new_email.count(".")
        if len(new_email)>=8 and len(new_email)<=50 and look_1==1 and look_2<=3 and new_email.islower():
            #Splits the email to check if there is text after the final .
            section:list[str]=new_email.split(".")
            #Counts the number of items in the list
            end=len(section)
            #IT checks if there is text after the .
            if section[end].isalnum():
                return True
            else:
                return False
        else:
            return False



        
class Booking:
    pass