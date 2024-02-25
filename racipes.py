
#function to take avrage of recipe list 
recipe=[]

def average_rating(recipe):
    title, ratings,url = recipe
    return sum(ratings) / len(ratings)

def recipe_list(recipe):
    filtered = [r for r in recipe if average_rating(r) > 7.0]
    for r in filtered:
        title, ratings ,url= r
        print(f"{title.center(70)}------{url.center(70)}\n\n")
        

