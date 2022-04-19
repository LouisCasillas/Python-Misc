
def does_string_have_unique_characters(string_to_check):
   
    character_hash = {}

    for character in string_to_check:
        try:
            character_hash[ character ] += 1

            print( "No" )

            return
        except:
            character_hash[ character ] = 1

    print( "Yes" )

does_string_have_unique_characters("zebra")
