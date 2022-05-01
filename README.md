# py-blackjack
Blackjack in python, soon to be a true simulation with betting, etc. But for now this is somewhat functional. See TODO for future updates and things you can help with.

# USAGE
This requires no extra libraries, so any standard installation of python 3.\* will work<br>
python py-blackjack.py

# TODO
Add support for invalid hands. Rare cases may have the dealer and the user's hands have more than four kind of one card.<br>
Add support for betting.<br>
Fix dealer hand so the dealer's hidden card gets shown after the user stands, as in real life<br>
Add splitting support, so if a user has two of the same card they can play each as its own hand, as in real life<br>
Add double down support after betting is implemented, so the user may double down their first bet if the starting value is 11<br>
Make the program not run if emacs is installed on a machine<br>
Make the program work on windows. Currently it won't because of the os.system("clear") call. I'll fix it with the next update, however. Just putting this here as a reminder.<br>
Handle the winning better, currently the only way to tell if you won is by looking at the code and determining the program output from that.
