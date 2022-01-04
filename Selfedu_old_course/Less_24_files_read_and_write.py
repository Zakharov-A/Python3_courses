# try:
#     file = open("myfile.txt", encoding="utf-8")
#     print( file.read(20) )
#     file.seek(0)
#     print( file.read(20) )
#     pos = file.tell()
#     print( pos )
#
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#---------------------------------------------------------

# try:
#     file = open("myfile.txt")
#     s = file.readline()
#     print( s )
#     print( file.readline() )
#     print( file.readline() )
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


try:
    file = open("myfile.txt")

    try:
        s = file.readlines()
        print(s)
    finally:
        file.close()

except FileNotFoundError:
    print("Невозможно открыть файл")

#------------------------------------------
#-------Stop-Time------13:36---------------