def main():
    good_list = []
    excellent_list = []
    bad_list = []
    poor_list = []
    average_list = []

    while True:
        ans = input("Sort reviews by good, excellent, bad, poor, average: ")
        if ans == "good":
            good_reviews(good_list)
        elif ans == "excellent":
            excellent_reviews(excellent_list)
        elif ans == "bad":
            bad_reviews(bad_list)
        elif ans == "poor":
            poor_reviews(poor_list)
        elif ans == "average":
            average_reviews(average_list)
        else:
            print("Invalid input. Please try again.")

def good_reviews(good_list):
    python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
    print("Good Reviews:")
    for review in python_reviews:
        if "good" in review:
            print(review.replace("good", "GOOD"))   
            good_list.append(review)
            break


def excellent_reviews(excellent_list):
    python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
    print("Excellent Reviews:")
    for review in python_reviews:
        if "excellent" in review:
            print(review.replace("excellent", "EXCELLENT"))  
            excellent_list.append(review)
            break

def bad_reviews(bad_list):
    python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
    print("Bad Reviews:")
    for review in python_reviews:
        if "bad" in review:
            print(review.replace("bad", "BAD")) 
            bad_list.append(review)
            break

def poor_reviews(poor_list):
    python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
    print("Poor Reviews:")
    for review in python_reviews:
        if "poor" in review:
            print(review.replace("poor", "POOR"))    
            poor_list.append(review)
            break

def average_reviews(average_list):
    python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
    print("Average Reviews:")
    for review in python_reviews:
        if "average" in review:
            print(review.replace("average", "AVERAGE"))  
            average_list.append(review)
            break

main()

#Task 2
python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "This was a poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


positive_count = 0
for review in python_reviews:
    for word in positive_words:
        if word in review:
            positive_count += 1
print("Number of positive words in python reviews:", positive_count)

negative_count = 0
for review in python_reviews:
    for word in negative_words:
        if word in review:
            negative_count += 1
print("Number of negative words in python reviews:", negative_count)

#Task 3
python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "This was a poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]
short_reviews = []
for review in python_reviews:
    if len(review) > 30:
        review = review[:30] + "..."
    short_reviews.append(review)
print("Shortened Reviews:")
for review in short_reviews:
    print(review)