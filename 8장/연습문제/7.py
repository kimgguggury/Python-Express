# class PhoneBook :
    
#     def __init__(self,n = "", m = "", o="", e="") :
#         self.__contacts = {"name" : n, "mobile" : m, "office" : o, "email" : e}
    
#     def add(self, name, mobile = None, office = None, email = None) :
#         self.__contacts["name"] = name
#         self.__contacts["mobile"] = mobile
#         self.__contacts["office"] = office
#         self.__contacts["email"] = email
    
#     def setName(self, name) :
#         self.__contacts["name"] = name
        
#     def setMobile(self, mobile) :
#         self.__contacts["mobile"] = mobile
        
#     def setOffice(self, office) :
#         self.__contacts["office"] = office
        
#     def setEmail(self, email) :
#         self.__contacts["email"] = email
        
#     def getName(self) :
#         return self.__contacts["name"]
        
#     def getMobile(self, mobile) :
#         return self.__contacts["mobile"] 
        
#     def getOffice(self, office) :
#         return self.__contacts["office"] 
        
#     def getEmail(self, email) :
#         return self.__contacts["email"] 
    
#     def __str__(self) :
#         for name, mobile ,office, address in self.__contacts.items() :
#             msg = self.__contacts[name]+"\n" +"office phone: " + self.__contacts[office] + "\n" + "email address: " + self.__contacts[address] 
#         return msg
# obj = PhoneBook()
# obj.add("kim", office = "1234567", email = "kimgguggury@naver.com")
# obj.add("Park", office = "2345678", email="park@naver.com")
# print(obj)        

class 