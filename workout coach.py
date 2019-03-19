def workout_coach(lift_name,weight):
    print("Time to",lift_name,weight,"pounds! You got this!")

def main():
    weight = 10
    answer = input("You ready to get started? Enter yes for your workout! ")

    for lift_name in ("squat","bench","deadlift"):
        while answer == "yes":
            workout_coach(lift_name,weight)
            answer = input("Keep doing the",lift_name+"? Enter yes for next set! ")            
            weight = weight+10
        else:
            break
        while answer == "yes" and weight <= 200:
            workout_coach(lift_name,weight)
            answer = input("Keep doing the",lift_name+"? Enter yes for next set! ")           
            weight = weight+10
        else:
            break
        while answer == "yes":
            workout_coach(lift_name,weight)
            answer = input("Keep doing the",lift_name+"? Enter yes for next set! ")            
            weight = weight+10
        else:
            print("Killer reps! Now go shower off. You smell awful.")

main()
