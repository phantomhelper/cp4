"""
A function that calculates the net price value based on the passed parameters gross price value and tax rate
"""


def calculate_net_price(gross_price, tax_rate):
    net_price = gross_price / (1 + tax_rate)
    return net_price
