# separates year and month as two diff columns
def make_year_tuple (year_column):
	tokens = year_column.split()
	year = int (tokens[0]) #year 
	rainfall = [float(x) for x in tokens[1:]] #rainfall == month and if float is not entered it will be stored as string.
	return (year, rainfall) #we are here passing list, thus return is able to transfer two values. or else return cannot 'return' more than one value

def load_table():
	all_data = dict() #all_data is a dictionary 
	file = open('njrainfall.txt','r')
	for year in file:
		year_record = make_year_tuple (year)
		all_data[year_record[0]] = year_record[1] #all_data [year_record[0]]  ==> key value 
		# year_record [0] => Year 
		# year_record [1] => Months 
		# We are here assigning year as a 'key' to its repective monthly rainfall data
	file.close()
	return all_data

def find_average(table, month) :
    # each element in table is a tuple with two entries (year, month)
    # entry 0 => year
    # entry 1 => monthly rainfalls for the year

    # Now compile a list of particular month from all_years 
    all_years = [table[x][month] for x in table ] 

    # -----------------------------------------------------------------------------------
    # >>>>>>>>>>>> This is same as:  													
    # all_years = []
   	# for x in table:
    # 	all_years.append(table[x][month])
    # >>>>>>>>>>>>> all_years Goes to key x 
    # >>>>>>>>>>>>>> key x identifies monthly data as it has monthly rainfall data stored 
    # >>>>>>>>>>>>>> stores particular month as month are stored as tuple
    # -----------------------------------------------------------------------------------
    # Getting the average value of month
    sum = 0.0
    for total in all_years:
        sum += total
    return sum / len(all_years)

												#Main Function 
table = load_table ()
first_year = min(table.keys()) ##access keys of the dictionary; remember table gets dictionary value 
last_year = max(table.keys()) #access keys of the dictionary; remember table gets dictionary value 

print ("New Jersey Rainfall Data are available from ", first_year, " to ", last_year)
print ("~~~~~~~~~~~~~~~Please enter -1 to stop.~~~~~~~~~~~~~~~~~~~~~")
while True:
	try:
		year = int(input("Please enter a year (1895 - 2014) (enter '-1' to stop): " ))
		if year == -1:
			False
			break
		while True:
			month = int (input("Please enter month (1-12): "))
			if month > 12 or month < 1:
				raise ValueError
			else:
				import utility_month_name # calls another file where month names are stored.
				print ("Year entered: ", year)
				print ("Monthly Rainfall for ", utility_month_name.month_name(month)," is: ", table [year][month-1], " ") #month-1 to account for indexing 
				#Calling Average Function 
				avg = find_average(table, month-1)
				print ("Average rainfall for ", utility_month_name.month_name(month), " is:", avg) 
				break 
	except KeyError:
		print ("The entered year is not valid. Please try again.")
	except ValueError:
		print ("The entered month is not valid. Please try again.")
