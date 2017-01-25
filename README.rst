PosNum
===============================
Computation with arbitrary large positional number systems in Python

This is probably one of my most used homework-type problem, ever. Instead of reinventing the wheel every single time, I've decided to just standardize the reinvention here! 

There's nothing new. By feeding the algorithm one's alphabet and delimiter (if any), one would could change base of any number up to the total number of the distinct element of the alphabet. E.g. If the provided alphabet is "0123456789", then the maximum base that can be represented is 10. If it's "abcdefghijklmnopqrstuvwxyz0123456789", then the maximum base is 36. 

By specifying a delimiter, it's also possible to feed it words of the dictionary which enables one to represent arbitrary large bases. E.g. if the dictionary size is 32000 and the delimiter is "," then the maximum possible base that can be represented is 32000. In this base "apple,orange" would be a valid number, provided that "apple" and "orange" were elements of said dictionary.
