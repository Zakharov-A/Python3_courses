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
#     file = open("out.txt", "rb")

#     try:
#         # pickle.dump(books, file)
#         bs = pickle.load(file)
#         print( bs )
#     finally:
#         file.close()

# except FileNotFoundError:
#     print("Невозможно открыть файл")

#--------------------------

import pickle

books = [
("А сороки-Белобоки"),
("Поскакали по полям,"),
("Закричали журавлям:"),
("«Горе! Горе! Крокодил"),
("Солнце в небе проглотил!»")
]

try:
    file = open("out.txt", "rb")

    try:
        # pickle.dump(books, file)
        bs = pickle.load(file)
        print( bs )
    finally:
        file.close()

except FileNotFoundError:
    print("Невозможно открыть файл")