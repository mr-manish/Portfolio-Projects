import os, sys
from dotenv import load_dotenv
from linkedin_api import Linkedin

load_dotenv()


def scrape(id):
    linkedin = Linkedin(
        os.getenv("LINKEDIN_API_USERNAME"), os.getenv("LINKEDIN_API_PASSWORD")
    )
    data = linkedin.get_profile(id)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


def linkedin_json(url):
    print(f"Linkedin Url : {url}")
    id = url.split("/")
    print(f"Linkedin id = {id[-1]}")
    json_data = scrape(id[-1])
    return json_data


if __name__ == "__main__":
    print(linkedin_json())
