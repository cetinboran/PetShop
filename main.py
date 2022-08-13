from jsons.data import JSON
from classes.animals import Dog,Cat
from classes.person import Worker,Customer
import Entrys.passwordManagement as passwordManagement

# JSON file'larını configure edeceğimiz obje
json = JSON()

# JSON'dan aldığımız bilgileri objelere dönüştürüp initliyoruz
ALL_ANIMALS = json.init_animals()
animalsList, dogList, catList = ALL_ANIMALS[0], ALL_ANIMALS[1], ALL_ANIMALS[2] 

# json'u etkileyecek değişiklikler yaptığımızda yazdırıyoruz.
# bu fonksiyon animalsList array'ini alıp json' fileına yazdırıyor.
#json.UpdateAnimalsJson(animalsList)

# Customer/Worker bilglerini json'dan çekip objelerini oluşturuyoruz ki json'u update'lediğimizde bozulmasın
ALL_PERSONS = json.init_persons()
adminList , WorkerList, customerList, personsList = ALL_PERSONS[0], ALL_PERSONS[1], ALL_PERSONS[2], ALL_PERSONS[3]

# Update personList 

#json.UpdatePersonsJson(personsList)

# personsList[1].animals[0] = 2 ile aldıkları animal'ları arttırıyoruz.


# Abstract class'ı ile her type için farklı loop çağırıyorum.
LoginPerson = passwordManagement.Login(personsList)
if LoginPerson[0] != False:
    LoginPerson[0].Loop(LoginPerson[0], personsList, dogList, catList, animalsList, LoginPerson[1])

