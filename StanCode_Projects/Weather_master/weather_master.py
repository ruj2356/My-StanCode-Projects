"""
File: weather_master.py
Name: Andy Chi`
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
    """
	By constantly entering temperatures, this program will find out the
	highest, lowest, and average temperature. It will also find out how many
	cold days their are (which is any temperature lower than 16 degrees).
	"""

    print("stanCode\'Weather Master 4.0'!")
    t = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
    c = 0
    if t == EXIT:
        print("No temperatures were entered.")
    else:
        if t < 16:
            c += 1
        maximum = t
        minimum = t
        b = 1
        a = t
        while True:
            t = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
            if t == EXIT:
                break
            if t < 16:
                c += 1
            b += 1
            if maximum < t:
                maximum = t
            if minimum > t:
                minimum = t
            if t != EXIT:
                a += t
        print("Highest temperature = " + str(maximum))
        print("Lowest temperature = " + str(minimum))
        print("Average " + str(my_average(a, b)))
        print(str(c) + "cold day(s)")


def my_average(d, e):
    """
	d = Sum of all temperatures entered
	e = How many temperatures entered
	"""
    ans = (d / e)
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
    main()
