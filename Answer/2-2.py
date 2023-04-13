name = "Tanaka"
location = "Kumamoto"

# 複数の引数、区切り文字の指定
print("My name is ", name, ". ", "I'm from ", location, ".", sep = "")

# f文字列
print(f"My name is {name}. I'm from {location}.")

# str.formatメソッド
print("My name is {}. I'm from {}.".format(name, location))