def leap_year():

    year = int(input("Please Enter The Year :"))
    if year % 4 == 0 and (year % 100 != 0 and year % 400 == 0):
        print("{} Is A Leap Year".format(year))


    else:
        print("{} Is Not A Leap Year".format(year))

leap_year()