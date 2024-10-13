import re
def password_criteria(p):
    length_criteria=len(p)>=8
    uppercase_criteria=bool(re.search(r'[A-Z]',p))
    lowercase_criteria=bool(re.search(r'[a-z]',p))
    num_criteria=bool(re.search(r'[0-9]',p))
    specialchar_criteria=bool(re.search(r'[!@#$%&*?]',p))

    score=sum([length_criteria,uppercase_criteria,lowercase_criteria,num_criteria,specialchar_criteria])

    feedback=[]
    if not length_criteria:
        feedback.append("Not long enough")
    if not uppercase_criteria:
        feedback.append("atleast one Uppercase letter")
    if not lowercase_criteria:
        feedback.append("Must include lower cases")
    if not num_criteria:
        feedback.append("include numbers")
    if not specialchar_criteria:
        feedback.append("include special characters")
    
    if score==5:
        print(" The password is strong ")
    elif 3<=score<5:
        print("The password is medium")
    else:
        print("The password is weak")
    return feedback

p=input("enter the password to check: \n")
feedback= password_criteria(p)
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(" ",comment)
