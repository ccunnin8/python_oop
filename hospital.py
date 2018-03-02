class Hospital(object):
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.patient_num = 0
        self.available_beds = [ num for num in range(1,capacity+1)]
        self.used_beds = []
        self.patients = []
    def admit(self,patient):
        if len(self.available_beds) != 0:
            #take first availble bed from self.available_beds
            bed = self.available_beds[0]
            #remove that bed from avail. beds
            del(self.available_beds[0])
            #add that bed to used_beds
            self.used_beds.append(bed)
            self.patient_num += 1

            #update patient
            patient.assign_id(self.patient_num)
            patient.assign_bed(bed)
            self.patients.append(patient)
            print("Patient Admitted")
        else:
            print("Hospital at capacity!")
        return self


    def discharge(self,patient):
        patients_bed = patient.bed
        patient_id = patient.id
        self.available_beds.append(patients_bed)
        self.used_beds = [bed for bed in self.used_beds if bed != patients_bed]
        self.patients = [_patient for _patient in self.patients if _patient.id != patient.id]
        print("Patient Discharged")
        return self

class Patient(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.allergies = []

    def assign_bed(self,bed):
        self.bed = bed
        return self

    def assign_id(self,_id):
        self.id = _id
        return self

    def add_allergies(self,allergy):
        self.allergies.append(allergy)
        return self
