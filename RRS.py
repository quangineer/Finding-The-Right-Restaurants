Cuisine = ["Chinese","Thai","Japanese","Canadian","Pub Food"]
Price = "$$$"

Filename = "Restaurants.txt"
A = open(Filename)
B = A.readlines()

Name_to_Rating = {}
for i in range((len(B)+1)//5):
    i = i * 5

    Name_to_Rating[B[i].strip('\n')] = B[i+1].strip('\n')
print "Name_to_Rating is", Name_to_Rating

Price_to_Names = {}
for i in range((len(B)+1)//5):
    i = i * 5
    if not (B[i+2].strip('\n') in Price_to_Names):
        Price_to_Names[B[i+2].strip('\n')] = [B[i].strip('\n')]
    else:
        Price_to_Names[B[i+2].strip('\n')].append(B[i].strip('\n'))
print "Price_to_Names is", Price_to_Names


C = {}
for i in range((len(B)+1)//5):
    i = i * 5
    C[B[i].strip('\n')] = ((B[i+3]).strip('\n')).split(',')
# print C
Cuisine_to_Names = {}
for i in C:
    # print C[i]
    for x in range(len(C[i])):
        if not (C[i][x] in Cuisine_to_Names):
            Cuisine_to_Names[C[i][x]] = [i]
        else:
            Cuisine_to_Names[C[i][x]].append(i)
print "Cuisine_to_Names is", Cuisine_to_Names

def recommend(Price):
    names_matching_price = Price_to_Names[Price]
    return names_matching_price
print recommend(Price)


names_matching_price = recommend(Price)
def names_final(names_matching_price, Cuisine_to_Names, Cuisine):
    filter_by_cuisine = []
    for i in range(len(Cuisine)):
        if Cuisine[i] in Cuisine_to_Names:
            for z in range(len(Cuisine_to_Names[Cuisine[i]])):
                if (Cuisine_to_Names[Cuisine[i]])[z] in names_matching_price:
                    filter_by_cuisine.append((Cuisine_to_Names[Cuisine[i]])[z])

                
    return filter_by_cuisine
print names_final(names_matching_price, Cuisine_to_Names, Cuisine)


Q = names_final(names_matching_price, Cuisine_to_Names, Cuisine)
def build_rating_list(Name_to_Rating, Q):
    P = {}
    for i in range(len(Q)):
        if Q[i] in Name_to_Rating:
            P[Q[i]] = Name_to_Rating[Q[i]]
    return P
print build_rating_list(Name_to_Rating, Q)

J = build_rating_list(Name_to_Rating, Q)
JVP = list(J.keys())
Final = []
for i in range(len(JVP)):
    Final.append([int((J[JVP[i]]).strip("%")),JVP[i]])
print Final

AC = Final 
AC.sort(key=lambda x : x [0])
print AC