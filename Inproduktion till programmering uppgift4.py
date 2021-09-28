names_list=[]
numbers_list=[]
dictionary={}
class telefonbok:
    def __init__(self, firstname, number, newname):         #alla definitioner som kommer behövas
        self.firstname = firstname
        self.number = number
        self.newname = newname

    def add(self):
        print(self.firstname)
        if self.firstname not in names_list and self.number not in numbers_list:        #om namnet/numret inte är i listan så updateras den
            names_list.append(self.firstname)
            numbers_list.append(self.number)
            dictionary[self.firstname] = self.number
            print('Added ',self.firstname,' to the phonebook')
        else:
            return print("Please enter a name and number that isnt used")           #error

    def lookup(self):
        if self.firstname in names_list:            #ser om namnet är i listan om inte --> error
            print('The number for ',self.firstname, 'is ',dictionary.get(self.firstname))
        else:
            return print("sorry there is no one with that name in the phonebook")

    def alias(self):        #om namnet är i listan så tas indexen om inte --> error
        if self.firstname in names_list:
            x = names_list.index(self.firstname)
        else:
            return print('that name does not exist in the current phonebook')
        if self.newname not in names_list:          #om nya namnet inte är i listan får den samma värde som den gamla + att listan uppdateras annars --> error
            dictionary[self.newname] = dictionary.get(self.firstname)
            names_list.append(self.newname)
            print("added that alias to the phonebook")
        else:
            return print("sorry that name already exists in the current dictenary")

    def change(self):
        flipped = {}            #stores future revursed dictunary
        if self.firstname in dictionary and self.number not in numbers_list:        #makes sure firstname does not exist in dictunary
            x = dictionary.get(self.firstname)
        else:
            return print("there is no saved number with that name")
        for key, value in dictionary.items():  #flips all key/values in dictunary and stores them in flipped
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        list=[flipped.get(x)]       #makes a list of the flipped values/keys0
        for i in list[0][0:]:       #makes sure EVERY alias number changes
            dictionary[i] = self.number

    def save(self):
        f = open(self.newname, "w")
        for key, value in dictionary.items():   #tar och loppar key o valuesen och skriver dom till en fil
            f.write(value)
            f.write(";")
            f.write(key)
            f.write(";")
            f.write("\n")
        f.close()

    def load(self):
        names_list.clear()
        numbers_list.clear()
        dictionary.clear()
        print(dictionary)               #för att visa att den är clearad
        f = open(self.firstname, "r")
        x = f.read().replace("\n","").split(";")    #gör allt till en lista samt tar bort onödiga \n
        print(x)                       #11 element måste sedan ta bort ett
        for i in range(0, len(x)-1, 2):     #-1 eftersom en tom str kommer med och förstör ordinigen sedan hoppar den 2 steg för att inte blanda ihop alla nycklar med värderna
            dic = {x[i+1]: x[i]}
            names_list.append(x[i+1])       #appendar och uppdaterar alla listor o dictunaries
            numbers_list.append(x[i])
            dictionary.update(dic)
        f.close()

def interface():
    while True:
        x = input("").split()
        if x[0] == 'add':
            ya = telefonbok(x[1], x[2], '')
            ya.add()
        elif x[0]== "lookup":
            ya = telefonbok(x[1], '', '')
            ya.lookup()
        elif x[0]== "alias":
            ya = telefonbok(x[1], '', x[2])
            ya.alias()
        elif x[0]== "change":
            ya = telefonbok(x[1], x[2], '')
            ya.change()
        elif x[0]== "save":
            ya = telefonbok('', '', x[1])
            ya.save()
        elif x[0]== "load":
            ya = telefonbok(x[1], '', '')
            ya.load()
        elif x[0]=="quit":
            exit()
        elif x[0]=="yes":
            print(dictionary)   #en extra för att visa alla dom sparade värderna
            print(names_list)
            print(numbers_list)

interface()