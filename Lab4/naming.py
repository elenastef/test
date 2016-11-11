# This program validates a Texas highway name

def valid_highway(highway):

	# List of valid highway prefixes
	valid_highway_abbrev = ["IH","US","UA","SH","SL","SS","BI","BS","BU","BF","UR","RR","FM","RM","PR","RE","PA"]

	length = len(highway)
        correct_length = False	
        if length >= 4 and length <=6:			# Test for correct length
                correct_length = True

        # Grab Highway Prefix
	roadType = highway[0 : 2]		        # Grab road type
        correct_type = roadType in valid_highway_abbrev # Test for valid prefix

	#Grab Highway Numbers
        number = highway[2 : ]        
        correct_numbers = number.isdigit() 		# Test for valid numbers

        is_valid = correct_length and correct_type and correct_numbers
        return is_valid 


