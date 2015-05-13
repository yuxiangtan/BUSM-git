def k_to_c(tempr):
	return tempr - 273.15

def f_to_k(tempr):
	temp_c=(tempr-32)*5/9+273.15
	reture temp_c

def f_to_c(temp):
	temp_k = f_to_k(temp)
	result = k_to_c(temp_k)
	return result
