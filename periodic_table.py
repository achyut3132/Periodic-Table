def print_menu(): # Printing Menu Function 
	print_menu = """
							Database for Periodic Table of the Elements
1) Search by symbol/name
2) Search by atomic mass
3) Molecular Mass Calculation
4) Quit
	"""
	print (print_menu)

def print_footer ():
	footer = """
====================================================================================================
	"""
	print (footer)
	return 

def print_header():
	header = """ 
#  ElementName   Sym   Mass 
====================================================================================================
	"""
	print (header)
	return
def exit ():
	print ("\nThank you for using the program!") 
	return 

def printonly_search_by_symbol(table, ask_string): #the function differs from search_by_symbol in just that it does not ask user for string. This function is just used by molecular_formula fiunction. - try to do something else.
	result = res (table) # this list store symbol 
	element = [] # this list stores element name
	print_header () 


	for symbol in result:  
		element.append(table[symbol]) #element has now stored all the name, atomic weight and number

	for symbol in result: #reads each line from result i.e reads each key >> element symbol
		if ask_string in symbol: #prints if symbol contains the string 
			print (table[symbol][1], "  ", table[symbol][0], "  ", symbol, "  ", table[symbol][2])

	for element_name in element: #reads each line from element  i.e reads each description >> name, number, weight
		index_element = element.index(element_name) #finds the index so that 'result' can go to that index and find the key i.e. symbol name. This is done to use result[x] below
		if ask_string in element_name[0] and ask_string not in result[index_element]: # passes iff the string is in element [0] and is also not repeated in symbol 
			print (element_name [1], "  ", element_name[0],"  ", result [index_element], "  ", element_name[2])
	print_footer ()
	return
''' 									Only prints Function Above this point 
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
''' 
def enter_again (function_pointer,table):
	while True:
		input_again = str (input("\nDo you want to try again (y,n) ?  ")) 
		input_again = input_again.lower()
		if input_again == 'y':
			False 
			function_pointer(table)
			break
		if input_again == 'n':
			False  
			print_footer ()
			print_menu ()
			break
		else:
			print ("Invalid input. Please try again.")


def build_periodic_table():
	file = open('periodic_Table.txt','r')
	table = dict() # table is a dictionary 
	for element in file:
		token = element.split()
		table[token[2].lower()] = (token[1].lower(), int (token[0]), float(token[3])) #table [token[2]] = key i.e. atomic symbol
	file.close()
	return table #table has now been assigned keys. 
	''' {'h': ('hydrogen', 1, 1.00794), 'he': ('helium', 2, 4.002602),} 
		table now contains keys but also shows what keys they are related to. 
		Next job would be to just take out keys. whoch is done in search_by_symbol function through "result" variable
		Next job would be to just take out info stored by keys i.e. ('hydrogen', 1,1.00794).  which is done in serach_by_symbol function through "element" varaible	'''

def res(table): # stores all the symbol names from table.
	result = []
	for store_symbol in table:
		result.append(store_symbol) #result has now stored all the symbol names from table
	return result

def search_by_symbol(table):
	ask_string = str(input("Please enter search string: "))
	ask_string = ask_string.lower()
	result = res(table) # this list stores symbol 
	element = [] # this list stores element name
	print_header () 

	for symbol in result:  
		element.append(table[symbol]) #element has now stored all the name, atomic weight and number in the respective order

	for symbol in result: #reads each line from result i.e reads each key >> element symbol
		if ask_string in symbol: #prints if symbol contains the string 
			print (table[symbol][1], "  ", table[symbol][0], "  ", symbol, "  ", table[symbol][2])

	for element_name in element: #reads each line from element  i.e reads each description >> name, number, weight
		index_element = element.index(element_name) #stores the index; 'result' can then go to that index and find the key i.e. symbol name. This is done to use result[x] below
		if ask_string in element_name[0] and ask_string not in result[index_element]: # passes iff the string is in element [0] and is also not repeated in symbol -- done so to avoid repition
			print (element_name [1], "  ", element_name[0],"  ", result [index_element], "  ", element_name[2])
	enter_again (search_by_symbol, table) 
	return

def mass_of_atom (table):
	min_mass = float (input("Please enter minimum mass: "))
	max_mass = float (input("Please enter maximum mass: "))
	result = res(table) 
	atom = []
	print_header ()
	for symbol in result:
		atom.append(table[symbol]) #atom has now stored all the name, atomic weight, and number

	for atomic_mass in atom: #reads each line from atom i.e reads each description >> name, number, weight
		index_atom = atom.index(atomic_mass) #finds the index so that 'result' can go to that index and find the key i.e. symbol name. This is done to use result[x] below
		if atomic_mass[2] >= min_mass and atomic_mass[2] <=max_mass:
			print (atomic_mass [1], " ", atomic_mass [0], " ", result [index_atom], " ", atomic_mass [2])
	enter_again (mass_of_atom, table) #mass_of_atom is used in enter_again function just to point at mass_of_atom

def molecular_formula (table):
	total_weight = 0 #stores updating molecular weight 
	result = res(table) # stores keys from the dictionary table 
	molecule = [] # stores all the name, atomic weight, and number of an element  

	for symbol in result:
		molecule.append(table[symbol]) #molecule has now stored all the name, atomic weight, and number

	while True: #stops if user enter '-1'  in atomic_symbol promt 
		found_symbol = 0 #tracks if the found_Symbol is found
		atomic_symbol = str(input("Please enter atomic symbol of element(Enter '-1' if you want to stop): "))
		atomic_symbol = atomic_symbol.lower()
		if atomic_symbol == '-1':
			False
			break
		else: 
			atomic_num = int (input("Please enter number of atoms of %s in molecule: " %atomic_symbol))
			for molecule_mass in molecule:  #reads each line from molecule  i.e reads each description >> name, number, weight
				index_molecule = molecule.index (molecule_mass) #finds the index so that 'result' can go to that index and find the key i.e. symbol name. This is done to use result[x] below
				if atomic_symbol == result[index_molecule]: #enters only if the key(i.e. symbol) matches exactly with the  atomic_symbol
					weight = molecule_mass[2] * atomic_num
					total_weight= total_weight + weight 
				if atomic_symbol != result [index_molecule] and atomic_symbol in result [index_molecule]: #enters if the user entered symbol name that is not the exact key. Will then show suggestions to the user
					print ("\nThe molecular mass cannot be found. The molecular formula contains an unknown element called '", atomic_symbol,"'")
					print ("Here is a list of what we think you might be looking for:") 
					printonly_search_by_symbol(table, atomic_symbol) #funtion serach by symbole is duplicated just for printing the list  ''' 
					print ("Please try again below\n")

	print ("The molecular mass is: ", total_weight)
	enter_again (molecular_formula, table)
	return

def select_menu(): #Selecting Menu Option
	#Loading the Periodic Table 
	table = build_periodic_table () 
	while True:
		menu_choice = int (input("\nPlease enter your choice: ")) 
		if menu_choice == 1:
			 search_string = search_by_symbol(table) 
			 select_menu ()
			 break
		if menu_choice ==2:
			mass_of_atom (table)
			select_menu ()
			break
		if menu_choice == 3:
			molecular_formula (table)
			select_menu ()
			break
		if menu_choice == 4:
			exit ()
			break
		False 
												#Main Function 
#Calling Menu
print_menu() 
#Asking user to enter choice and proceeding accordingly
choice = select_menu()


