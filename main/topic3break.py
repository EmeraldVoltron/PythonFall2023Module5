# a_list = "the quick brown fox jumped over the lazy dog".split(" ")
# print(a_list)
#
# words_in_count = 0
# for word in a_list:
#     print("loop is currently at: " + word)
#     words_in_count += 1
#     if word == "fox":
#         break
# print("fox was the " + str(words_in_count) + "th word in the sentence.")

# a_list = "the quick brown fox jumped over the lazy dog".split(" ")
# print(a_list)
# words_in_count = 0
# size_of_a_list = len(a_list)
# index = 0
# while(index < size_of_a_list):
#     print("loop is currently at: " + a_list[index])
#     words_in_count = (index+1)
#     if a_list[index] == "fox":
#         break
#     index += 1
# print("fox was the " + str(words_in_count) + "th word in the sentence.")

a_list = "the quick brown fox jumped over the lazy dog".split(" ")
print(a_list)
words_in_count = 0

for word in a_list:
    words_in_count += 1
    if word != "fox":
        continue
    print("loop is past continue and currently at: " +word)
    print("fox was the " + str(words_in_count) + "th word in the sentence")