def solution(num_list):
    sum_of_elements = sum(num_list)
    product_of_elements = 1
    for num in num_list:
        product_of_elements *= num
    
    if product_of_elements < sum_of_elements ** 2:
        return 1
    else:
        return 0