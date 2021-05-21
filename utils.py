def block_verification(verificator_digit, diff_check_digit):
    return (verificator_digit != 0 and diff_check_digit == verificator_digit) or (
        verificator_digit == 0 and diff_check_digit == 10
    )


def cbu_checked(value):

    multiplier_1 = [7, 1, 3, 9, 7, 1, 3]

    accumulator_check_1 = 0
    fragment_1 = value[:7]
    verificator_digit_1 = int(value[7])

    for index, item in enumerate(multiplier_1):
        accumulator_check_1 += int(fragment_1[index]) * item

    diff_check_1 = 10 - int(str(accumulator_check_1)[-1])

    multiplier_2 = [3, 9, 7, 1, 3, 9, 7, 1, 3, 9, 7, 1, 3]

    accumulator_check_2 = 0
    fragment_2 = value[8:-1]
    verificator_digit_2 = int(value[-1])

    for index, item in enumerate(multiplier_2):
        accumulator_check_2 += int(fragment_2[index]) * item

    diff_check_2 = 10 - int(str(accumulator_check_2)[-1])

    if block_verification(verificator_digit_1, diff_check_1) and block_verification(
        verificator_digit_2, diff_check_2
    ):
        return True

    return False
