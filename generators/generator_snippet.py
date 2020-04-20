
def square_numbers_with_generator(nums_list: list):
    for x in nums_list:
        yield x*x


if __name__ == '__main__':
    gn = square_numbers_with_generator([1, 2, 3])
    for i in gn:
        print(i)
