##write code here
print("Hello, World!")
print("This is a test file.")
print("Testing version control integration.")
print("Final line of the test file.")
print("End of the test file.")
#####
age = 30
print("Age is:", age)
print("This line is added in the new branch.")
print("This line is added in the main branch.")
print("This line is added in both branches.")
ht = 143
wt = 60
bmi = wt / (ht/100) ** 2
print("BMI is:", bmi)
print("This line is added in both branches.")
# Example: Print numbers from 1 to 5
for i in range(1, 6):
    print("Number:", i)
# --- IGNORE ---    
## branch:
# main
##fetch > pull
#new branch: testgit

#branch: test
#create changes > git add . > git commit -m "message" > git push -u origin testgit
#merge > pull request > merge pull request > confirm merge > delete branch