from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    LEVEL_CHOICES = [
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Artisan', 'Artisan'),
    ]
    MEAN_GRADE = [
        ('C', 'Cplain'),
        ('C-', 'Cminus'),
        ('D+', 'Dplus'),
        ('D', 'Dplain'),
        ('D-', 'Dminus'),
    ]
    name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    kcpe_index = models.CharField(max_length=100, null=True)
    kcse_index = models.CharField(max_length=100, null = True)
    email_id = models.EmailField(max_length=255,null=True)
    phone_num = models.CharField(max_length=13,null=True)
    student_gender = models.CharField(choices = GENDER_CHOICES, max_length=1,null=True)
    student_level = models.CharField(choices = LEVEL_CHOICES, max_length=12,null=True)
    secondary_grade = models.CharField(choices = MEAN_GRADE, max_length=2,null=True)
    student_address = models.TextField(null=True)
    student_course = models.ManyToManyField('AvailableCourse')
    date_of_birth = models.DateField(null=True)
    student_image = models.ImageField(upload_to='pages/images/', null=True)

    #def __str__(self):
        #return self.first_name


class AvailableCourse(models.Model):
    nam = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    #GENDER_CHOICES = [
        #('M', 'Male'),
        #('F', 'Female'),
    #]
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    student_gender = models.CharField(max_length=100,null=True)
    student_address = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)
    idnumber = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_of_birth = models.CharField(max_length = 100,null=True)
    birth_cert_no= models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    marital_status = models.CharField(max_length=100, null=True)
    home_county = models.CharField(max_length=100, null=True)
    sub_county = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    sub_location = models.CharField(max_length=100, null=True)
    village = models.CharField(max_length=100, null=True)
    estate = models.CharField(max_length=100, null=True)
    name_of_father = models.CharField(max_length=100, null=True)
    occupation_of_father = models.CharField(max_length=100, null=True)
    father_tel = models.CharField(max_length=100, null=True)
    name_of_mother = models.CharField(max_length=100, null=True)
    occupation_of_mother = models.CharField(max_length=100, null=True)
    mother_tel = models.CharField(max_length=100, null=True)
    name_of_guardian = models.CharField(max_length=100, null=True)
    occupation_of_guardian = models.CharField(max_length=100, null=True)
    guardian_tel = models.CharField(max_length=100, null=True)
    name_of_sponsor = models.CharField(max_length=100, null=True)
    sponsor_tel = models.CharField(max_length=100, null=True)
    sponsor_address = models.CharField(max_length=100, null=True)
    kra_pin = models.CharField(max_length=100, null=True)
    huduma_num = models.CharField(max_length=100, null=True)
    orphan_status = models.CharField(max_length=100, null=True)
    sibling1_name = models.CharField(max_length=100, null=True)
    sibling1_school = models.CharField(max_length=100, null=True)
    sibling1_level = models.CharField(max_length=100, null=True)
    sibling2_name = models.CharField(max_length=100, null=True)
    sibling2_school = models.CharField(max_length=100, null=True)
    sibling2_level = models.CharField(max_length=100, null=True)
    sibling3_name = models.CharField(max_length=100, null=True)
    sibling3_school = models.CharField(max_length=100, null=True)
    sibling3_level = models.CharField(max_length=100, null=True)
    sibling4_name = models.CharField(max_length=100, null=True)
    sibling4_school = models.CharField(max_length=100, null=True)
    sibling4_level = models.CharField(max_length=100, null=True)
    sibling5_name = models.CharField(max_length=100, null=True)
    sibling5_school = models.CharField(max_length=100, null=True)
    sibling5_level = models.CharField(max_length=100, null=True)
    beneficiary_status = models.CharField(max_length=100, null=True)
    chronic_suffering_choice = models.CharField(max_length=100, null=True)
    chronic_suffering_exp = models.TextField(max_length=100, null=True)
    food_allergy = models.CharField(max_length=100, null=True)
    food_allergy_exp = models.TextField(max_length=100, null=True)
    co_curricula_1 = models.CharField(max_length=100, null=True)
    co_curricula_2 = models.CharField(max_length=100, null=True)
    staying_preference = models.CharField(max_length=100, null=True)
    course_applying = models.CharField(max_length=100, null=True)
    primary_school = models.CharField(max_length=100, null=True)
    kcpe_index = models.CharField(max_length=100, null=True)
    kcpe_year = models.CharField(max_length=100, null=True)
    secondary_school = models.CharField(max_length=100, null=True)
    kcse_index = models.CharField(max_length=100, null=True)
    kcse_year = models.CharField(max_length=100, null=True)
    previous_institution = models.CharField(max_length=100, null=True)
    previous_institution_index = models.CharField(max_length=100, null=True)
    tvet_exam_year = models.CharField(max_length=100, null=True)
    kcse_subject_1 = models.CharField(max_length=100, null=True)
    kcse_subject_1_grade = models.CharField(max_length=100, null=True)
    kcse_subject_2 = models.CharField(max_length=100, null=True)
    kcse_subject_2_grade = models.CharField(max_length=100, null=True)
    kcse_subject_3 = models.CharField(max_length=100, null=True)
    kcse_subject_3_grade = models.CharField(max_length=100, null=True)
    kcse_subject_4 = models.CharField(max_length=100, null=True)
    kcse_subject_4_grade = models.CharField(max_length=100, null=True)
    kcse_subject_5 = models.CharField(max_length=100, null=True)
    kcse_subject_5_grade = models.CharField(max_length=100, null=True)
    kcse_subject_6 = models.CharField(max_length=100, null=True)
    kcse_subject_6_grade = models.CharField(max_length=100, null=True)
    kcse_subject_7 = models.CharField(max_length=100, null=True)
    kcse_subject_7_grade = models.CharField(max_length=100, null=True)
    kcse_subject_8 = models.CharField(max_length=100, null=True)
    kcse_subject_8_grade = models.CharField(max_length=100, null=True)
    kcse_meangrade = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='pages/images/',null=True)
    resultslip = models.FileField(upload_to='pages/pdfs/',null=True)
    leaving_certificate = models.FileField(upload_to='pages/pdfs/',null=True)
    id_card = models.FileField(upload_to='pages/pdfs/',null=True)
    birth_cert = models.FileField(upload_to='pages/pdfs/',null=True)
    medical_cert = models.FileField(upload_to='pages/pdfs/',null=True)


    def __str__(self):
        return self.first_name
    
    



