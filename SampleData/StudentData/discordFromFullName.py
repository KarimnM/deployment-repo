import random


popular_domains = ["vcu.edu", "gmail.com", "yahoo.com", "aol.com", "hotmail.com"]
def make_discord_uname_from_full_name(firstname, lastname):
    return firstname + lastname[0] + str(random.randint(0, 9)) + '#{}{}{}{}'.format(*[random.randint(0, 9) for _ in range(4)])

if __name__ == '__main__':
    names = [("Mike", "Hawk"), ("Ben", "Dover"), ("Amanda", "Hugankiss"), ("Heywood", "Jablowme")]
    for first, last in names:
        print(make_discord_uname_from_full_name(first, last))