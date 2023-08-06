Description: 
..\randSelector\randSelector\rand_selector module contains a function select_rand_item,
that can select a random a item from a data set with its associated probability



pip instalattion:
give the following command to add the module to your environment:
	 'pip install randSelector' 

get access to the functions by adding the following to the top of your script:
	 'from  randSelector import rand_selector'

to test, run command:
	select_rand_item( ((1, 0.6), (3, 0.4))), seed_num=10) from any script 

	OR

	run ..\MsAssesment\randSelector\unitTest\test_rand_selector.py from the zipped folder after installing pip package above
	this will unit test the module.Also, additional tests can be written to extend test covergage

