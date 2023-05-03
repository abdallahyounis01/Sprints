def replace_char():

    st = input("Please Enter Your String : ")
    st_list = list(st)  # put string in list to modify it

    wanted_char = input("Please Enter The Wanted Char : ")
    if len(wanted_char) != 1:
        return "ERROR! ... Please Make Sure To Insert Just One Char "


    else:
        pos = int(input("Please Enter The Position Of The Char You Want To Replace : "))
        if pos >= len(st_list):  # check if index is in range of string
            print("ERROR! ... The Given Position Is Larger Than The String")

        st_list[pos] = wanted_char  # modify the list
        st = ''.join(st_list)
        print("Your New String Is : {} ".format(st))  # print the new string


replace_char()