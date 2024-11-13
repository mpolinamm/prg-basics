def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n*0.3937

def ft_in_to_cm(ft, inches):
    ft_to_cm = ft * 30.48
    in_to_cm = inches * 2.54
    return ft_to_cm + in_to_cm
    
if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'166 cm = {cm_to_inches(166)}in')
    print(f'5 ft 5.4 in = {ft_in_to_cm(5, 5.4)}cm')
