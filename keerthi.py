fruits=["Apple","Banana","Orange","Mango"]
print(fruits)

numbers=[10,20,30]
numbers.append(40)
numbers.insert(1,15)
numbers.remove(20)
print(numbers)

numbers=[10,20,30,40,50,60]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])

colors=("Red","Green","Blue")
print(colors)

numbers=(10,20,30,40)
print(numbers.count(20))
print(numbers.index(30))

numbers=(10,20,30,40,50)
print(numbers[1:4])
print(numbers[::-1])

A={10,20,30}
A.add(40)
A.remove(20)
print(A)

number=15
if number%2==0:
    print("Even")
else:
    print("Odd")

    student={"name":"Rahul","marks":88}
    if student["marks"]>=50:
        print(student["name"],"passed")
    else:
        print(student["name"],"failed")

    marks=82
    if marks>=90:
        print("Grade A+")
    elif marks>=75:
            print("grade A")
    elif marks>=60:
            print("grade B")
    else:
            print("grade C")

    data=(5,10,15,20,25,30)
    print(data[2:1])
    print(data[:4])
    print(data[::-1])

    python={"variables","Loops","functions"}
    java={"loops","oops","classes"}
    print("common:",python.intersection(java))
    print("All topics:",python.union(java))

    age=20
    if age>=18:
          print("Eligible to vote")

    students=[
          {"name":"Anu","marks":90},
          {"name":"Raja","marks":45},
          {"name":"Kavi","marks":70}
    ]
    for student in students:
          if student["marks"]>=50:
                print(student["name"],"pass")
          else:
                print(student["name"],"fail")

    class animal:
            def eat(self):
                print("my dog eats well")
    obj=animal()
    obj.eat()

    class animal:
          def __init__(self):
             print("i am the constructor")
    obj=animal()

    class student:
          def display(self):
                print("Name:",self.name)
                print("Roll no:",self.rollno)
                print("Department:",self.department)
    s1=student()
    s1.name="Raja"
    s1.rollno=101
    s1.department="BCA"
    s1.display() 

    class Employee:
          def annual_salary(self):
                print("Employee Name:",self.name)
                print("Annual Salary:",self.salary *12)
    e1=Employee()
    e1.name="Arun"
    e1.salary=25000
    e1.annual_salary()    

    class Rectangle:
          def area(self):
            print("Area=",self.length*self.width)
          def perimeter(self):
                print("perimeter=",2*(self.length+self.width))
    r=Rectangle()
    r.length=10
    r.width=5
    r.area() 
    r.perimeter()  

    class Circle:
          def area(self):
                print("Area=",3.14*self.radius*self.radius)
          def circumference(self):
                print("Circumference=",2*3.14*self.radius)
    c=Circle()
    c.radius=7
    c.area()
    c.circumference() 

    class car:
          def display(self):
                print("Brand:",self.brand)
                print("Model:",self.model)
                print("Price:",self.price)
    c=car()
    c.brand="Toyoto"
    c.model="Innova"
    c.price=1800000
    c.display()

    class product:
          def bill(self):
                total=self.price*self.quantity
                print("Total bill:",total)
    p=product()
    p.price=150
    p.quantity=8
    p.bill() 

    class movie:
          def total_amount(self):
                total=self.ticket_price*self.tickets
                print("Total Amount:",total)
    m=movie()
    m.ticket_price=200
    m.tickets=5
    m.total_amount()

    class Person :
          def person_details(self):
                print("Name:",self.name)
                print("Age:",self.age)
    class student(Person):
          def student_details(self):
                print("course:",self.course)
    s=student()
    s.name="raja"
    s.age=20
    s.course="python"
    s.person_details()
    s.student_details()

     

               
                            
                
                     

    
                                        
                 

                
          
         











