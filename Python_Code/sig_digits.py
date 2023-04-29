def sig_digits(x):
  try:
    x0 = float(x)
  except Exception:
    return False, "sorry, invalid input /{0/}"

  if x0 == 0: return False, 0
  elif x0 < 0:  return False, "sorry, invalid input /{1/}"

  x1 = str(float(x) / 1e9)


  first_digit_check = float(x1.split('.')[0])
  sig_digit_check = x1.split('e')[1]

  if first_digit_check >4: return True, first_digit_check, abs(int(sig_digit_check))-10
  elif first_digit_check < 5: return True, first_digit_check, abs(int(sig_digit_check))-9
  else: False, "sorry, invalid input /{2/}"

  # return first_digit_check, abs(int(sig_digit_check))-10


# print(sig_digits(0.2520979e-7))
def main():
  while True:
    x = input("enter of instance (0.321423e-3), (-1 to cancel): ")
    if x == "-1": break
    bol, first_digit = sig_digits(x)[0], sig_digits(x)[1]
    
    if bol: 
      sig_digit = sig_digits(x)[2]
      print("the number of significant digits of given number is: ", sig_digit, "\n")
    else: print(sig_digits(x))

# main()






# OUT OF ORDER, PLEASE IGNORE

# while False:  # in order to have a continous run

#   RE = float(input("enter, (-1 to cancel): "))  # Given Relative Error
#   if RE == -1:  # if user has no more values to enter
#     break

#   try:  # if the number is small enough to have (e) in it
#     SD = abs(
#       int(str(RE).split('e')[1])
#     ) - 2  # we first turn the RE into str then try to take                                                #the exponent of "e"
#     num = int(str(RE)[0])  # trying to check if the first nonzero digit is                                                 #greater than 5
#     if num > 4:
#       SD += 1  # python will turn (0.66e-2) into (6.6e-3) so therefor we have add one
#     else:
#       SD = abs(int(str(RE).split('e')[1]))
#     print("SD: ", SD)

#   # if RE is large enough to not have (e) init then above                                        #code will end in error so therefore for that we have the code below
#   except Exception as e:
#     nu = str(RE).split('.')[1]
#     sig = 0
#     for i in range(len(nu)):  # simply the code will count the occurrence of zeros
#       if int(str(RE).split('.')[0]) !=0 and 'e' not in str(RE):
#         break
#       elif int(nu[i]) == 0:  # 0.00432 => SD=2
#         sig += 1
#       elif int(nu[i]) >= 5:
#         # sig += 1
#         break
#       elif int(nu[i]) != 0 and int(nu[i]) < 5:
#         sig += 1
#         break

#     print("SD; ", sig)
