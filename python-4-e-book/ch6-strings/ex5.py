# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

# str = 'X-DSPAM-Confidence:0.8475'
# search = str.find(':')
# slice = str[search+1:]
# slice_fl = float(slice)
# print(slice_fl)

# #print uct.ac.za
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# d_search = data.find('@')
# n_search = data.find(' ', d_search)
# slice_data = data[d_search + 1:n_search]
# print(slice_data)

# did it myself
# print '09:14:16'
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
a_search = data.find('5')
b_search = data.find(' ', a_search + 2)
# print(data[b_search:])
print(data[a_search+2:b_search])
# print(a_search)