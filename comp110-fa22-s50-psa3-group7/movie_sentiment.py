"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Sophia Zaboukos - szaboukos@sandiego.edu
2) Maggie Cope - mcope@sandiego.edu
"""

def average_review(word, review_filename):
    """
    Loops through all the reviews in the movie review file and calculates/returns the average score of
    the reviews that contain the given word. 

    Parameters:
    word (type: string): The word to look for in the reviews.
    review_filename(type: string): The name of the file containing movie review

    Returns:
    (type: float) An average score of the review
    """

    review_file = open(review_filename, 'r')

    total = 0
    num_reviews = 0


    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_word = word.lower()
        lower_line = line.lower()  
        vals = lower_line.split()

        if lower_word in vals:
            total = total + int(vals[0])
            num_reviews = num_reviews + 1
                 
    review_file.close()
    if num_reviews == 0 :
        return 2.0
    average = total / num_reviews
    return average

    


def estimate_review_score(movie_review, review_filename):
    """
    Returns the estimated review score for that review

    Parameters: movie_review(type: String): contains a movie review
    review_filename(type: String): contains the name of a file containing movie reviews

    Returns: (type: Int): estimated review score for that review
    """
    punctuation_mark = [".",",","!","-"]

    review = ""

    for ch in movie_review :
        if ch not in punctuation_mark:
            review = review + ch

    vals = review.split()
    sum = 0

    for word in vals :
        average = average_review(word, review_filename)
        sum = sum + average
    
    score_estimate = sum/len(vals)
    return score_estimate
    
    



def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    user_review = input("Enter a movie review: ")
    file_review = input("Enter the name of the file containing reviews: ")

    estimate = estimate_review_score(user_review, file_review)
    rounded_estimate = round(estimate)

    sentiment_word = ["(negative)","(somewhat negative)","(neutral)", "(somewhat positive)","(positive)"]

    if rounded_estimate == 0:
        print("Estimated score:", estimate, sentiment_word[0])
    elif rounded_estimate == 1:
        print("Estimated score:", estimate, sentiment_word[1])
    elif rounded_estimate == 2:
        print("Estimated score:", estimate, sentiment_word[2])
    elif rounded_estimate == 3:
        print("Estimated score:", estimate, sentiment_word[3])
    elif rounded_estimate == 4:
        print("Estimated score:", estimate, sentiment_word[4])


# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
