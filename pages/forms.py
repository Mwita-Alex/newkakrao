from django import forms
from .models import Student, Registration 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','last_name','kcpe_index','kcse_index','email_id','phone_num',
        'student_address', 'student_gender','student_course','student_level',
        'date_of_birth','student_image','secondary_grade')
    

class KakForm(forms.ModelForm): 
    class Meta:
         model = Registration
         fields = ['first_name','middle_name','last_name','student_gender','student_address','code','town',
         'tel','idnumber','email','date_of_birth','birth_cert_no','country','marital_status',
         'home_county','sub_county','location','sub_location','village','estate','name_of_father','occupation_of_father',
         'father_tel','name_of_mother','occupation_of_mother','mother_tel','name_of_guardian','occupation_of_guardian',
         'guardian_tel','name_of_sponsor','sponsor_tel','sponsor_address','kra_pin','huduma_num','orphan_status','sibling1_name',
         'sibling1_school','sibling1_level','sibling2_name','sibling2_school','sibling2_level','sibling3_name',
         'sibling3_school','sibling3_level','sibling4_name','sibling4_school','sibling4_level','sibling5_name',
         'sibling5_school','sibling5_level','beneficiary_status','chronic_suffering_choice','chronic_suffering_exp',
         'food_allergy','food_allergy_exp','co_curricula_1','co_curricula_2','staying_preference','course_applying','primary_school',
         'kcpe_index','kcpe_year','secondary_school','kcse_index','kcse_year','previous_institution','previous_institution_index',
         'tvet_exam_year','kcse_subject_1','kcse_subject_1_grade','kcse_subject_2','kcse_subject_2_grade','kcse_subject_3','kcse_subject_3_grade',
         'kcse_subject_4','kcse_subject_4_grade','kcse_subject_5','kcse_subject_5_grade','kcse_subject_6','kcse_subject_6_grade',
         'kcse_subject_7','kcse_subject_7_grade','kcse_subject_8','kcse_subject_8_grade','kcse_meangrade','image','resultslip',
         'leaving_certificate','id_card','birth_cert','medical_cert']      
