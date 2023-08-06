#direct_percent
def percent(n,npercent):
    percentage = npercent/100*n
    return percentage

def min_percent(n,npercent):
    percentage = npercent/100*n
    percentage = n-percentage
    return percentage

def plus_percent(n,npercent):
    percentage = npercent/100*n
    percentage = n+percentage
    return percentage

def x_percent(n,npercent):
    percentage = npercent/100*n
    percentage = n*percentage
    return percentage

def div_percent(n,npercent):
    percentage = npercent/100*n
    percentage = n/percentage
    return percentage

#inverted_percent
def inv_percent(vp,percent):
    percentage = (100*vp)/percent
    return percentage

def min_inv_percent(vp,percent):
    percentage = (100*vp)/percent
    percentage = percentage-vp
    return percentage

def plus_inv_percent(vp,percent):
    percentage = (100*vp)/percent
    percentage = percentage+vp
    return percentage

def x_inv_percent(vp,percent):
    percentage = (100*vp)/percent
    percentage = percentage*vp
    return percentage

def div_inv_percent(vp,percent):
    percentage = (100*vp)/percent
    percentage = percentage/vp
    return percentage

#percentage_between_two_numbers
def compared_percent(n,n1):
    percentage = (100*n)/n1
    return percentage