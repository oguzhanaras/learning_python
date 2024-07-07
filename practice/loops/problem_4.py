# In each while loop, take a number from the user and add the numbers entered by the user to a variable named "total". When the user presses "q", end the loop and print "total variable" to the screen.
#
# *Tip : Start the while loop with an infinite condition and end the loop with break if the user presses q.

toplam = 0

while True:
    islem = input(" sayı gir ya da cikis yapmak için q ya bas")
    if islem == "q":
        break
    else:
        toplam += int(islem)

print(toplam)