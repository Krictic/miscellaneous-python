def generate_hashtag(str):
    if str == "":
        return False

    hashtag = ""
    temp = ["#"]
    strlist = str.split()

    for i in strlist:
        i = i.capitalize()
        temp.append(i)

    hashtag = hashtag.join(temp)

    if len(hashtag) > 140:
        return False

    return hashtag


string = input("Enter a string (less than 140 characters long): ")

print(generate_hashtag(string))
