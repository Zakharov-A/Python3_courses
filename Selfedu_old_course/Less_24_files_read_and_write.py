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

# 1 задача1: Странно не увидел ни у кого использование срезов сразу в файле.. так же проще по моему.
try:
    file2 = open('text1.txt', 'r', encoding='utf-8')
    file3 = open('text2.txt', 'w', encoding='utf-8')
    try:
        f2 = file2.read(100)
        f3 = file3.write(f2[::2])
    finally:
        file2.close()
        file3.close()
except FileNotFoundError as fnfe:
    print(fnfe)
