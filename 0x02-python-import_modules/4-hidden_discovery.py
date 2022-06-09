#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):#use dir to search for the names in hidden_4
        if (i[:2] != '__'):#check if i starts with __
            print(i)
