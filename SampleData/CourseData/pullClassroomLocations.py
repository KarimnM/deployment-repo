from selenium import webdriver # pip install selenium
import os
import re
import urllib.request
from urllib.parse import urljoin

if __name__ == '__main__':
    url = "https://maps.vcu.edu/monroepark/function.html#Academic"
    html = urllib.request.urlopen(url).read().decode()
    start_index = html.index("Classroom")
    end_index = html.rindex("Administrative offices and service facilities")
    target_html = html[start_index : end_index]

    classroom_links = []
    for line in target_html.splitlines():
        match = re.match(r'^\s*<li>\s*<a href="(.*)">.*$', line)
        if match:
            classroom_links += [match.group(1)]

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "chromedriver.exe"), options=options)
    addresses = []
    for link in classroom_links:
        driver.get(urljoin(url, link))
        classroom_name = driver.find_element_by_id("title").find_element_by_tag_name("h2").text
        addr = driver.find_element_by_id("title").find_element_by_tag_name("h3").text
        print(classroom_name)
        print(addr)
        print()
        addresses += [classroom_name + "\n" + addr + ", Richmond, VA 23220"]

    print("Saving . . .")
    with open("classrooms.txt", 'w+') as f:
        f.write("\n".join(addresses))
    print("Done.")
    driver.quit()