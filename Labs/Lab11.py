def count_vowels(s):
    
    vowel_count = 0
    forbidden_few = '1234567890!@#$%^&*()-_+='
    
    try:
        if type(s) != str:
            raise TypeError
        if len(s) == 0:
            raise ValueError
        for x in forbidden_few:
            if x in s:
                raise ValueError
    
        
        
    except TypeError:
        return 'Input should be a string'
    
    except ValueError:
        if len(s) == 0:
            return 'Input string cannot be empty'
        else:
            return 'Input string should contain only alphabetic characters'
        
        
        
    for x in s:
        if x in 'aeiouAEIOU':
            vowel_count +=1
            
    return f'The sentence contains {vowel_count} vowels'

