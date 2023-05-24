# pass_gen
Generates a random password using a combination of capital letters, special characters, and alphanumeric characters. 

# Documentation

It begins by importing the random and string modules, which provide functions for generating random values and manipulating strings, respectively.

The generate_password  function generates a random password based on certain criteria.

It starts by selecting one capital letter from the set of uppercase ASCII letters using the random.choice function.

Next, it selects two special characters from the set of punctuation characters using the random.sample function. The string.punctuation constant contains all the punctuation characters.

It then creates a string called alphanumeric by concatenating the sets of ASCII letters and digits using string.ascii_letters and string.digits.

Using a loop to select five random alphanumeric characters from the alphanumeric string to get remaining characters to form 8 character password and joins them together into a string.

The password is constructed by concatenating the capital letter, the two special characters, and the rem_chars string.

To ensure randomness, the code converts the password string into a list of characters using the list function. It then shuffles the list using random.shuffle to rearrange the characters randomly.

Finally, the shuffled list is joined back into a string, and the resulting password is returned.


