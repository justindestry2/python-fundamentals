def parse_numbers(nums):
    return [int(i) for i in nums.split(",")]

def double(nums):
    return [i*2 for i in nums]


def main():
    nums = "1, 2, 3, 4"
    raw = parse_numbers(nums)
    times_two = double(raw)
    print(times_two)


if __name__ == '__main__':
    main()