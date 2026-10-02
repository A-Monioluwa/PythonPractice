#print ("Hello... How are you doing")
#print (23)
##x=y=z=5
#print (x)
#x,y,z=5
#print (x)
#x,y,z=1,2,3
#print(y)
x, y, z = 1, 2, 3
#print (x)
Firstname = "Monioluwa"
last_Name = "Adeyemo"
age = 12
#print("Welcome to class" + " " +"Last_Name" + " " + "Firstname")
#print("My name is"+last_Name+" "+Firstname)
#print("i am " + str(age) + " years old")
#print("Welcome to class",Firstname )
#Firstname=input ("Firstname:  ")
#print (f"Welcome to class,(Firstname)")
#students = ["Monioluwa", "Adeyemo", "Adebayo", "Oluwaseun"] 
#students = ("Monioluwa", "Adeyemo", "Adebayo", "Oluwaseun")
#print (type(students))


#Logical Operators
#number=int(input("Enter a number: "))
#if number%2==0:
    #print("The number is even")
#else:
    #print("The number is odd")
#email validation
#email = input("Enter your email: ")
#if "@" in email and "." in email:
    #print("Email is valid")
#else:
   # print("Email is invalid")


#bitwise operators
a = 10
b = 4
#print(bin(a))
#print(bin(b))
#print(bin(a & b))


#index
name = "Monioluwa"
#print(name[-9])

exp= ("Jesus is the way and the truth and the life")
#print(exp[4:10])
#print(exp[5:])
#print(exp.upper())
#print(exp.capitalize())
#print(exp.title())
#print(exp.replace("Jesus", "God"))
#print(exp.split())


#Simple Grading System
#ca_score = int(input("Welcome to the SQI Grading System: Please enter your CA score: "))
#exam_score = int(input("Please enter your Exam score: "))
#total_score = ca_score + exam_score
#if total_score >= 70:
    #print("You have passed! You're A superstar!")
#elif total_score <= 69 and total_score >= 60:
    #print("You are a \"B\" Boss student.")
#elif total_score <= 59 and total_score >= 50:
    #print("You are a \"C\" cool student.")
#elif total_score <= 49 and total_score >= 45:
    #print("You are a \"D\" dare to dream student.")
#elif total_score <= 44 and total_score >= 40:
    #print("You are an \"E\" effortless student.")
#else: 
    #print("You have failed! You need to work harder.")

#Simple CBT System
#exp= int(input("Welcome to the SQI Trivial Friday, press 1 to start the quiz: "))
#score = [0, 0, 0]

#if exp == 1:
    #Question 1
    #print("Question 1: What is the capital of Nigeria?")
    #answer1 = input("Your answer: ")
    #if answer1.lower() == "abuja":
        #print("Correct!") 
        #score[0] += 2
    #else:
        #print("Incorrect. The correct answer is Abuja.")
        #Question 2
    #print("Question 2: What is 2 + 2?")
   # answer2 = input("Your answer: ")
    #if answer2 == "4":
            #print("Correct!") 
            #score[1] += 2
    #else:
        # print("Incorrect. The correct answer is 4.")
         #Question 3
    #print("Question 3: What is the largest planet in our solar system?")
    #answer3 = input("Your answer: ")
    #if answer3.lower() == "jupiter":
           # print("Correct!") 
            #score[2] += 2
    #else:
            #print("Incorrect. The correct answer is Jupiter.")

#if sum(score) >= 4:
   # print("Congratulations! You passed the quiz with a score of", sum(score))   
#else:
    #print("You failed the quiz with a score of", sum(score))

#SimpleToDoApp
while True:
    print("""\nWelcome to the SQI To-Do App! Please select an option below:
    1. Add a task
    2. Edit a task
    3. View tasks
    4. Delete a task
    5. Clear all tasks
    6. Exit the app
    """)
    
    
    Choice = input("Enter your choice (1-5): ")
    if Choice == "1":
        task = input("Enter the task you want to add: ")
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task added successfully!")
    elif Choice == "2":
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print("Here are your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")
        task_number = int(input("Enter the number of the task you want to edit: "))
        new_task = input("Enter the new task: ")
        tasks[task_number - 1] = new_task + "\n"
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task edited successfully!")
    elif Choice == "3":
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print("Here are your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")
    elif Choice == "4":
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        print("Here are your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")
        task_number = int(input("Enter the number of the task you want to delete: "))
        del tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully!")
    elif Choice == "5":  
        with open("tasks.txt", "w") as file:
            file.write("")
        print("All tasks cleared successfully!")
    elif Choice == "6":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. please enter a valid option.")
    
