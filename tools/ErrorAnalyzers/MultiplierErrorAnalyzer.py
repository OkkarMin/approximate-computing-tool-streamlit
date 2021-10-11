import random
import math
from common import ApproxMultipliers

## Multiplier error calculations (AE, MAE, RMSE)

# Error Calculation for AAM01 Multiplier with different V-cuts


def AAM01_VCut(N1, N2, V_val):
    AAM01_VCut_estimate_AE = 0.0
    AAM01_VCut_estimate_MAE = 0.0
    AAM01_VCut_estimate_RMSE = 0.0

    if N1 <= 8 and N2 <= 8:
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2 ** N1):
            for num2 in range(2 ** N2):
                accurate_product = ApproxMultipliers.accurate_array_multiplier(
                    num1, num2, N1, N2
                )
                AAM01_VCut_product = ApproxMultipliers.AAM01(num1, num2, N1, N2, V_val)
                AAM01_VCut_estimate_AE += AAM01_VCut_product - accurate_product
                AAM01_VCut_estimate_MAE += abs(AAM01_VCut_product - accurate_product)
                AAM01_VCut_estimate_RMSE += (AAM01_VCut_product - accurate_product) ** 2

        AAM01_VCut_estimate_AE /= 2 ** (N1 + N2)
        print()
        print("AAM01 VCut=", V_val, "average error", AAM01_VCut_estimate_AE)
        print()

        AAM01_VCut_estimate_MAE /= 2 ** (N1 + N2)
        print("AAM01 VCut=", V_val, "mean absolute error", AAM01_VCut_estimate_MAE)
        print()

        AAM01_VCut_estimate_RMSE /= 2 ** (N1 + N2)
        AAM01_VCut_estimate_RMSE = math.sqrt(AAM01_VCut_estimate_RMSE)
        print("AAM01 VCut=", V_val, "Root Mean Square Error", AAM01_VCut_estimate_RMSE)
        print()

        return (
            AAM01_VCut_estimate_AE,
            AAM01_VCut_estimate_MAE,
            AAM01_VCut_estimate_RMSE,
        )

    else:
        print(
            "\n Since atleast one of the two input is >8 bits, \n \
        Approximate Error Anaylsis is performed\n \
        using 100,000 random input combinations...\n"
        )
        num_rand_values = 100000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2 ** N1)
            num2 = random.randrange(2 ** N2)
            accurate_product = ApproxMultipliers.accurate_array_multiplier(
                num1, num2, N1, N2
            )
            AAM01_VCut_product = ApproxMultipliers.AAM01(num1, num2, N1, N2, V_val)
            AAM01_VCut_estimate_AE += AAM01_VCut_product - accurate_product
            AAM01_VCut_estimate_MAE += abs(AAM01_VCut_product - accurate_product)
            AAM01_VCut_estimate_RMSE += (AAM01_VCut_product - accurate_product) ** 2

        AAM01_VCut_estimate_AE /= num_rand_values
        print()
        print("AAM01 VCut=", V_val, "average error", AAM01_VCut_estimate_AE)
        print()

        AAM01_VCut_estimate_MAE /= num_rand_values
        print("AAM01 VCut=", V_val, "mean absolute error", AAM01_VCut_estimate_MAE)
        print()

        AAM01_VCut_estimate_RMSE /= num_rand_values
        AAM01_VCut_estimate_RMSE = math.sqrt(AAM01_VCut_estimate_RMSE)
        print("AAM01 VCut=", V_val, "Root Mean Square Error", AAM01_VCut_estimate_RMSE)
        print()

        return (
            AAM01_VCut_estimate_AE,
            AAM01_VCut_estimate_MAE,
            AAM01_VCut_estimate_RMSE,
        )


def AAM01_VCut(N1, N2, V_val):
    AAM01_VCut_estimate_AE = 0.0
    AAM01_VCut_estimate_MAE = 0.0
    AAM01_VCut_estimate_RMSE = 0.0

    if N1 <= 10 and N2 <= 10:
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2 ** N1):
            for num2 in range(2 ** N2):
                accurate_product = ApproxMultipliers.accurate_array_multiplier(
                    num1, num2, N1, N2
                )
                AAM01_VCut_product = ApproxMultipliers.AAM01(num1, num2, N1, N2, V_val)
                AAM01_VCut_estimate_AE += AAM01_VCut_product - accurate_product
                AAM01_VCut_estimate_MAE += abs(AAM01_VCut_product - accurate_product)
                AAM01_VCut_estimate_RMSE += (AAM01_VCut_product - accurate_product) ** 2

        AAM01_VCut_estimate_AE /= 2 ** (N1 + N2)
        print()
        print("AAM01 VCut=", V_val, "average error", AAM01_VCut_estimate_AE)
        print()

        AAM01_VCut_estimate_MAE /= 2 ** (N1 + N2)
        print("AAM01 VCut=", V_val, "mean absolute error", AAM01_VCut_estimate_MAE)
        print()

        AAM01_VCut_estimate_RMSE /= 2 ** (N1 + N2)
        AAM01_VCut_estimate_RMSE = math.sqrt(AAM01_VCut_estimate_RMSE)
        print("AAM01 VCut=", V_val, "Root Mean Square Error", AAM01_VCut_estimate_RMSE)
        print()

    else:
        print(
            "\n Since atleast one of the two input is >10 bits, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n"
        )
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2 ** N1)
            num2 = random.randrange(2 ** N2)
            accurate_product = ApproxMultipliers.accurate_array_multiplier(
                num1, num2, N1, N2
            )
            AAM01_VCut_product = ApproxMultipliers.AAM01(num1, num2, N1, N2, V_val)
            AAM01_VCut_estimate_AE += AAM01_VCut_product - accurate_product
            AAM01_VCut_estimate_MAE += abs(AAM01_VCut_product - accurate_product)
            AAM01_VCut_estimate_RMSE += (AAM01_VCut_product - accurate_product) ** 2

        AAM01_VCut_estimate_AE /= num_rand_values
        print()
        print("AAM01 VCut=", V_val, "average error", AAM01_VCut_estimate_AE)
        print()

        AAM01_VCut_estimate_MAE /= num_rand_values
        print("AAM01 VCut=", V_val, "mean absolute error", AAM01_VCut_estimate_MAE)
        print()

        AAM01_VCut_estimate_RMSE /= num_rand_values
        AAM01_VCut_estimate_RMSE = math.sqrt(AAM01_VCut_estimate_RMSE)
        print("AAM01 VCut=", V_val, "Root Mean Square Error", AAM01_VCut_estimate_RMSE)
        print()
