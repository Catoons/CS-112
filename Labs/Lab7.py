def word_frequency(text_dict):
    
    answer = {}
    
    for key, value in text_dict.items():
         if value in answer:
             answer[value].append(key)
         else:
             answer[value] = [key]
             
    for key in answer:
        answer[key].sort()
    
    return answer