class Attendee:
    symbols:list[str]=["!",",","£","$","%","^","&","*","(",")","_","-","+","=","]","[","{","}",":",";","/","?","<",">","|","¬","``"]
    def __init__(self,attendee_id: int,name: str, email:str | None=None):
        self.__attendee_id=attendee_id
        self.name=name

        check_1:[str]=email.count("@")
        check_2[str]=email.count(".")

        if len(email)>=8 and len(email)<=50 and check_1==1 and check_2<=3 and email.islower():
            valid:bool=True
            for x in email:
                if x in Attendee.symbols:
                    valid=False
        
        if valid:
            self.email=email
        else:
            self.email=None

class Booking:
    pass