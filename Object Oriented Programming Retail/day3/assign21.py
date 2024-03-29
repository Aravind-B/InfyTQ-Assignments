#OOPR-Assgn-21
class Patient:
    def __init__(self,patient_id,patient_name,list_of_lab_test_ids):
        self.__patient_id=patient_id
        self.__patient_name=patient_name
        self.__list_of_lab_test_ids=list_of_lab_test_ids
        self.__lab_test_charge=None
    def get_patient_id(self):
        return self.__patient_id
    def get_patient_name(self):
        return self.__patient_name
    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids
    def get_lab_test_charge(self):
        return self.__lab_test_charge
    def calculate_lab_test_charge(self):
        #lab1=LabTestRepository()
        self.__lab_test_charge=0
        for i in self.__list_of_lab_test_ids:
            #print(LabTestRepository.get_test_charge(i))
            if(LabTestRepository.get_test_charge(i)!=-1):
                self.__lab_test_charge+=LabTestRepository.get_test_charge(i)
                '''
                self.__lab_test_charge+=\
                LabTestRepository.__list_of_lab_test_charge[LabTestRepository.get_test_charge(i)]
                '''
            else:    
                self.__lab_test_charge+=0
            #print(self.__lab_test_charge)

class LabTestRepository:
    __list_of_hospital_lab_test_ids=["L101","L102","L103","L104"]
    __list_of_lab_test_charge=[2020,1750.50,5700,1320.50]
    @staticmethod
    def get_test_charge(lab_test_id):
        if(lab_test_id in LabTestRepository.__list_of_hospital_lab_test_ids):
            ind=LabTestRepository.\
            __list_of_hospital_lab_test_ids.index(lab_test_id)
            return LabTestRepository.__list_of_lab_test_charge[ind]
        else:
            return -1

lab_test_list1=["L101","L103","L104",'L105']
patient1=Patient(1010,"Sam",lab_test_list1)
patient1.calculate_lab_test_charge()
print("Patient id:",patient1.get_patient_id(),"\nPatient name:",patient1.get_patient_name(),
      "\nPatient's test ids:",patient1.get_list_of_lab_test_ids(), 
      "\nTotal lab test charge:",patient1.get_lab_test_charge())