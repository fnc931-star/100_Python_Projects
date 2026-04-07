

def BandNameGenerator():
    
    print("**************** WELCOME TO BAND-NAME-GENERATOR ****************")
    

    # Get the City name
    city_name = input("What's the name of the city you grew up in?\n")
    
    # Get your Favourite Pet name
    pet_name = input("What's your pet name?\n")

    # Concate the City and Pet name to create a Band Name
    band_name = city_name + " " + pet_name

    # Return the result 
    return f"Your Band Name could be '{band_name}'"



# Save the Band Name into a variable for reuse into another file
result  = BandNameGenerator()

