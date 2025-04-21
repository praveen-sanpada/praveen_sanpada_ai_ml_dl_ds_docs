from fuzzywuzzy import process

# Function to find the best match using fuzzywuzzy
def get_best_match(query, choices):
    match = process.extractOne(query, choices)
    
    # If match score is greater than 80, return the match
    if match and match[1] > 80:
        return match[0]
    return None
