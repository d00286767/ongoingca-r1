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
class Booking:
    pass