letter = "Hey my name is {} and I am from {}"
country ="India"
name ="Sanath"

print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")

print(f"Hey my name is {{name}} and I am from {{country}}")    #To print the text as it is


# txt ="For Only {price:.2f} Rupees!"
# print(txt.format(price=49.0999999))

# price=49.0999999
# txt =f"For Only {price:.2f} Rupees!"
# print(txt)