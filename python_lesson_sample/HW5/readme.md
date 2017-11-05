Homework 5:
1. Purpose: build a console software to allow user to key in items and amount repeatedly, review stored items and amount, and exit.
	1.1. Use a loop ("for" or "while")
	1.2. In each loop, 
	   1.2.1 a menu is displayed with choices for user to pick:
		"1. Input item and amount
		 2. Display stored items and amount
		 3. Exit "
	   1.2.2 take the user choice of 1 or 2 or 3
	  	1.2.2.1 if user choose 1, ask user to put in name of item and read in the name of item as string; then ask user to put in amount and read in as integer. Store the item in dictionary using "item":amount.
		1.2.2.2 if user choose 2, display the dictionary content 
		1.2.2.3 if user choose 3, display the dictionary content and break out of loop
	1.3. Make a limit of number of items to be 5. If the stored items in dictionary reaches 5, display the dictionary content and break out of loop
	1.4 Make the display of dictionary content as a function being called in different places. The display of dictionary will be display keys, values and key-value pairs
