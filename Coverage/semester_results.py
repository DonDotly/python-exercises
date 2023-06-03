#It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes. 
#If the average score is 7 and above print "Good job!",
#if the average score is between 6 and 4 print "You need to work harder!",
#if the average score is below 4 print "Failed, you really need to work harder!"
 
# Solution 
Geometry = float(input("Enter Score in Geometry : "))
Algebra = float(input("Enter Score in Algebra : "))
Physics = float(input("Enter Score in Physics : "))
print ("Geometry: ", Geometry,"\n Algebra: ", Algebra, "\n Physics: " , Physics)
total_score = (Geometry + Algebra + Physics)
average_score = (total_score / 30)*100
if average_score >= 70:
    print ("Good Job!")
elif (average_score >=40 and average_score <=60):
     print("You Need to work hard!")
else:
     print("Failed, You really need to work harder!")