# %%

# 1. Import the necessary LIBRARIES
import requests
from bs4 import BeautifulSoup

links = [
    f"http://www.alhabibomar.com/Lessons.aspx?SectionID=7&CatID=3&page={i}" for i in range(1, 47)]
links[::-1]

mp3_links = []

with open('..\links.txt', 'a', encoding="UTF-8") as f:
    for l in links:
        # 3. Send get() Request and fetch the webpage contents
        response = requests.get(l)
        webpage = response.content

        # 4. Check Status Code (Optional)
        # print(response.status_code)

        # 5. Create a Beautiful Soup Object
        soup = BeautifulSoup(webpage, "html.parser")
        # 6. Implement the Logic.
        for link in soup.find_all('a', text="Mp3"):
            new_links = [link.parent.parent.parent.parent.find_all(
                "h3")[0].a.string, "\t", link['href']]
            f.writelines('\n'.join(new_links))
            mp3_links += new_links
            print("\n".join(mp3_links))
            pass

print("\n".join(mp3_links))
