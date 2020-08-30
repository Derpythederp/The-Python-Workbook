#!~/anaconda3/bin/python

rating = float(input("How well are your ratings? \n> "))

if rating < 0:
    performance = "...well I have no words"
elif rating == 0.4:
    performance = "unacceptable"
elif rating == 0.6: 
    performance = "acceptable"
elif 0.6 < rating <= 1.0:
    performance = "meritorious"
elif rating > 1.0:
    performance = "stellar, absolutely stunning. Everyone, come look at the bigshot who thinks he can be better than the limit!"
else:
    print("Go get your actual rating value. This isn't valid.")
    quit()

stoinks = 2400.00 * rating
print(f"Your performance was {performance}.\nYour pay raise is {stoinks:.2f}")