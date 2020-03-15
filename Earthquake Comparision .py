status = True
def get_magnitude(number) :
    m = float(input(f"Please enter the magnitude for earthquake {number}: "))
    while m < 0 :
        m = float(input(f"Please enter the magnitude for earthquake {number}: "))
    return m
        
def compare_magnitudes(magnitude1, magnitude2):
    f = (10)**(1.5*(float(magnitude1-magnitude2)))
    
    return f

def get_run_again():
    ra = int(input("Try again? Type 1 for yes: "))
    if ra == 1:
        return True
    else :
        print("Bye !")
        return False
        
if __name__ == "__main__" :
    while status == True :
        m1 = get_magnitude(1)
        m2 = get_magnitude(2)
        f = compare_magnitudes(m1, m2)
        print()
        if m1 > m2 :
            print(f"An earthquake of magnitude {m1} is {f:.1f} times more powerful than an earthquake of magnitude {m2}.")
        elif m2 > m1 :
            if m2 > m1 :
                f = 1/f
            print(f"An earthquake of magnitude {m2} is {f:.1f} times more powerful than an earthquake of magnitude {m1}.")
        status = get_run_again()
        print()

    

    


