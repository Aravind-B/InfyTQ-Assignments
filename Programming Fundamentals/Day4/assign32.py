#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    list1=[]
    for i in patient_medical_speciality_list:
        if isinstance(i, str):
            list1.append(i)
    max1=max(list1,key=list1.count)
    speciality=medical_speciality[max1]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[101,'O',102,'O',302,'P',305,'E',401,'O',656,'P']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)