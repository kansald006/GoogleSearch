class Cab:
     def bookCab(self, source, destination):
         print("Cab Booked from",source,"to",destination)

class OlaCab(Cab):
     def bookMeCab(self, source, destination,type):
         print("Ola Cab Booked from",type,source, "to",destination)

class UberCab(Cab):
     def bookCab(self, source, destination,type):
         print("Cab Booked from",type,source, "to",destination)

cref= Cab()
cref=OlaCab()
cref.bookCab("Pavilion","Model Town")
cref.bookMeCab("2Wheeler","Pavilion","Model Town")