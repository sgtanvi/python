
playing = True

while playing:


	damageHeroDoes = float(input("How much damage does the hero do? Type a number: "))

	damageCompanionDoes = float(input("How much damage does the hero's companion do? Type a number: "))

	DragonScaleDamageResist = .2

	totaldamage = damageCompanionDoes + damageHeroDoes 

	print("Total Damage by Heros : ")
	print(totaldamage)

	damageTakenbyDragon = totaldamage * DragonScaleDamageResist

	print("Dragon's Health % After Hit :")
	dragonHealth = 100 - damageTakenbyDragon
	print(dragonHealth)


	did_win = dragonHealth <= .5
	print("Did they beat the dragon?", did_win)

	want_play = input("Want to play again? (y/n)")
		if want_play == n:
		playing = False