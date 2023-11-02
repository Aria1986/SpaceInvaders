# set1= { 10, 20, 30, 40,50}
# set2= { 30, 40, 50, 60,70}
# set1.intersection(set2)

# # {40,50,60}
# set1
# # {50,20,40,10,30}

# type(set1.intersection(set2))
# s=[]
# for element in set1:
#     if element in set2:
#         s = s + [element]
        
# print('Veuillez entrer votre nom')
# nom = input()
# print(f'bonjour{nom}')

# def multiplication(n, nombre):
    # print('saisissez la valeur de n')
    # n= int(input())
    # print('saisissez la valeur du nombre')
    # nombre= int(input())
    
#    for i in range(n):
#     print(i*nombre, end(';'))
    
# def diviseur():
#     diviseurs=[]
#     # generateur:
#     # diviseurs=[x for x in range(2, entier) if entier % x ==0]
#     print('saisissez la valeur d\'un entier supérieur à un')
#     n= int(input())
#     if (n<1):
#         print('le nombre est inférieur à un veuillez en resaisir un')
#         n= int(input())
#     else:
#         for i in range(2,n-1):
#             if(i % n == 0):
#                 diviseurs.append(i)
                
#         if len(diviseurs) == 0:
#             print('aucun ! Il est premier')
#         elif len(diviseurs) != 0:
#             print(f'Diviseurs propres sans répétition de {n} : {diviseurs}(soit {len(diviseur)} diviseurs propres)')
    
    # ex suivant        
    # def diviseurs(entier):
    #     return diviseurs=[x for x in range(2, entier) if entier % x ==0]
    
    # cmpte = 0
    # res = []
    # nb_res = 0
    # while nb_res <=100:
    #     if len(diviseurs(i)) == 0:
    #         if nb_res !=100:res.append(i)
    #         nb_res +=1
    #     i +=1
    # print(res)
    
    # Fibonacci
    # def fibonacci(nombre):
    #     result = 0
    #     liste = []
    #     for i in range(0,nombre):
    #         result +=i
    #         liste.append(result)
    #     print(result)
        
    # gardien de phare
    # def hauteurParcourue(nb_marche, hauteurMarche):
    #     x = 10*nb_marche*hauteurMarche/100
    #     print('Pour{nb_marche} marches de{hauteurMarche} cm, il parcourt{:.2f}'.format(x)'m par semaine')
        
        
    # chaine ADN
    # adn = input('veuillez saisir la chaine d\adn:')
    # proteine =['a','t', 'g','c']
    # def valide():
    #     # for i in range (0,len(adn)):
    #     if(proteine in adn == False or (!adn)):
    #         return False
    #     else:
    #         return True
        
    # def saisie():
    #     for i in range(0,10):
    #         adn+random.choice(proteine)
    #     return adn
    
    # def proportion(chaine, sequence):
    #     y=0
    #     for i in range(0,len(chaine)):
    #         if(sequence == chaine[i].chaine[i+1]):
    #             y+=1
    #     proportion = y/len(chaine)
    #     print(f'il y a {proportion} %de {sequence} dans votre chaine')