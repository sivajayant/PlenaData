# PlenaData

WORKING:

  step1: run the file.
  step2: when it prompts, enter a string.
  step3: view your results on the console.
  
  
Methods and Complexity analysis:

  step1: to find the first non repeating character -- runs in O(N) time, where N == lenght of input string:
    - we call a method "getFirstNonRepeating" with our string as an argument.
    - this method counts the number of time each letter is found in the string and stores it in "Counts"(dictionary). -- O(N) time
    - we reiterate through counts and find the first letter which has value 1 and return that key -- O(N) time
        
        
 step2: to get the String in order of number of occurrences and order from the inputted string -- runs in O(NlogN) time:
    - we make use of a pririty queue that keeps track of the counts, index of each letter in the input string
    - we insert all the letter with their associated counts and index into the heap -- O(NlogN) time
    - we then pop each item out of the heap concatenate and return as a string -- O(NlogN) time
 
 
 time complexity of the algorithm : O(NlogN), where N == lenght of input string.
