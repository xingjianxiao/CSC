MIN_LENGTH = 1
MAX_LENGTH = 140


def is_valid_tweet(tweet):
    """ (str) -> bool

    Return True if and only if tweet is no less than 1 and no more 
    than 140 characters long.

    >>> is_valid_tweet('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of knowledge. - Grace Hopper')
    True
    >>> is_valid_tweet('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand them clearly. - Donald Knuth')
    False
    """

    # Your code here


def contains_hash_symbol(tweet):
    """ (str) -> bool

    precondition: tweet is no less than 1 and no more than 140 
    characters long.

    Return True if and only if tweet contains hash symbol.
    
    >>> contains_hash_symbol('#I am good')
    True
    >>> contains_hash_symbol('I am awsome')
    False
    """
    
    # Your code here


def is_mentioned(tweet, username):
    """ (str, str) -> bool
    
    precondition:tweet is no less than 1 and no more than 140 
    characters long and username must be a valid username

    Return True if and only if the tweet mentions that username preceded by @.

    >>> is_mentioned ('@Vincent Xiao，hello', 'Vincent Xiao')
    True
    >>> is_mentioned ('@Vincent Xiao，hello', 'Vin')
    True
    >>> is_mentioned ('Yo, @Vincent Xiao，hello', 'Vin')
    True
    >>> is_mentioned ('hello Vincent Xiao@','Vincent Xiao')
    False
    >>> is_mentioned ('hello Vincent Xiao@','Tom')
    False
    """

    # Your code here

    
def report_shortest (Tweet1, Tweet2):
    """(str, str) -> str
    
    precondition: tweet is no less than 1 and no more than 140 
    characters long.
    
    Return 'Tweet 1' if the first tweet is shorter than the second, 'Tweet 2'
    if the second tweet is shorter than the first, and 'Same length' if the 
    tweets have the same length.
    
    >>> report_shortest('hi', 'hello')
    hi
    >>> report_shortest('your', 'you')
    you
    >>> report_shortest('me', 'me')
    same length
    """

    # Your code here

        
def is_reply (tweet):
    """(str, str) -> bool
    
    precondition: tweet is no less than 1 and no more than 140 
    characters long.
    
    Return True if and only if this tweet is a reply.
    
    >>> is_reply ('@Vincent Xiao I am here')
    True
    >>> is_reply ('I am here @Vincent Xiao')
    False
    >>> is_reply ('I am here Vincent Xiao')
    False
    """

    # Your code here


        
def format_reply_to(username, tweet):
    """(str, str) -> str
    
    precondition: tweet is no less than 1 and no more than 140 
    characters long and username must be a valid username or 
    a valid usename preceded by @
    
    Return If the reply tweet is at most 140 characters long, return it. 
    Otherwise, return a string that indicates how many extra characters 
    there are in the invalid reply tweet.
    
    >>> format_reply_to ('Vincent Xiao', 'How are you')
    @Vincent Xiao How are you
    >>> format_reply_to ('@Vincent Xiao','How are you')
    @Vincent Xiao How are you
    >>> format_reply_to ('Vincent Xiao','The best programs are written so' \
        + ' that computing machines can perform them quickly and so that ' \
        + 'human beings can understand them clearly. - Donald Knuth')
    10 characters too long
    >>> format_reply_to ('@Vincent Xiao','The best programs are written so' \
        + ' that computing machines can perform them quickly and so that ' \
        + 'human beings can understand them clearly. - Donald Knuth')
    10 characters too long    
    """

    # Your code here


if __name__ == "__main__":
    # call the function inside the print to test your code, for example
    # print(contains_hash_symbol('#I am good'))
    # expected result: True
    print(contains_hash_symbol('#I am good'))
