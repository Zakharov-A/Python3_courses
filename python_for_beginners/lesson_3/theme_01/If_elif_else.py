# ---if ---
# x = 80
#
# res = "xs"
# if x >= 80:
#     res = "s"
# if x >= 100:
#     res = "m"
# if x >= 150:
#     res = "l"
# if x >= 180:
#     res = "xl"

# print(res)

# ---- if - elif ----

# x = 60
# if x < 80:
#     res = "xs"
# elif x < 100:
#     res = "s"
# elif x < 150:
#     res = "m"
# elif x < 180:
#     res = "l"
# else:
#     res = "xl"

# print(res)

# ----

x = 130
if x >= 180:
    res = "xl"
elif x >= 150:
    res = "l"
elif x >= 100:
    res = "s"
elif x >= 80:
    res = "s"
else:
    res = "xs"
print(res)