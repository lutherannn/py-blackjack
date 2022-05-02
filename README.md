# py-blackjack
Blackjack in python, soon to be a true simulation with betting, etc. But for now this is somewhat functional. See TODO for future updates and things you can help with.

# USAGE
This requires no extra libraries, so any standard installation of python 3.\* will work<br>
python py-blackjack.py \<number of games\>

# TODO
Add support for invalid hands. Rare cases may have the dealer and the user's hands have more than four kind of one card.<br>
Fix dealer hand so the dealer's hidden card gets shown after the user stands, as in real life<br>
Add splitting support, so if a user has two of the same card they can play each as its own hand, as in real life<br>
Add double down support after betting is implemented, so the user may double down their first bet if the starting value is 11<br>
Make the program not run if emacs is installed on a machine<br>

# Known Bugs
Issue with determining winner, sometimes the wrong winner is chosen<br>
Issue with ace logic. Not sure exactly why, but the count gets thrown off when an ace with the value of 11 is dealt.
