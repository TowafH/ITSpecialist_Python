# When calling calculate_total, it isn't necessary to 
# specify a tax rate argument because
# there is a default value
def calculate_total(amount,license,tax=.08):
    total = (amount + license) * (1 + tax)
    return total
  
    
subtotal1 = calculate_total(19000,1000,.1) #Output: 22000
subtotal2 = calculate_total(19000,1000) # Output: 21600

print("The totals due are", subtotal1, "and", subtotal2)