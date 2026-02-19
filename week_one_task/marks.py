

#generating result according to student attendence ,and score.

#student's data:
attendence = int(input("enter your attendence:"))               
assignment_score = int(input("enter your asssignment score:"))  
final_project_score = int(input("enter your final project:"))

if attendence >= 75 and attendence >= 0 and attendence <= 100:    #attendence should be between 0 and 100 and should be greater than 75%
    print("your attendence is", attendence)
    if final_project_score > 80 and assignment_score > 70:      #final progect and assignment score limitations for good score.
        print("result: pass with good score")
    elif final_project_score > 50 and final_project_score < 80 and assignment_score > 50:  #final project and assignment score limitations for pass score.
        print("result: pass") 
    else:
            print("insufficient score ")      #when user didn't meet the score requirements .
            print("result: fail")

else:
    print("insufficient attendence")          #when user didn't meet the attendence requirements.
    print("result: fail")        

 

