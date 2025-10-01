import json

def load_data(file_path):
    """
    Pull JSON data from file and return a dictionary
    """

    try: 
        with open(file_path, 'r') as file:     
            data = json.load(file) 
            return data
        
    except FileNotFoundError: 
        print(f"Error: The file '{file_path}' was not found.") 

    except json.JSONDecodeError as e:   
        print(f"Error: The file '{file_path}' isn’t valid JSON.") 
        print(f"JSONDecodeError: {e}")
        print(f"Error occurred at line: {e.lineno}, column: {e.colno}")
        print(f"Position in string: {e.pos}")
        
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")

def get_deck(file_path, troops, spells):
    """                                                                                                                                       
    Pull card data from dictionary

    file_path - path to the folder holding the JSON data
    troops - troop name list
    spells - spell name list
    
    """

    try:

        # This will be our eight card deck
        deck = []

        # Load the troop JSON data into a dictionary
        troop_data = load_data(file_path + 'troops.json')

        # Traverse the troop deck
        for card in troop_data['troops']:

            # Keep only the troop cards we want
            if card['sc_key'] in troops:

                # Add to deck
                deck.append(card)

        # Repeat for spells
        spell_data = load_data(file_path + 'spells.json')

        # Do the same for spells
        for card in spell_data['spells']:

            # Keep only the spell cards we want   
            if card['sc_key'] in spells:

                # Add to deck                                                                                                                 
                deck.append(card)

        return deck
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

