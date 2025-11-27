class StringReverser:
    def reverse_words(self, input_string: str) -> str:
        
        words = input_string.split()  
        reversed_words = words[::-1]  
        return " ".join(reversed_words) 
