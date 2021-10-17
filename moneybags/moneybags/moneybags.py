###################################################
#   Weekly Exercise 7: Moneybags
#   CMPUT 274 Fall 2020
#
#   Ashley Davis - 1616898
###################################################

"""readinput() will read in a certain number of lines of input as
    determined by the value of num_app
input values:  *num_app - the number of applicants
return values: *applicants - list with wealth of each applicant"""


def readinput(num_app):

    # create empty applicant list with wealth as values
    applicants = [None]*num_app

    # fill the list with each line of input from the user
    for person in range(num_app):
        applicants[person] = int(input())

    return applicants


"""determineN() will find the highest number N such that there are
    at least N applicants with at least N million dollars
input values:  *num_app - the number of applicants
               *applicants - list with wealth of each applicant
return values: *None, but prints highest N value"""


def determineN(num_app, applicants):

    # start at the highest possible N = num_app, and then go down
    for N in range(num_app, 0, -1):
        '''if the applicant of the Nth position from the end of the
        list has a value >= N, then all values to the end of the
        list will be >= N'''
        if applicants[-N] >= N:
            print(N)
            break
    return


"""main() is the main function which calls readinput() and
    determineN() to run the program, as well as reads the input for
    number of applicants and sorts the list of applicant wealth"""


def main():

    # input number of applicants
    num_app = int(input())
    # read lines of input and create list of applicant wealth
    applicants = readinput(num_app)
    # sort the list from smallest integer to largest
    applicants.sort()
    # print out the highest value of N
    determineN(num_app, applicants)


if __name__ == '__main__':
    main()
