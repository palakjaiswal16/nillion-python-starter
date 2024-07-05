from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    A = SecretInteger(Input(name="A", party=party1))
    B = PublicInteger(Input(name="B", party=party1))
    C = SecretInteger(Input(name="C", party=party1))
    D = PublicInteger(Input(name="D", party=party1))
    E = SecretInteger(Input(name="E", party=party2))
    F = PublicInteger(Input(name="F", party=party2))
    threshold = PublicInteger(Input(name="Threshold", party=party2))

    TMP0 = A + B
    TMP1 = C * D
    TMP2 = B + D
    TMP3 = B * D
    TMP4 = E + F
    TMP5 = E * F

    sum_all = TMP0 + TMP1 + TMP2 + TMP3 + TMP4 + TMP5

    is_above_threshold = sum_all > threshold

    result = Select(is_above_threshold, "Above Threshold", "Below Threshold")

    return [Output(result, "Result", party1)]
