from selenium import webdriver # pip install selenium
import os
import re
# from mylib.myterminal import LoadingBar

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # To download a driver for Chrome, go to https://chromedriver.chromium.org/downloads
    # and download the driver for your OS. Place it in the same directory as this file, 
    # and make sure to rename the file -------------------------------- here \/
    driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), "chromedriver.exe"), options=options)
    driver.get("http://bulletin.vcu.edu/azcourses/")

    department_links = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        link = elem.get_attribute("href")
        if re.match(r"http://bulletin\.vcu\.edu/azcourses/\w{4}/", link):
            department_links += [link]


    # lb = LoadingBar(0.3333)
    course_titles = []
    for i, link in enumerate(department_links):
        # lb.display(i / len(department_links))
        print(f"\r ({i} / {len(department_links)}) complete     ", end='', flush=True)
        driver.get(link)
        course_names = driver.find_elements_by_class_name("courseblocktitle")
        for course_name in course_names:
            title = course_name.find_element_by_tag_name("strong").text
            course_titles += [title]

    # lb.finish()
    print(f"({len(department_links)} / {len(department_links)}) complete       ")
    print("Saving . . .")
    with open("courses.txt", 'w+') as f:
        f.write("\n".join(course_titles))
    print("Done.")