import json

def load_data():
    with open("students123.json", "r") as file:
        x = json.load(file)
    return x
readed_data = load_data()
  
def try_or_main():
    while True:
        idoper = input("PRESS 1 TO TRY AGAIN AND PRESS 2 TO GO BACK TO MAIN: ")
        if idoper == "1":
            input("PRESS ENTER TO TRY")
            break
        elif idoper == "2":
            run_system()
            break
        else:
            print("ENTER VALID INPUT..")
            continue

def check_idcard_update(add_student_para):
    while True:
        id_value = input(add_student_para).strip()
        # Check ID card format
        if len(id_value) != 13 or not id_value.isdigit():
            print("\n[Error] PLEASE ENTER A FULL 13 DIGIT ID CARD NUMBER (NUMBERS ONLY)\n")
            try_or_main()
            continue

        # Check whether ID already exists
        if id_value in readed_data:
            print("\n[Error] THIS ID CARD NUMBER ALREADY HAS INFORMATION.")
            print("PLEASE ENTER A DIFFERENT ID CARD NUMBER.\n")
            try_or_main()
            continue

        # Everything is correct
        return id_value
# in 1
def check_rollno_update(roll_no_para):
    while True:
        id_value = input(roll_no_para).strip()
        # Check ID card format
        if len(id_value) != 7 or not id_value.isalnum():
            print("\n[Error] PLEASE ENTER A FULL ROLL NUMBER \n")
            try_or_main()
            continue

        if id_value[0:4] != "stf-":
            print("ROLL NO. MUST BE START WITH STF-\n(in this format stf-###)")
            continue

        all_rollno = []
        for stud, detail in readed_data.items():
            all_rollno.append(detail["roll no"])
            # Check whether ID already exists
        if id_value in all_rollno:
            print("\n[Error] THIS ROLL NUMBER ALREADY HAS GIVEN TO STUDENT.")
            print("PLEASE ENTER A DIFFERENT ROLL NO.\n")
            try_or_main()
            continue

        # Everything is correct
        return id_value
# in 4
def check_rollno_add(roll_no_para):
    while True:
        id_value = input(roll_no_para).strip().title()
        # Check ID card format
        if len(id_value) != 7 or not id_value.isalnum:
            print("\n[Error] PLEASE ENTER A FULL ROLL NUMBER \n")
            try_or_main()
            continue

        if id_value[0:4] != "Stf-":
            print("ROLL NO. MUST BE START WITH STF-\n(in this format stf-###)")
            continue

        all_rollno = []
        for stud, detail in readed_data.items():
            all_rollno.append(detail["roll no"])
        if id_value in all_rollno:
            print("\n[Error] THIS ROLL NUMBER ALREADY HAS GIVEN TO STUDENT.")
            print("PLEASE ENTER A DIFFERENT ROLL NO.\n")
            try_or_main()
            continue

        # Everything is correct
        return id_value
# in 1
def check_idcard_verify(target_id):
    while True:
        id_value = input(target_id).strip()
        for x,y in readed_data.items():
            if x == id_value:
                print("ID FOUND")
                return y
                break
            else :
                continue
        print("ID CARD NOT FOUND \nTRY AGAIN")
        idoper = input("PRESS 1 TO TRY AGAIN AND PRESS 2 TO GO BACK TO MAIN")
        if idoper == "1":
            input("PRESS ENTER TO TRY")
        elif idoper == "2":
            run_system()
        else:
            print("enter valid input").upper()
# in  6
def check_idcard(target_id):
    while True:
        id_value = input(target_id).strip()
        for x,y in readed_data.items():
            if x == id_value:
                print("ID FOUND")
                return id_value
                break
            else :
                continue
        print("ID CARD NOT FOUND \nTRY AGAIN")
        idoper = input("PRESS 1 TO TRY AGAIN AND PRESS 2 TO GO BACK TO MAIN")
        if idoper == "1":
            input("PRESS ENTER TO TRY")
        elif idoper == "2":
            run_system()
        else:
            print("enter valid input".upper())
# in 7
def get_alphaint(alphainteger):
    while True:
        value = input(alphainteger).strip().title()
        if value == "":
            print("Input cannot be empty!")
        else:
            return value 
            break   


def get_input(message):
    while True:
        value = input(message).strip().title()
        if value == "":
            print("Input cannot be empty!")
        elif not value.replace(" ", "").isalpha():
            print("ONLY ALPHABETS ARE ALLOWED")
        else:
            return value
            break
# in 8, 9
def get_integer(message):
    while True:
        value = input(message).strip()
        if value == "":
            print("Input cannot be empty!")
            continue
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")

def get_floatinp(message):

    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty!")
            continue

        try:
            value = float(value)
        except ValueError:
            print("ENTER VALID INPUT....")
            print("ONLY FLOAT INPUT!!")
            continue

        if value < 0 or value > 4:
            print("MUST BE BETWEEN 0 TO 4")
            continue

        return value
# in 10,11

def gendercheck(message):
    while True:
        gender = input(message).strip().title()
        if gender == "":
            print("Input cannot be empty!")
        elif not gender.replace(" ", "").isalpha():
            print("ONLY ALPHABETS ARE ALLOWED")
        elif gender != "Male" and gender != "Female" :
            print("ENTER VALID GENDER\nMALE or FEMALE")
        else:
            return gender
            break

def enlist_majors():
    print("ALL MAJORS THAT STUDENTS HAVE GIVEN BELOW: ")
    i=0
    all_majors = [] 
    for stud, detail in readed_data.items():
        if detail["major"] not in all_majors:
            all_majors.append(detail["major"])
    for each in all_majors:
        i+=1
        print(f"No. {i} : {each}")
# in 15

# main functions starting from here

def add_student():
    print("FOR ENTERING A NEW STUDENT FILL ALL THINGS ASK BELOW:")
    while True:#id card input
        idcard = check_idcard_update("1. ENTER THE ID CARD NUMBER\n(ENTER FULL ID WITHOUT SPACE): ")

        if len(idcard) == 13 and idcard.isdigit():
            idcard = int(idcard) 
            break
        else:
            print("\n[Error] PLEASE! ENTER FULL 13 DIGIT ID CARD NUMBER (NUMBERS ONLY)\n")

    name = get_input("2. ENTER THE FULL STUDENT NAME: ")
    age = get_integer("3. ENTER THE AGE OF STUDENT: ")
    gender = gendercheck("4. ENTER YOUR GENDER: ")
    city_name = get_input("5. ENTER THE CITY NAME OF STUDENT: ")
    roll_no = check_rollno_add("6. ENTER THE STUDENT ID(roll no.): ")
    Major = get_input("7. ENTER YOUR MAJOR SUBJECT: ")

    while True:  # for gpa
        gpa = input("7. ENTER STUDENT GPA: ")
        gpa = float(gpa)
        if gpa > 4 or gpa < 0:
            print("[ERROR] ENTER VALID INPUT")
        else :
            break

    readed_data[idcard] = {}
    readed_data[idcard]["name"] = name
    readed_data[idcard]["age"] = age
    readed_data[idcard]["gender"] = gender
    readed_data[idcard]["city"] = city_name
    readed_data[idcard]["roll no"] = roll_no
    readed_data[idcard]["major"] = Major
    readed_data[idcard]["gpa"] = gpa


    while True:
        try:
            with open("students123.json", "w") as file:
                json.dump(readed_data, file, indent=4)
                print("UPLOADED SUCCESSFULLY")
                break

        except:
            print("UPLOAD FAIL!!..  TRY AGAIN")
            input("PRESS ENTER TO TRY AGAIN")

        else:
            print("OPERATION DONE")
# add student upper 1

def view_all_students():
    print("---DATA OF ALL STUDENTS---")
    i=0
    for x ,y in readed_data.items():
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {x}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {y["name"]} \n AGE      : {y["age"]} \n CITY     : {y["city"]}\n GENDER   : {y["gender"]} \n ROLL NO. : {y["roll no"]}\n MAJOR    : {y["major"]}\n GPA      : {y["gpa"]}")
        print("- - - - - - - - - - - -")
# view student upper 2

def search_student_record():
    while True:
        print("\n1. SEARCH STUDENT'S ALL RECORD \n2. SEARCH STUDENT'S SPECIFIC RECORD")
        oper = input("WRITE NO. OF OPERATION GIVEN")
        if oper == "1":
            idcard_num = check_idcard("ENTER ID CARD NUMBER: ")
            print(f"RECORD OF ENTERED STUDENT IS GIVEN: ")
            print(f"ID CARD NO. {idcard_num}")
            print("           '-------------'")
            print(f"DETAILS:\n NAME     : {readed_data[idcard_num]["name"]} \n AGE      : {readed_data[idcard_num]["age"]} \n CITY     : {readed_data[idcard_num]["city"]}\n ROLL NO. : {readed_data[idcard_num]["roll no"]}\n MAJOR    : {readed_data[idcard_num]["major"]}\n GPA      : {readed_data[idcard_num]["gpa"]}")
            print("- - - - - - - - - - - -")
            break
        
        elif oper == "2":
            while True:
                idcard_num = check_idcard("ENTER ID CARD NUMBER: ")

                if idcard_num in readed_data:
                    y = readed_data[idcard_num]

                    print(f"\nTHE DETAILS FOR ID CARD {idcard_num} ARE GIVEN:")

                    for each in y.keys():
                        print(each)

                    tar_detail = input("\nNOW ENTER THE NAME OF DETAIL YOU WANT TO CHECK: ").lower().strip()

                    # Check whether the detail exists
                    if tar_detail not in y:
                        print(f"\n[ERROR] THE ENTERED DETAIL '{tar_detail}' "
                            "WAS NOT FOUND. TRY AGAIN FROM THE GIVEN DETAILS.")
                        continue

                    print(f"\nDETAIL IS:")
                    print(f"{tar_detail} : {y[tar_detail]}")
                    break
            break    

        else:
            print("ID CARD NOT FOUND.")
            continue            
# search record upper 3 

def update_student_record():
    while True:    
        id_update = check_idcard("ENTER THE ID CARD NUMBER OF STUDENT: ")
        xyz = readed_data[id_update]
        for a in xyz.keys():
            print(a.title())
        det_update = input("ENTER THE NAME OF DETAIL YOU WANT TO UPDATE:").lower()
        
        det_list = []
        for x in xyz.keys():   
            det_list.append(x) 
        if det_update not in det_list:
            print("DETAIL NOT FOUND IN RECORD...\nTRY AGAIN")
            continue
        
        if det_update == "gpa":
            print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
            value_update = get_floatinp("ENTER VALUE YOU WANT TO UPDATED: ")
            readed_data[id_update][det_update] = value_update
            print("UPDATED SUCCESSFULLY..")
            print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")

        elif det_update == "age":
            print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
            value_update = get_integer("ENTER VALUE YOU WANT TO UPDATED: ")
            readed_data[id_update][det_update] = value_update
            print("UPDATED SUCCESSFULLY..")
            print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")

        elif det_update == "roll no":
            print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
            value_update = check_rollno_update("ENTER VALUE YOU WANT TO UPDATED: ")
            readed_data[id_update][det_update] = value_update
            print("UPDATED SUCCESSFULLY..")
            print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")

        elif det_update == "gender":
            print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
            value_update = gendercheck("ENTER VALUE YOU WANT TO UPDATED: ")
            readed_data[id_update][det_update] = value_update
            print("UPDATED SUCCESSFULLY..")
            print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")
        
        else:
            print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
            value_update = get_alphaint("ENTER VALUE YOU WANT TO UPDATED: ")
            readed_data[id_update][det_update] = value_update
            print("UPDATED SUCCESSFULLY..")
            print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")
            break



        
        break
# update syudent upper 4

def delete_student():
    id_delete = check_idcard("ENTER THE ID CARD NUMBER OF STUDENT 5YOU WANT TO DELETE: ")
    oper = input(f"YOU WANT TO DELETE INFO FOR ID CARD NO. {id_delete}\n\n1. PRESS 1 TO DELETE RECORD PERMANANTLY.\n2. PRESS 2 TO GO BACK TO MAIN MENU.\n")
    
    if oper == "1":
        try: 
            del readed_data[id_delete]
            with open("students123.json", "w") as file:
                json.dump(readed_data, file, indent=4)
        except:
            print("FAILED TO DELETE..\nTRY AGAIN")

        else:
            print("DELETED SUCCESSFULLY...")
    elif oper == "2":
        run_system()

    else:
        print("ENTER VALID INPUT")










    #det_update = input("ENTER THE NAME OF DETAIL YOU WANT TO UPDATE:").lower()
    #print(f"THE DETAIL {det_update} HAS STORED VALUE :{readed_data[id_update][det_update]}")
    #value_update = get_alphaint("ENTER VALUE YOU WANT TO UPDATED: ")
    #readed_data[id_update][det_update] = value_update
    #print("UPDATED SUCCESSFULLY..")
    #print(f"THE DETAIL {det_update} IS NOW  STORING VALUE :{readed_data[id_update][det_update]}")
# delete student 5

def verify_student():
    id_verify = input("ENTER YOUR ID CARD NUMBER: ")

    try:    
        if id_verify in readed_data:
            print("STUDENT FOUND SUCCESSFULY!..\nDETAILS ARE GIVEN BELOW:")
            print(f"ID CARD NO. {id_verify}")
            print("           '-------------'")
            print(f"DETAILS:\n NAME     : {readed_data[id_verify]['name']} \n AGE      : {readed_data[id_verify]['age']} \n CITY     : {readed_data[id_verify]['city']}\n GENDER   : {readed_data[id_verify]['gender']} \n ROLL NO. : {readed_data[id_verify]['roll no']}\n MAJOR    : {readed_data[id_verify]['major']}\n GPA      : {readed_data[id_verify]['gpa']}")
            print("- - - - - - - - - - - -")
    except:
        print(f"NO ANY DETAILS ABOUT THis ID CARD ({id_verify}) FOUND")
        input("PRESS ENTER TO GO TO MAIN MENU")
# verify student upper 6

def search_by_roll():
    id_search_roll = input("ENTER THE ROLL NO. OF STUDENT YOU WANT TO FIND: ")
    try:
        print(f"FOR ID CARD NO. {id_search_roll}")
        print("               '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[id_search_roll]["name"]} \n AGE      : {readed_data[id_search_roll]["age"]} \n CITY     : {readed_data[id_search_roll]["city"]}\n GENDER   : {readed_data[id_search_roll]["gender"]} \n ROLL NO. : {readed_data[id_search_roll]["roll no"]}\n MAJOR    : {readed_data[id_search_roll]["major"]}\n GPA      : {readed_data[id_search_roll]["gpa"]}")
        print("- - - - - - - - - - - -")
    except:
        print("NO ROLL NUMBER FOUND!!...")
# search by roll no 7

def search_by_city():
    search_city = get_input("ENTER THE CITY NAME OF STUDENT YOU WANT TO FIND:").title().strip()
    print(f"---ALL STUDENTS FROM CITY \"{search_city.upper()}\"---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["city"] != search_city:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
    print(f"THERE ARE TOTAL {i} STUDENTS FROM \"{search_city}\".")
# SEARCH BY CITY 8 

def search_by_major():
    search_major = get_input("ENTER THE MAJOR OF STUDENT YOU WANT TO FIND:").title().strip()
    print(f"---ALL STUDENTS WITH MAJOR {search_major.upper()}---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["major"] != search_major:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
# search by major 9

def search_by_gpa():
    search_gpa = get_floatinp("ENTER THE GPA OF STUDENT YOU WANT TO FIND:")
    print(f"---ALL STUDENTS WITH GPA {search_gpa} ---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["gpa"] != search_gpa:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
# SEARCH BY GPA 10

def search_by_gpa_range():
    print("ENTER THE RANGE YOU WANT TO SEARCH")
    gpa_range_start = get_floatinp("ENTER THE STARTING OF GPA RANGE: ")
    gpa_range_end  = get_floatinp("ENTER THE ENDING OF GPA RANGE")
    print("STUDENTS FALLING IN RANGE GIVEN BELOW:\n(INCLUDING BOUDARIES OF RANGE)")
       
    if gpa_range_start > gpa_range_end :
        print("RANGE ENDING CAN NOT BE SMALL FROM STARTING\n TRY AGAIN")
        try_or_main()
        search_by_gpa_range()

    i=0
    for stud, detail in readed_data.items():
        if not gpa_range_start < detail["gpa"] < gpa_range_end:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
    print(f"\nTHERE ARE TOTAL {i} STUDENTS LIE IN THE RANGE.")
# search by gpa range 11

def search_by_age_range():
    print("ENTER THE AGE RANGE YOU WANT TO SEARCH")
    age_range_start = get_integer("ENTER THE STARTING OF AGE RANGE: ")
    age_range_end  = get_integer("ENTER THE ENDING OF AGE RANGE")
    print("STUDENTS FALLING IN RANGE GIVEN BELOW:\n(INCLUDING BOUDARIES OF RANGE)")
    
    if age_range_start > age_range_end :
        print("RANGE ENDING CAN NOT BE SMALL FROM STARTING\n TRY AGAIN")
        try_or_main()
        search_by_age_range()

    if age_range_start< 0 or age_range_end < 0:
        print("RANGE CAN NOT INCLUDE NEGATIVE VALUE..\n TRY AGAIN")
        try_or_main()
        search_by_age_range()

    i=0
    for stud, detail in readed_data.items():
        if detail["age"] <= age_range_start or detail["age"] >= age_range_end :
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
    print(f"\nTHERE ARE TOTAL {i} STUDENTS LIE IN THE RANGE.")
# search by age range 12 

def search_by_gender():
    search_gender = gendercheck("ENTER THE GENDER OF STUDENT YOU WANT TO FIND:")
    print(f"---ALL STUDENTS WITH GENDER {search_gender.upper()}---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["gender"] != search_gender:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
    
    print(f"\nTHERE ARE TOTAL {i} STUDENTS LIE IN THE RANGE.")
# search by gender 13

def search_by_academic_result():
    search_result = get_floatinp("ENTER THE GPA OF STUDENT YOU WANT TO FIND:")
    print(f"---ALL STUDENTS WITH RESULT {search_result} ---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["gpa"] != search_result:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")
    
    print(f"\nTHERE ARE TOTAL {i} STUDENTS WITH GPA {search_result}.")
# search by academic result 14

def search_by_major_group():
    name_major = get_input("ENTER THE NAME OF MAJOR FROM GIVEN :")
    print(f"---ALL STUDENTS WITH MAJOR {name_major.upper()}---")
       
    i=0
    for stud, detail in readed_data.items():
        if detail["major"] != name_major:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")

    print(f"\nTHERE ARE TOTAL {i} STUDENTS WITH MAJOR {name_major.upper()}.")
# search by major group 15

def search_by_name_initial():
    while True:
        name_initial = get_input("ENTER THE NAME'S FIRST LETTER: ")

        if len(name_initial) != 1:
            print("NAME INITIAL MUST BE OF 1 ALPHABET ONLY")
            continue

        print(f"---ALL STUDENTS WITH NAME INTITIAL {name_initial.upper()} ---")
        i=0
        for stud, detail in readed_data.items():
            if detail["name"][0] != name_initial:
                continue
            i+=1
            print(f"STUDENT NO. {i}")
            print(f"ID CARD NO. {stud}")
            print("           '-------------'")
            print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
            print("- - - - - - - - - - - -")

        print(f"\nTHERE ARE TOTAL {i} STUDENTS WITH NAME INITIAL {name_initial.upper()}.")
        break
# name intial 16

def search_student_low_gpa():
    search_low_gpa = get_floatinp("ENTER GPA TO FIND STUDENTS WITH LOW GPA THAN THAT: ")
 
    i=0
    for stud, detail in readed_data.items():
        if detail["gpa"] > search_low_gpa :
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")

    print(f"\nTHERE ARE TOTAL {i} STUDENTS WITH LOW GPA THAN {search_low_gpa}.")
# serch student with low gpa 17

def top_performing():
    print("-- STUDENT WITH HIGHEST GPA --")
    
    top = 0
    for stud, detail in readed_data.items():
        if detail["gpa"] > top :
            top = detail["gpa"]

    i=0
    for stud, detail in readed_data.items():
        if detail["gpa"] != top:
            continue
        i+=1
        print(f"STUDENT NO. {i}")
        print(f"ID CARD NO. {stud}")
        print("           '-------------'")
        print(f"DETAILS:\n NAME     : {readed_data[stud]["name"]} \n AGE      : {readed_data[stud]["age"]} \n CITY     : {readed_data[stud]["city"]}\n GENDER   : {readed_data[stud]["gender"]} \n ROLL NO. : {readed_data[stud]["roll no"]}\n MAJOR    : {readed_data[stud]["major"]}\n GPA      : {readed_data[stud]["gpa"]}")
        print("- - - - - - - - - - - -")

    print(f"\nTHERE ARE TOTAL {i} TOP STUDENTS WITH GPA {top}.")
# top student 18

def all_student_names():
    print("-- NAME OF ALL STUDENTS --")
    i=0
    for stud, detail in readed_data.items():
        i+=1
        print(f"No. {i} {readed_data[stud]["name"]}--({readed_data[stud]["roll no"]})")

    print(f"\nTHERE ARE TOTAL {i} NAMES OF ALL STUDENTS IN RECORD.")
# all student names

def all_student_major():
    print("-- ALL MAJORS PRESENT STUDENTS HAVE --")
    
    all_each_major = []
    for stud, detail in readed_data.items():
        if detail["major"] not in all_each_major :
            all_each_major.append(detail["major"])

    i=0
    for major in all_each_major:
        i+=1
        print(f"No. {i} {major}")

    print(f"\nTHERE ARE TOTAL {i} MAJORS WHICH CURRENT STUDENTS HAVE.")
# all current majors 20

def all_idcard_numbers():
    print("-- ALL IDCARD NUMBERS OF CURRENT STUDENTS --")

    i=0
    for stud in readed_data.keys():
        i+=1
        print(f"No. {i} {stud}--({readed_data[stud]["name"]})")

    print(f"\nTHESE ARE TOTAL {i} ID CARD NUMBERS OF ALL CURRENT STUDENTS..")
# all id card numbers 21

def all_student_rollno():
    print("-- ALL ROLL NUMBERS OF CURRENT STUDENTS --")

    i=0
    for stud, detail in readed_data.items():
        i+=1
        print(f"No. {i} {readed_data[stud]["roll no"]}--({readed_data[stud]["name"]})")

    print(f"\nTHESE ARE TOTAL {i} ROLL NO. OF STUDENTS.")
# all roll no of students 22

def all_each_city():
    print("-- ALL CITIES CURRENT STUDENTS COME FROM --")
    
    all_each_city = []
    for stud, detail in readed_data.items():
        if detail["city"] not in all_each_city :
            all_each_city.append(detail["city"])

    i=0
    for city in all_each_city:
        i+=1
        print(f"No. {i} {city}")

    print(f"\nTHESE ARE TOTAL {i} CITIES FROM WHERE STUDENTS ARE.")
# display all students from where students are 23

def gpa_top_least_average():
    
    gpa_list = []
    for stud, detail in readed_data.items():
        gpa_list.append(detail["gpa"])
    while True:
        operation = input("1. TOP GPA\n2. LEAST GPA \n3. AVERAGE GPA \n WRITE NO. OF OPERATION YOU WANT TO DO")
        if operation == "1":
            mac = max(gpa_list)
            print(f"THE HIGHEST GPA IN RESULT IS GIVEN:\n{mac}")
            break
        elif operation =="2":
            mini = min(gpa_list)
            print(f"THE LOWEST GPA IN RESULT IS GIVEN:\n{mini}")
            break
        elif operation == "3":
            aver = sum(gpa_list)/len(gpa_list)
            print(f"THE AVERAGE GPA IN RESULT IS GIVEN:\n{aver}")
            break
        else:
            print("ENTER VALID INPUT!!..")
# ALL GPA STATISTICS 24def 

def name_result_stat_no_by_gender():
    while True:    
        oper = get_input("\n1. MALE\n2. FEMALE\nWRITE NAME OF GENDER FROM GIVEN:")
        oper = oper.title()
        if oper == "Male" or oper == "Female":
            break
        else:
            print("ENTER VALID GENDER NAME:")
            continue

    gpa_list_m = []
    for stud, detail in readed_data.items():
        if detail["gender"] == oper :
            gpa_list_m.append(detail["gpa"])
    male_quant = len(gpa_list_m)
    male_aver = sum(gpa_list_m)/len(gpa_list_m)
    male_max = max(gpa_list_m)
    male_min = min(gpa_list_m)

    print(f"\n---NUMBER OF STUDENTS---\nTHE TOTAL NUMBER OF {oper} GENDER IS : {male_quant}")

    print(f"\n--- RESULT STATISTICS OF MALE STUDENTS ---\n1. HIGHEST GPA ACHIEVED IS : {male_max} \n2. LOWEST GPA SCRED IS : {male_min} \n3. AVERAGE GPA OF ALL MALE STUDENTS IS : {male_aver}")
        
    print(f"\n--- ALL NAMES OF STUDENTS OF GENDER ")
           
    i=0
    for stud, detail in readed_data.items():
        if detail["gender"] != oper:  
            continue
        i+=1
        print(f"No. {i} {detail["name"]} --({readed_data[stud]["roll no"]})")

    print(f"\nTHERE ARE TOTAL {i} STUDENTS OF GENDER {oper}.")
# alname result stat by gender 25

def name_result_stat_no_by_city():
    all_each_city = []
    for stud, detail in readed_data.items():
        if detail["city"] not in all_each_city :
            all_each_city.append(detail["city"])

    i=0
    for city in all_each_city:
        i+=1
        print(f"No. {i} {city}")
    
    
    
    while True:    
        oper = get_input("WRITE NAME OF CITY FROM GIVEN:")
        oper = oper.title()
        if oper in all_each_city:
            break
        else:
            print("ENTER VALID CITY NAME:")
            continue

    gpa_list_m = []
    for stud, detail in readed_data.items():
        if detail["city"] == oper :
            gpa_list_m.append(detail["gpa"])
    male_quant = len(gpa_list_m)
    male_aver = sum(gpa_list_m)/len(gpa_list_m)
    male_max = max(gpa_list_m)
    male_min = min(gpa_list_m)

    print(f"\n---NUMBER OF STUDENTS---\nTHE TOTAL NUMBER OF STUDENTS FROM {oper} IS : {male_quant}")

    print(f"\n--- RESULT STATISTICS OF STUDENTS FROM {oper} ---\n1. HIGHEST GPA ACHIEVED IS : {male_max} \n2. LOWEST GPA SCRED IS : {male_min} \n3. AVERAGE GPA OF ALL STUDENTS FROM {oper} : {male_aver}")
        
    print(f"\n--- ALL NAMES OF STUDENTS OF CITY {oper} ")
           
    i=0
    for stud, detail in readed_data.items():
        if detail["city"] != oper:  
            continue
        i+=1
        print(f"No. {i} {detail["name"]} --({readed_data[stud]["roll no"]})")

    print(f"\nTHERE ARE TOTAL {i} STUDENTS FROM CITY {oper.upper()}.")
# name reult stat from sa e city 26

def name_result_stat_no_by_major():
    all_each_major = []
    for stud, detail in readed_data.items():
        if detail["major"] not in all_each_major :
            all_each_major.append(detail["major"])

    i=0
    for major in all_each_major:
        i+=1
        print(f"No. {i} {major}")
    
    
    while True:    
        oper = get_input("WRITE NAME OF MAJOR FROM GIVEN:")
        oper = oper.title()
        if oper in all_each_major:
            break
        else:
            print("ENTER VALID MAJOR NAME:")
            continue


    gpa_list_m = []
    for stud, detail in readed_data.items():
        if detail["major"] == oper :
            gpa_list_m.append(detail["gpa"])
    male_quant = len(gpa_list_m)
    male_aver = sum(gpa_list_m)/len(gpa_list_m)
    male_max = max(gpa_list_m)
    male_min = min(gpa_list_m)

    print(f"\n---NUMBER OF STUDENTS---\nTHE TOTAL NUMBER OF STUDENTS MAJOR {oper} IS : {male_quant}")

    print(f"\n--- RESULT STATISTICS OF STUDENTS OF  {oper} ---\n1. HIGHEST GPA ACHIEVED IS : {male_max} \n2. LOWEST GPA SCRED IS : {male_min} \n3. AVERAGE GPA OF ALL STUDENTS WITH MAJOR {oper} : {male_aver}")
        
    print(f"\n--- ALL NAMES OF STUDENTS WITH MAJOR {oper} \n")
           
    i=0
    for stud, detail in readed_data.items():
        if detail["major"] != oper:  
            continue
        i+=1
        print(f"No. {i} {detail["name"]} --({readed_data[stud]["roll no"]})")

    print("-"*50) 
    print(f"\nTHERE ARE TOTAL {i} STUDENTS WITH MAJOR {oper}.")
# name reult stat from sa e city 26

def save_student_record():
    try:
        with open("students123.json", "w") as file:
            json.dump(readed_data, file, indent=4)
    except:
        print("FAILED TO SAVE..")
    else:
        print("SAVED SUCCESSFULLY...")


def load_student_record():
    while True:    
        try:
            load_data()
        except:
            print("\nFAILED TO LOAD DATA!!!...")
            try_or_main()
            continue
        else:
            print("DATA LOADED SUCCESSFULLY..")


def run_system():
    while True:

        print("\n" + "=" * 50)
        print("          STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("\n                 STUDENT RECORDS")
        print("-" * 50)
        print("1.  Add New Student")
        print("2.  View All Student Records")
        print("3.  Search Student Record")
        print("4.  Update Student Record")
        print("5.  Delete Student Record")
        print("6.  Verify Student Existence")

        print("\n                 SEARCH OPTIONS")
        print("-" * 50)
        print("7.  Search Student by Roll Number")
        print("8.  Search Students by City")
        print("9.  Search Students by Major")
        print("10. Search Students by GPA")

        print("\n                 SEARCH BY RANGES")
        print("-" * 50)
        print("11. Search Students by GPA Range")
        print("12. Search Students by Age Range")
        print("13. Search Students by Gender")

        print("\n                 RESULT & ACADEMIC OPTIONS")
        print("-" * 50)
        print("14. Search Students by Academic Result")
        print("15. Search Students by Major Group")
        print("16. Search Students by Name Initial")
        print("17. Search Students with Low GPA")
        print("18. Display Top-Performing Student")

        print("\n                 Student Statistics")
        print("-" * 50)
        print("19. Enlist All Student's name")
        print("20. Enlist All Majors Students Have")
        print("21. Enlist All ID Card Numbers of Students")
        print("22. Enlist All Roll No. of Students")
        print("23. Enlist All Cities From Where Students Are")
        print("24. GPA (top, least, average)".title())
        print("25. name, result statistics & no. of students of same gender".title())
        print("26. name, result statistics & no. of students from same city".title())
        print("27. name, result statistics & no. of students with same major".title())


        print("\n                 FILE MANAGEMENT")
        print("-" * 50)
        print("28. Save Student Records")
        print("29. Load Student Records")

        print("\n                 SYSTEM")
        print("-" * 50)
        print("30. Exit System")
        print("=" * 50)

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            print("\nADD NEW STUDENT SELECTED")
            add_student()

        elif choice == "2":
            print("\nVIEW ALL STUDENT RECORDS SELECTED")
            view_all_students()

        elif choice == "3":
            print("\nSEARCH STUDENT RECORD SELECTED")
            search_student_record()

        elif choice == "4":
            print("\nUPDATE STUDENT RECORD SELECTED")
            update_student_record()

        elif choice == "5":
            print("\nDELETE STUDENT RECORD SELECTED")
            delete_student()

        elif choice == "6":
            print("\nVERIFY STUDENT EXISTENCE SELECTED")
            verify_student()

        elif choice == "7":
            print("\nSEARCH STUDENT BY ROLL NUMBER SELECTED")
            search_by_roll()

        elif choice == "8":
            print("\nSEARCH STUDENTS BY CITY SELECTED")
            search_by_city()

        elif choice == "9":
            print("\nSEARCH STUDENTS BY MAJOR SELECTED")
            search_by_major()

        elif choice == "10":
            print("\nSEARCH STUDENTS BY GPA SELECTED")
            search_by_gpa()

        elif choice == "11":
            print("\nSEARCH STUDENTS BY GPA RANGE SELECTED")
            search_by_gpa_range()

        elif choice == "12":
            print("\nSEARCH STUDENTS BY AGE RANGE SELECTED")
            search_by_age_range()

        elif choice == "13":
            print("\n[SEARCH STUDENTS BY GENDER SELECTED]")
            search_by_gender()

        elif choice == "14":
            print("\n[SEARCH STUDENTS BY ACADEMIC RESULT SELECTED]")
            search_by_academic_result()

        elif choice == "15":
            print("\n[SEARCH STUDENTS BY MAJOR GROUP SELECTED]")
            enlist_majors()
            search_by_major_group()

        elif choice == "16":
            print("\n[SEARCH STUDENTS BY NAME INITIAL SELECTED]")
            search_by_name_initial()

        elif choice == "17":
            print("\n[SEARCH STUDENTS WITH LOW GPA SELECTED]")
            search_student_low_gpa()

        elif choice == "18":
            print("\n[DISPLAY TOP-PERFORMING STUDENT SELECTED]")
            top_performing()

        elif choice == "19":
            print("\n[Enlist All Student's name]".upper())
            all_student_names()
                 
        elif choice == "20":
            print("\n[Enlist All Majors Students Have]".upper())
            all_student_major()

        elif choice == "21":
            print("\n[Enlist All ID Card Numbers of Students]".upper())
            all_idcard_numbers()

        elif choice == "22":
            print("\n[Enlist All Roll No. of Students]".upper())
            all_student_rollno()

        elif choice == "23":
            print("\n[Enlist All Majors From Where Students Are]".upper())
            all_each_city()

        elif choice == "24":
            print("\n[Gpa (Top, Least, Average]".upper())
            gpa_top_least_average()

        elif choice == "25":
            print("\n[all names and numbers of students by gender]".upper())
            name_result_stat_no_by_gender()

        elif choice == "26":
            print("\n[all names and number of students from same city]".upper())
            name_result_stat_no_by_city()

        elif choice == "27":
            print("\n[all names and number of students by city]".upper())
            name_result_stat_no_by_major()

        elif choice == "28":
            print("\n[Save Student Records]".upper())
            save_student_record()

        elif choice == "29":
            print("\n[Load Student Records]".upper())
            load_student_record()

        elif choice == "30":
            print("\n[Exit System]".upper())
            oper = input("IT WILL CLOSE THE WHOLE PROGRAMME AND FILE\n1. PRESS A TO EXIT\n2. PRESS M TO GO TO MAIN MENU").lower()
            if oper == "a":
                break
            elif oper == "m":
                continue
            else:
                print("NOT CORRECT INPUT SELECTED TRY AGAIN..")

        else:
            print("\nINVALID CHOICE!")
            print("PLEASE ENTER A NUMBER FROM 1 TO 23.")

        input("\nPRESS ENTER TO CONTINUE...")

# Run the application
if __name__ == "__main__":
    run_system()