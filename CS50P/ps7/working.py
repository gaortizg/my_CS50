import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        # Retrieve info from string 's'. Notice I had to use '?:'
        # in the inner groups so they were not included in 'matches'
        # as separate elements
        matches = re.search(r"^([0-9]?[0-9](?:\:[0-9][0-9])?) (AM|PM) to ([0-9]?[0-9](?:\:[0-9][0-9])?) (AM|PM)$", s)
    
        # Retrieve info from RE search
        time1 = matches.group(1)
        mer1 = matches.group(2)
        time2 = matches.group(3)
        mer2 = matches.group(4)

    # If time is not in valid format, then raise ValueError
    except AttributeError:
        raise ValueError()
    
    # If everything Ok!
    else:
        # Split hours and minutes (if any)
        time1 = time1.split(":")
        time2 = time2.split(":")

        # Convert str to int
        time1 = [int(i) for i in time1]
        time2 = [int(i) for i in time2]

        # Compute length of the lists above
        len1 = len(time1)
        len2 = len(time2)

        # Check number of hours is valid
        if time1[0] > 12:
            raise ValueError()
        elif time2[0] > 12:
            raise ValueError()
        
        # Check number of minutes is valid (if given)
        if len1 == 2:
            if time1[1] > 59:
                raise ValueError()
        
        if len2 == 2:
            if time2[1] > 59:
                raise ValueError()

        # Format first time
        if mer1 == "AM":
            if len1 == 1:
                if time1[0] == 12:
                    time1_str = f"{(time1[0] - 12):02}:00"
                else:
                    time1_str = f"{time1[0]:02}:00"
            else:
                if time1[0] == 12:
                    time1_str = f"{(time1[0] - 12):02}:{time1[1]:02}"
                else:
                    time1_str = f"{time1[0]:02}:{time1[1]:02}"
        if mer1 == "PM":
            if len1 == 1:
                time1_str = f"{(time1[0] + 12):02}:00"
            else:
                time1_str = f"{(time1[0] + 12):02}:{time1[1]:02}"
        
        # Format second time
        if mer2 == "AM":
            if len2 == 1:
                if time2[0] == 12:
                    time2_str = f"{(time2[0] - 12):02}:00"
                else:
                    time2_str = f"{time2[0]:02}:00"
            else:
                if time2[0] == 12:
                    time2_str = f"{(time2[0] - 12):02}:{time2[1]:02}"
                else:
                    time2_str = f"{time2[0]:02}:{time2[1]:02}"
        if mer2 == "PM":
            if len2 == 1:
                time2_str = f"{(time2[0] + 12):02}:00"
            else:
                time2_str = f"{(time2[0] + 12):02}:{time2[1]:02}"
        
        return f"{time1_str} to {time2_str}"


# Run 'main' function
if __name__ == "__main__":
    main()