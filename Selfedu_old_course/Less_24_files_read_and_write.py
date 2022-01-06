# try:
#     file = open("myfile.txt", encoding="utf-8")
#     print( file.read(20) )
#     file.seek(0)
#     print( file.read(20) )
#     pos = file.tell()
#     print( pos )

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#---------------------------------------------------------

# try:
#     file = open("myfile.txt")
#     s = file.readline()
#     print( s )
#     print( file.readline() )
   
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#------------------------------------------------------------

# try:
#     file = open("myfile.txt")
#     print( file.readline(), end="" )
#     print( file.readline(), end="" )
#     print( file.readline(), end="" )
#     print( file.readline(), end="" )
#
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#-----------------------------------------------

# try:
#     file = open("myfile.txt")
#     for line in file:
#         print( line, end="")
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#------------------------------------------------


# try:
#     file = open("myfile.txt")

#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#------------------------------------------

# try:
#     # file = open("myfile.txt")
#     with open("myfile.txt", "r") as file:
#         s = file.readlines()
#         print(s)

# except FileNotFoundError:
#     print("Невозможно открыть файл")
# finally:
#     print(file.closed)    

#----------------------------

# try:
#     file = open("out.txt", "w")

#     try:
#         file.write("Hello Hello! Faka!1\n")
#         file.write("Hello Hello! Faka!2\n")
#         file.write("Hello Hello! Faka!3\n")
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#-----------------------

# try:
#     file = open("out.txt", "a+")

#     try:
#         file.write("Hello Hello! Faka!1\n")
#         file.write("Hello Hello! Faka!2\n")
#         file.write("Hello Hello! Faka!3\n")
#         file.seek(0)
#         print( file.read() )
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#-------------------------

# try:
#     file = open("out.txt", "w")

#     try:
#         file.writelines(["Hello Faka1\n", "Hello2\n"])
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#----------------

# import pickle

# books = [
# ("А сороки-Белобоки"),
# ("Поскакали по полям,"),
# ("Закричали журавлям:"),
# ("«Горе! Горе! Крокодил"),
# ("Солнце в небе проглотил!»")
# ]

# try:
#     file = open("out.bin", "rb")

#     try:
#         # pickle.dump(books, file)
#         bs = pickle.load(file)
#         print( bs )
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#--------------------------

# import pickle

# books = [
# ("А сороки-Белобоки"),
# ("Поскакали по полям,"),
# ("Закричали журавлям:"),
# ("«Горе! Горе! Крокодил"),
# ("Солнце в небе проглотил!»")
# ]

# try:
#     file = open("out.bin", "rb")

#     try:
#         # pickle.dump(books, file)
#         bs = pickle.load(file)
#         print( bs )
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#------------------------------------

# import pickle

# books1 = ["А сороки-Белобоки"]
# books2 = ["Поскакали по полям,"]
# books3 =["Закричали журавлям:"]
# books4 =["«Горе! Горе! Крокодил"]



# try:
#     file = open("out.bin", "wb")

#     try:
#         pickle.dump(books1, file)
#         pickle.dump(books2, file)
#         pickle.dump(books3, file)
#         pickle.dump(books4, file)
        
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#-------------------------------

# import pickle

# books1 = ["А сороки-Белобоки"]
# books2 = ["Поскакали по полям,"]
# books3 =["Закричали журавлям:"]
# books4 =["«Горе! Горе! Крокодил"]



# try:
#     file = open("out.bin", "rb")

#     try:
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
#         b4 = pickle.load(file)

#         print(b1, b2, b3, b4, sep="\n")
        
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#--------------------------------

# 1 задача

# k=0

# a=[]

# with open('test.txt', 'r', encoding='utf-8') as f:

# 	for i in f.readlines():

# 		i=i.replace('\n', '')

# 		while (k+len(i))<=100:

# 			a+=i[::2]

# 			k+=len(i)

# 		else:

# 			a+=i[:(100-k):2]

# with open('out.txt', 'w+', encoding='utf-8') as f:

# 	for i in a:

# 		f.write(i)
	





# 2 задача

# try:
#     with open("user_sentence","w",encoding ="UTF-8") as file:
#         sentence = input("Write a sentence:").split()
#         for word in sentence:
#             file.write(word+'\n')
# except Exception as e:
#     print(e)

# 3 задача

# import pickle

# d = {"house": "дом", "car": "машина",

#      "tree": "дерево", "road": "дорога",

#      "river": "река"}

# s=open('w.bin','wb')

# pickle.dump(d,s)

# s.close()

# r=open('w.bin','rb')

# d= pickle.load(r)

# for i in d:

#     print( i,d.get(i))

# r.close()