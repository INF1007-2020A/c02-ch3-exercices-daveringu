#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	power = voltage**2 /resistance
    return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	prodscal=v1[0]*v2[0]+v1[1]*v2[1]
    # calculer le produit scalaire
    return prodscal==0
    #vérifier si =0
    #retourner Vrai si =0, Faux sinon

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
    sum = 0
    num_values = 0
	for v in values:
        if v­>= 0:
            sum += v
            num_values +=1
    return sum/num_values
	# La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties=tens=fives=ones=0
    while value != 0:
		if value >= 20:
			twenties=value//20
            value=value%
		elif value >= 10:
			pass
		elif value >= 5:
			pass
		elif value >= 1:
			pass

	return (twenties, tens, fives, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
