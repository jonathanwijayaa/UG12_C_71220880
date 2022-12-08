k_a = (input("Masukan Kata atau angka :"))

def reverse(k_a):
    str = ""
    for i in k_a:
        str = i + str
    return str
print(reverse(k_a))
