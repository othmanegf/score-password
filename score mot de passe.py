def NbCMin(password):
    return sum(1 for char in password if 'a' <= char <= 'z')
def  NBCMaj(password):
    return sum(1 for char in password if 'A' <= char <= 'Z')
def NBCAlpha(password):
    return sum(1 for char in password if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'))
def LongMaj(password):
    max_length = 0
    current_length = 0
    for char in password:
        if 'A' <= char <= 'Z':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length
def LongMin(password):
    max_length = 0
    current_length = 0
    for char in password:
        if 'a' <= char <= 'z':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length
def score(password):
    bonus = len(password) + (len(password) - NBCMaj(password)) * 2 + (len(password) - NbCMin(password)) * 3 + NBCAlpha(password) * 5
    malus = LongMin(password) * 2 + LongMaj(password) * 2
    final_score = bonus - malus

    if final_score < 20:
        return "Très faible"
    elif 20 <= final_score < 40:
        return "Faible"
    elif 40 <= final_score < 80:
        return "Fort"
    else:
        return "Très fort"
mot_de_passe=input("entrer le mot de passe:")
resultat = score(mot_de_passe)
print("Le score du mot de passe est ",resultat)
