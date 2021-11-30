from random import choice, randint

def randchar():
    return chr(randint(97, 122))

def random_meeting_link(domain=None):
    possible_domains = ['zoom', 'google']
    if domain is None:
        domain = choice(possible_domains)        
        
    if domain == 'google':
        return "https://meet.google.com/{}{}{}-{}{}{}{}-{}{}{}".format(*[randchar() for _ in range(10)])
    elif domain == 'zoom':
        return "https://zoom.us/j/{}{}{}{}{}{}{}{}{}{}".format(*[randint(0, 9) for _ in range(10)])
    else:
        raise ValueError(f"Domain '{domain}' not supported. The valid domains are {possible_domains}")

if __name__ == '__main__':
    for _ in range(10):
        print(random_meeting_link())