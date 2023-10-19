"""
write a function called linear_ search_product that takes the list of product and a target product
name as input. the function should perform a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found, or an empty list if the product is not
found.
"""


deflinearsearchproduct(productlist, targetproduct):
   indices = []

  for index,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices

 # example usage:
products =["shoes , "boot" , "loafer" , "shoes" , sandal]