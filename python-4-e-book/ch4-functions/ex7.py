# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string

try:
    score = float(input('Enter a score from 0.0 to 1.0: '))

except:
    print('only numbers')
    quit()
def computegrade(score):
    if (score > 1.0):
        return ('out of range')
    elif (score >= 0.9):
        return ('A')
    elif (score >= 0.8):
        return ('B')
    elif (score >= 0.7):
        return ('C')
    elif (score >= 0.6):
        return ('D')
    else:
        return ('F')

print(computegrade(score))
