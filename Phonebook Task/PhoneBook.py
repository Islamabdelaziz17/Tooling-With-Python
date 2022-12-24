import sys,os,difflib,re

myphonebooks = {}

##Creating Phonebook Dictionary
def create_phonebook():
  phonebookname = input("Phonebook Name: ")
  mydict = {}
  return mydict,phonebookname
  
##Select which phonebook to have access upon
def SelectPhoneBook():
  for phonebook in myphonebooks:
        print(str(int(list(myphonebooks).index(phonebook))+1) +"-" + phonebook)
  phonebookno = input("Choose Your Phonebook: ")
  return phonebookno
 
##Add new contact to the selected phonebook
def AddContact(myphonebook):
  flag = True
  ##Input Name and verify it
  while flag:
    Name = input("Enter Contact Name: ")
    if not Name.isdigit():
      flag = False
  flag = True
  ##Input Number and verify it
  while flag:
    Num  = input("Enter Contact Number: ")
    if Num.isdigit() and len(Num) == 11:
      flag = False
  flag = True
  ##Input Mail and verify it using REGEX
  while flag:
    Mail = input("Enter Contact Mail: ")
    #Verify using regex expression the correct inputed format of the mail
    if not re.match(r'[\w.-]+@[\w.-]+[.]com',Mail):
      flag = True
      print("Wrong Email Format[You can use letters, numbers . & -]")
    else:
      flag = False
  flag = True
  ##Input Gender and verify it
  while flag:
    Gender = input("Enter Contact Gender: ")
    Gender = Gender.lower()
    if Gender == 'm' or Gender == 'f':
      flag = False
    else:
      print("Please choose between 'm' OR 'f' only")
      
  ##Finally, Add record to the phonebook
  myphonebook.update({Name:[Num,Mail,Gender]})
    
    
##Method to Modify phonebook contacts
def ModifyContact(myphonebook):
  print("--------------------------------------------")
  
  #Print the list of Contact Names to the user
  for key in myphonebook:
    print(str(int(list(myphonebook).index(key))+1) +"-" + key)
    
  #take the chosen contact iput from the user
  key = input("Choose the contact you want to modify: ")
  
  #verify if the contact scanned available in the phonebook or not
  if list(myphonebook)[int(key)-1] not in myphonebook.keys():
    print("Invalid Contact")
  else:
    print("----------------------\nChoose what you want to modify:\n1-Number\n2-Mail\n3-Gender\n----------------------")
    flag = True
    modnum = input()
    if modnum == '1':
      ##Modify the contact number & verifies it
      while flag:
        temp = input("Enter a new number: ")
        if temp.isdigit() and len(temp) == 11:
          flag = False
          myphonebook[list(myphonebook)[int(key)-1]][0] = temp
      flag = True
    ##Modify the contact mail & verifies it
    elif modnum == '2':
      while flag:
        temp = input("Enter a new mail: ")
        if not re.match(r'[\w.-]+@[\w.-]+[.]com',temp):
          flag = True
          print("Wrong Email Format[You can use letters, numbers . & -]")
        else:
          flag = False
          myphonebook[list(myphonebook)[int(key)-1]][1] = temp
      flag = True
    ##Modify the contact gemder & verifies it
    elif modnum == '3':
      while flag:
        temp = input("Enter a new gender: ")
        temp = temp.lower()
        if temp == 'm' or temp == 'f':
          flag = False
          myphonebook[list(myphonebook)[int(key)-1]][2] = temp
        else:
          print("Please choose between 'm' OR 'f' only")
    else:
      print("Invalid Option")
      
      
##Method to display the current selected phonebook contacts
def ShowContacts(myphonebook):
  ##if phonebook is empty show nothing
  if len(myphonebook) == 0:
    print("No Contacts")
  ##else display the contacts information
  else:
    print('###---Contacts---###')
    print('--------------------')
    for key in myphonebook:
      print("Name: " + key)
      print("Number: " + myphonebook[key][0])
      print("Mail: " + myphonebook[key][1])
      print("Gender: " + myphonebook[key][2])
      print("-------------------------")
  
##Method used to search for a specific contact inside the phonebook and returns the best match contact for a given input
def SearchPhoneBook(myphonebook):
  Names = []
  BestFitNames = []
  ##loop to get only contact names from the phonebook
  for key in myphonebook:
    Names.append(str(key))
  #check if there is contacts or phonebook is empty
  if len(Names) <= 0:
    print("No Contacts")
  else:
    ##Scan the input name from the user
    contacttosearchfor = input("Enter The Contact you want to search for: ")
    print('-------------------------')
    #Search for the best fit contact that matches the user input
    BestFitNames = difflib.get_close_matches(contacttosearchfor, Names, len(Names),0.3)
    if len(BestFitNames) <= 0:
      print("Not Found")
    else:
      print("Did you mean: ")
      print("Name: " + BestFitNames[0])
      print("Number: " + myphonebook[BestFitNames[0]][0])
      print("Mail: " + myphonebook[BestFitNames[0]][1])
      print("Gender: " + myphonebook[BestFitNames[0]][2])
      print("-------------------------")
      
##method used to  Delete specific contact from the curret selected phonebook 
##using the SearchPhoneBook() method to get the desired contact then deletes it
def DeleteContact(myphonebook):
  Names = []
  BestFitNames = []
  flag = True
  for key in myphonebook:
    Names.append(str(key))
  if len(Names) <= 0:
    print("No Contacts")
  else:
    contacttosearchfor = input("Enter The Contact you want to Delete: ")
    print('-------------------------')
    BestFitNames = difflib.get_close_matches(contacttosearchfor, Names, len(Names))
    if len(BestFitNames) <= 0:
      print("Not Found")
    else:
      print("Did you mean: ")
      for name in BestFitNames:
        print("Name: " + name)
        print("Number: " + myphonebook[name][0])
        print("Mail: " + myphonebook[name][1])
        print("Gender: " + myphonebook[name][2])
        print("-------------------------")
        while flag:
          YourFinalChoice = input("Write Down The Contact You really want to delete: ")
          if YourFinalChoice in myphonebook:
          ##Delete the desired contact
            del myphonebook[YourFinalChoice]
            flag = False
            print("** Contact Deleted Successfully **")
          else:
            print("NotFound")
        
##Method used to show the mainmenu of the Phonebook application
def ShowMenu():
  os.system('cls')
  print("Choose Your Option: ")
  print("--------------------------\n1--->Create Phonebook\n2--->Select Phonebook\n3--->Add Contact\n4--->Modify Contact\n5--->Show Contact\n6--->Search Contact\n7--->Delete Contact\n8--->Delete Phonebook\n9--->Exit\n--------------------------\n" )

##Method used to check whether the user wanted to end a specific functionality or not
def CheckTermination(Terminate):
  FunctionTerminator = False
  while Terminate:
    contin = input("Do You Want To Return Back To Mainmenu ? (Y || N): ")
    contin = contin.upper()
    if contin == 'N':
      FunctionTerminator = True
      Terminate = False
    elif contin == 'Y':
      FunctionTerminator = False
      Terminate = False
      ShowMenu()
  return FunctionTerminator
  
def main():
 
  ShowMenu()      ##Display the MainMenu for the user
  Terminate = True  ## Terminator flag used to decide the status of the currently used function
  while True:
  
    choice = input()  ##Scanning the menu optio choosen by the user
    FunctionTerminator = True   ## Terminator flag used to decide the status of the currently used function
    ##Create new Phonebook
    if choice == '1':
      while FunctionTerminator:
        Terminate = True
        ##Call the  create_phonebook method which returns the dictionart & the phonebook name which will be the key of this phonebook inside another dictionary
        mydict,phonebookname = create_phonebook()
        ##add to the myphonbooks dictionary the new created dictionnary to be a dictionary of dictionaries
        myphonebooks.update({phonebookname:mydict})
        print("** Phonebook Created Successfully **")
        FunctionTerminator = CheckTermination(Terminate)
    ##Select a Phonebook
    elif choice == '2':
      while FunctionTerminator:
        Terminate = True
        try:
          ##Call SearchPhoneBook() method return's the index of the chosen phonebook
          phonebookno = SelectPhoneBook()
          ##Assign the current phonebook with the chosen one
          mydict = myphonebooks[list(myphonebooks)[int(phonebookno)-1]]
          print("** Phonebook "+ list(myphonebooks)[int(phonebookno)-1] + "Selected Successfully **")
        except:
          print("There Are No Phonebooks Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Add New Contact to the currently selected Phonebook
    elif choice == '3':
     while FunctionTerminator:
        Terminate = True
        try:
          #Call Addcontact() method to scan the user input ad save the contact information
          AddContact(mydict)
          print("** Contact Added Successfully **")
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Modify a specific contact 
    elif choice == '4':
      while FunctionTerminator:
        Terminate = True
        try:
          ##Call ModifyContact() method to scan the user input & then saves the data to the phonebook
          ModifyContact(mydict)
          print("** Contact Modified Successfully **")
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Display the phonebook contacts
    elif choice == '5':
      while FunctionTerminator:
        Terminate = True
        try:
          ##Call ShowContacts() method to display the current currently existed contacts
          ShowContacts(mydict)
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Search the phonebook contacts best match the user input
    elif choice == '6':
      while FunctionTerminator:
        Terminate = True
        try:
          SearchPhoneBook(mydict)
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Delete a selected phonebook contact by the user
    elif choice == '7':
      while FunctionTerminator:
        Terminate = True
        try:
          DeleteContact(mydict)
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Delete a selected phonebook by the user
    elif choice == '8':
      while FunctionTerminator:
        Terminate = True
        try:
          phonebookno = SelectPhoneBook()
          mydict = myphonebooks[list(myphonebooks)[int(phonebookno)-1]]
          choiceofdeletion = input("** Phonebook: "+ list(myphonebooks)[int(phonebookno)-1] + " Will Be Deleted Are You Sure ? ** (Y || N)")
          if choiceofdeletion == 'Y':
            del mydict
            print("** Deleted Successfully **")
        except:
          print("There Are No Phonebooks Selected/Created Yet")
        FunctionTerminator = CheckTermination(Terminate)
    ##Exit the application
    elif choice == '9':
      break
     
      
  
if __name__ == '__main__':
  main()  
