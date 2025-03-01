import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("WELCOME TO STUDENT INFORMATION MANAGEMENT SYSTEM OF GRD 11 2024 - 25")

stud_nm = str(input("Please enter the student's full name:"));

stud_age = float(input("Please enter the student's age:"));
stud_dob = input("Please enter the student's DOB :");
stud_gen = str(input("Please enter the student's gender:"));
stud_cls = str(input("Please enter the student's class:"));
stud_prnt = str(input("Please enter the student's parent's full name:"));
stud_no = int(input("Please enter the student's contact number:"));

if stud_cls == "11A" or "11B" or "11C":
    stud_stream = input("Please enter the student's Stream(PCM, PCB, PCMB or COM):")
    stud_5 = input("Please enter the student's 5th Subject(CS, PSY, PE, PAINT:")
    stud_skill = input("Please enter the student's skill subject(AI, MAR, NONE):")
    print("Confirmation: Student's subjects are -", stud_stream, stud_5, stud_skill)
    con = input("Type OK to confirm or GB to go back")
    
    if con == "OK":
        stud_subs = stud_stream, stud_5 , stud_skill
    elif con == "GB":
         alt1 = input("Please select the detail to alter (stream, 5th, skill):")
         
         if alt1 == "stream":
             stud_stream = input("Please enter the student's Stream(PCM, PCB, or COM):")
             print("Confirmation: Student's subjects are -", stud_stream, stud_5, stud_skill)
             con = input("Type OK to confirm or GB to go back")
             
         elif alt1 == "5th":
              stud_5 = input("Please enter the student's 5th Subject(CS, PSY, PE, PAINT, BIO:")
              print("Confirmation: Student's subjects are -", stud_stream, stud_5, stud_skill)
              con = input("Type OK to confirm or GB to go back")
              
         elif alt1 == "skill":
              stud_skill = input("Please enter the student's skill subject(AI, MAR, NONE):")
              print("Confirmation: Student's subjects are -", stud_stream, stud_5, stud_skill)
              con = input("Type OK to confirm or GB to go back")
              
    stud_subs = stud_stream, stud_5 , stud_skill  
            
details = [stud_nm, stud_age, stud_dob, stud_gen, stud_cls, stud_prnt, stud_no, stud_subs]

folders = str(input("Select the folder to view (Marks/ Attendance/ Personal Details): "))


if folders == "Personal Details":
    print("Till date the details are as follows:")
    print(details)
    opt= input("Do you wish to make any changes? (Yes or No)")
    if opt == "Yes":
        alt = input("Please select the detail to alter (name, age, gender, dob, class, parent, number ):")
        if alt == "name":
            stud_nm = str(input("Please enter the student's full name:"));
        elif alt == "age":
            stud_age = float(input("Please enter the student's age:"));
        elif alt == "dob":
            stud_dob = input("Please enter the student's DOB :");
        elif alt == "gen":
            stud_gen = str(input("Please enter the student's gender:"));
        elif alt == "class":
            stud_cls = str(input("Please enter the student's class:"));
        elif alt == "parent":
            stud_prnt = str(input("Please enter the student's parent's full name:"));
        elif alt == "number":
            stud_no = int(input("Please enter the student's contact number:"));
            
        print("The updated details are: ", details)
        
    elif opt == "No":
        print("Ok, thank you for viewing")
    
elif folders == "Marks":
    Mark_fold = input("Please select the exam (1,2,3,4):")
    if Mark_fold == "1":
        print("Welcome to Marksheet of Pre Midterm Assessment for", stud_nm)
        if stud_stream == "PCM":
            eng = float(input("Please enter marks scored in English (30):"))
            phy = float(input("Please enter marks scored in Physics (30):"))
            chem = float(input("Please enter marks scored in Chemistry (30):"))
            math = float(input("Please enter marks scored in Maths (30):"))      
        elif stud_stream == "PCB":
            eng = float(input("Please enter marks scored in English (30):"))
            phy = float(input("Please enter marks scored in Physics (30):"))
            chem = float(input("Please enter marks scored in Chemistry (30):"))
            bio = float(input ("Please enter marks scored in Biology (30):"))
        elif stud_stream == "COM":
            eng = float(input("Please enter marks scored in English (30):"))
            acc = float(input ("Please enter marks scored in Accountancy (30):"))
            bs = float(input("Please enter marks scored in Business Studies (30):"))
            eco = float(input("Please enter marks scored in Economics (30):"))
            
        if stud_5 == "CS":
            cs = float(input("Please enter marks scored in Computer Science (30):"))
        elif stud_5 == "PSY":
            psy = float(input("Please enter marks scored in Psychology (30):"))
        elif stud_5 == "PE":
            pe = float(input("Please enter marks score in Physical Education (30):"))
        elif stud_5 == "PAINT":
            pnt = float(input("Please enter marks score in Painting (30):"))
        elif stud_5 == "BIO":
            bio2 = float(input("Please enter marks score in Biology (30):"))

        if stud_skill == "AI":
            ai = float(input("Please enter marks scored in AI (30):"))

        elif stud_skill == "MAR":
            mar = float(input("Please enter marks scored in Marketing (30):"))

        elif stud_skill == "NONE":
            skill =  "NA" or 0
            print("Skill subject not opted by the student")

        marksheet = [eng, phy or acc, chem or bs, math or bio or eco, cs or psy or pnt or pe or bio2, ai or mar or skill]
        print ("The marks scored by the student (English, stream, 5th, skill order) are:", marksheet)
        avg = (eng+ phy or acc + chem or bs + math or eco or bio + cs or psy or pnt or pe or bio2 + ai or mar or skill)/6
        print ("The student's percentage is:", avg)

        plt.title = ("Marksheet of PreMidTerm")
        colours = np.array([0,10,20,30,40, 45])
        subs = ["English", "Core1", "Core2", "Core3", "5th Sub", "Skill"]
        plt.scatter(subs, marksheet,c= colours ,cmap= "viridis")
        plt.xticks(rotation = 45)
        plt.xlabel = ("Subjects")
        plt.ylabel = ("Marks")
        plt.show()


    if Mark_fold == "2":
            print("Welcome to Marksheet of Midterm Assessment for", stud_nm)
            if stud_stream == "PCM":
                eng = float(input("Please enter marks scored in English (80):"))
                phy = float(input("Please enter marks scored in Physics (70):"))
                chem = float(input("Please enter marks scored in Chemistry (70):"))
                math = float(input("Please enter marks scored in Maths (80):"))            
            elif stud_stream == "PCB":
                eng = float(input("Please enter marks scored in English (80):"))
                phy = float(input("Please enter marks scored in Physics (70):"))
                chem = float(input("Please enter marks scored in Chemistry (70):"))
                bio = float(input ("Please enter marks scored in Biology (70):"))
            elif stud_stream == "COM":
                eng = float(input("Please enter marks scored in English (80):"))
                acc = float(input ("Please enter marks scored in Accountancy (80):"))
                bs = float(input("Please enter marks scored in Business Studies (80):"))
                eco = float(input("Please enter marks scored in Economics (80):"))
                
            if stud_5 == "CS":
                cs = float(input("Please enter marks scored in Computer Science (70):"))
            elif stud_5 == "PSY":
                psy = float(input("Please enter marks scored in Psychology (70):"))
            elif stud_5 == "PE":
                pe = float(input("Please enter marks score in Physical Education (70):"))
            elif stud_5 == "PAINT":
                pnt = float(input("Please enter marks score in Painting (30):"))
            elif stud_5 == "BIO":
                bio2 = float(input("Please enter marks score in Biology (70):"))

            if stud_skill == "AI":
                ai = float(input("Please enter marks scored in AI (50):"))

            elif stud_skill == "MAR":
                mar = float(input("Please enter marks scored in Marketing (50):"))

            elif stud_skill == "NONE":
                skill =  "NA" or 0
                print("Skill subject not opted by the student")

            marksheet = [eng, phy or acc, chem or bs, math or bio or eco, cs or psy or pnt or pe or bio2, ai or mar or skill]
            print ("The marks scored by the student (English, stream, 5th, skill order) are:", marksheet)
            avg = (((eng*100)/80)+ ((phy*100)/70) or ((acc*100)/80) + ((chem*100)/70) or ((bs*100)/80) + ((math*100)/80) or ((eco*100)/80) or ((bio*100)/70) + ((cs*100)/70) or ((psy*100)/70) or ((pnt*100)/30) or ((pe*100)/70) or ((bio2*100)/70) + ((ai*100)/50) or ((mar*100)/50) or skill)/6
            print ("The student's percentage is:", avg)

            plt.title = ("Marksheet of MidTerm")
            colours = np.array([0,10,20,30,40, 45])
            subs = ["English", "Core1", "Core2", "Core3", "5th Sub", "Skill"]
            plt.scatter(subs, marksheet,c= colours ,cmap= "viridis")
            plt.xticks(rotation = 45)
            plt.xlabel = ("Subjects")
            plt.ylabel = ("Marks")
            plt.show()


    if Mark_fold == "3":
            print("Welcome to Marksheet of Pre Midterm Assessment 2 for", stud_nm)
            if stud_stream == "PCM":
                eng = float(input("Please enter marks scored in English (30):"))
                phy = float(input("Please enter marks scored in Physics (30):"))
                chem = float(input("Please enter marks scored in Chemistry (30):"))
                math = float(input("Please enter marks scored in Maths (30):"))      
            elif stud_stream == "PCB":
                eng = float(input("Please enter marks scored in English (30):"))
                phy = float(input("Please enter marks scored in Physics (30):"))
                chem = float(input("Please enter marks scored in Chemistry (30):"))
                bio = float(input ("Please enter marks scored in Biology (30):"))
            elif stud_stream == "COM":
                eng = float(input("Please enter marks scored in English (30):"))
                acc = float(input ("Please enter marks scored in Accountancy (30):"))
                bs = float(input("Please enter marks scored in Business Studies (30):"))
                eco = float(input("Please enter marks scored in Economics (30):"))
                
            if stud_5 == "CS":
                cs = float(input("Please enter marks scored in Computer Science (30):"))
            elif stud_5 == "PSY":
                psy = float(input("Please enter marks scored in Psychology (30):"))
            elif stud_5 == "PE":
                pe = float(input("Please enter marks score in Physical Education (30):"))
            elif stud_5 == "PAINT":
                pnt = float(input("Please enter marks score in Painting (30):"))
            elif stud_5 == "BIO":
                bio2 = float(input("Please enter marks score in Biology (30):"))

            if stud_skill == "AI":
                ai = float(input("Please enter marks scored in AI (30):"))

            elif stud_skill == "MAR":
                mar = float(input("Please enter marks scored in Marketing (30):"))

            elif stud_skill == "NONE":
                skill =  "NA" or 0
                print("Skill subject not opted by the student")

            marksheet = [eng, phy or acc, chem or bs, math or bio or eco, cs or psy or pnt or pe or bio2, ai or mar or skill]
            print ("The marks scored by the student (English, stream, 5th, skill order) are:", marksheet)
            avg = (eng+ phy or acc + chem or bs + math or eco or bio + cs or psy or pnt or pe or bio2 + ai or mar or skill)/6
            print ("The student's percentage is:", avg)

            plt.title = ("Marksheet of PostMidTerm")
            colours = np.array([0,10,20,30,40, 45])
            subs = ["English", "Core1", "Core2", "Core3", "5th Sub", "Skill"]
            plt.scatter(subs, marksheet,c= colours ,cmap= "viridis")
            plt.xticks(rotation = 45)
            plt.xlabel = ("Subjects")
            plt.ylabel = ("Marks")
            plt.show()

    if Mark_fold == "4":
            print("Welcome to Marksheet of Annual Assessment for", stud_nm)
            if stud_stream == "PCM":
                eng = float(input("Please enter marks scored in English (80):"))
                phy = float(input("Please enter marks scored in Physics (70):"))
                chem = float(input("Please enter marks scored in Chemistry (70):"))
                math = float(input("Please enter marks scored in Maths (80):"))            
            elif stud_stream == "PCB":
                eng = float(input("Please enter marks scored in English (80):"))
                phy = float(input("Please enter marks scored in Physics (70):"))
                chem = float(input("Please enter marks scored in Chemistry (70):"))
                bio = float(input ("Please enter marks scored in Biology (70):"))
            elif stud_stream == "COM":
                eng = float(input("Please enter marks scored in English (80):"))
                acc = float(input ("Please enter marks scored in Accountancy (80):"))
                bs = float(input("Please enter marks scored in Business Studies (80):"))
                eco = float(input("Please enter marks scored in Economics (80):"))
                
            if stud_5 == "CS":
                cs = float(input("Please enter marks scored in Computer Science (70):"))
            elif stud_5 == "PSY":
                psy = float(input("Please enter marks scored in Psychology (70):"))
            elif stud_5 == "PE":
                pe = float(input("Please enter marks score in Physical Education (70):"))
            elif stud_5 == "PAINT":
                pnt = float(input("Please enter marks score in Painting (30):"))
            elif stud_5 == "BIO":
                bio2 = float(input("Please enter marks score in Biology (70):"))

            if stud_skill == "AI":
                ai = float(input("Please enter marks scored in AI (50):"))

            elif stud_skill == "MAR":
                mar = float(input("Please enter marks scored in Marketing (50):"))

            elif stud_skill == "NONE":
                skill =  "NA" or 0
                print("Skill subject not opted by the student")

            marksheet = [eng, phy or acc, chem or bs, math or bio or eco, cs or psy or pnt or pe or bio2, ai or mar or skill]
            print ("The marks scored by the student (English, stream, 5th, skill order) are:", marksheet)
            avg = (((eng*100)/80)+ ((phy*100)/70) or ((acc*100)/80) + ((chem*100)/70) or ((bs*100)/80) + ((math*100)/80) or ((eco*100)/80) or ((bio*100)/70) + ((cs*100)/70) or ((psy*100)/70) or ((pnt*100)/30) or ((pe*100)/70) or ((bio2*100)/70) + ((ai*100)/50) or ((mar*100)/50) or skill)/6
            print ("The student's percentage is:", avg)

            plt.title = ("Marksheet of Final Assessment")
            colours = np.array([0,10,20,30,40, 45])
            subs = ["English", "Core1", "Core2", "Core3", "5th Sub", "Skill"]
            plt.scatter(subs, marksheet,c= colours ,cmap= "viridis")
            plt.xticks(rotation = 45)
            plt.xlabel = ("Subjects")
            plt.ylabel = ("Marks")
            plt.show()

    
elif folders == "Attendance":
    attendance_records = {}

    def mark_attendance(stud_nm):
        
        if stud_nm in attendance_records:
            print(stud_nm," has already been marked present.")
        
        else:
            attendance_records[stud_nm] = True
            print(stud_nm,"has been marked present.")
            
    def no_attendance(stud_nm): 
        
        attendance_records[stud_nm] = False
        print(stud_nm, "has been marked absent")

    def main():
        while True:
            print("Attendance Tracker")
            print("1. Mark Attendance")
            print("2. View Attendance Records")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                ap = input("Absent or present: ")
                if ap == "Present":
                    mark_attendance(stud_nm)

                elif ap == "Absent":
                    no_attendance(stud_nm) 
                    
            elif choice == '2':
                print("\nAttendance Records:")
                for student, attendance in attendance_records.items():
                    print(f"{student}: {'Present' if attendance else 'Absent'}")
            elif choice == '3':
                print("Exiting Attendance Tracker.")
                break
            else:
                print("Invalid choice. Please choose again.")

    if __name__ == "__main__":
        main()
        


    
