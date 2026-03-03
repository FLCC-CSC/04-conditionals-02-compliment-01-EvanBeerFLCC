# FILE NAME - compliment_01.py

# NAME: Evan Beer
# DATE: 3/3/26
# BRIEF DESCRIPTION: Asks the user if they want a compliment and either givers them one or not but either way it thanks the user for playing.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YOUR CODE BELOW THIS LINE ##########

def main():
    compliment_giver()

def compliment_giver():
    Choice = input('Would you like a compliment? ')
    
    if Choice == 'yes':
        print("You have wonderful eyes.")
    print('Thank you for playing.')

main()








########### END YOUR CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? y
Thank you for playing.
'''


'''
Would you like a compliment? Yes
Thank you for playing.
'''


'''
Would you like a compliment? no
Thank you for playing.
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. On a scale of 1 to 10 (where 10 is the hardest), how would you rate this lab?

6


2. What was the hardest part of this lab?

Trying to figure out how to get the second print statement to work even if the user doesnt want a compliment.






'''
