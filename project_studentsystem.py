class student:
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m

    def __str__ (self):
         return f"RN:{self.rn},NAME={self.name},MARKS:{self.marks}"

s1=student(1,"abcd",10.0)
s2=student(2,"defg",20.0)
s3=student(3,"ghij",30.0)

students_list=[s1,s2,s3]

while True:
    ch = int(input("\n\nEnter choice:\n\
                   1.Add student\n\
                   2.show all list\n\
                   3update student\n\
                   4.delete student\n"))
    match ch:
         case 1:
             print("Add student")
             r = int(input("Enter Roll No:"))
             n = input("Enter Name:")
             m = float(input("Enter marks:"))
             s5 = student(r,n,m)
             student_list.append(s5)
             print("Student added succesfully!")
         case 2:
             print("show all students")
             for stu in students_list:
                 print(stu)
         case 3:
             print("update student")
         case 4:
             print("delete student")
             r=int(input("Enter Roll no to delete:"))
             found = False

             for stu in students_list:
                 if stu.rn == r:
                    found = True
                    student_to_be_removed = stu
                    break

             if found:
                 students_list.remove(students_to_be_removed)
                 print(student_to_be_removed,"Removed!")
             else:
                 print("NO such not found!")

         case 5:
              print("Exiting..")
              break
         case _ :
              print("Invalid choice..")
print("program ends")              
              
                       
        
