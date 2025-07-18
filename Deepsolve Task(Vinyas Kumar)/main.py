from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import requests
from bs4 import BeautifulSoup

app = FastAPI()



class Product(BaseModel):
    title: str
    handle: str
    image: Optional[str] = None
    price: Optional[str] = None

class BrandData(BaseModel):
    brand_name: Optional[str]
    about: Optional[str]
    privacy_policy: Optional[str]
    return_policy: Optional[str]
    hero_products: List[Product]
    all_products: List[Product]
    faqs: Optional[List[str]] = []
    social_handles: Optional[List[str]] = []
    contact_details: Optional[List[str]] = []
    important_links: Optional[List[str]] = []


def fetch_shopify_data(store_url: str):
    try:
        products_api = f"{store_url.rstrip('/')}/products.json"
        product_res = requests.get(products_api, timeout=10)

        if product_res.status_code != 200:
            raise HTTPException(status_code=401, detail="Website not found or not a Shopify store.")

        product_data = product_res.json().get("products", [])
        all_products = []
        for product in product_data:
            all_products.append(Product(
                title=product["title"],
                handle=product["handle"],
                image=product.get("image", {}).get("src"),
                price=str(product.get("variants", [{}])[0].get("price", ""))
            ))

        homepage = requests.get(store_url).text
        soup = BeautifulSoup(homepage, "html.parser")
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        text_content = soup.get_text(separator=" ")

        socials = [l for l in links if any(x in l for x in ['instagram.com', 'facebook.com', 'tiktok.com'])]
        contact_details = [line.strip() for line in text_content.split("\n") if "@" in line or any(char.isdigit() for char in line)]

        policy_pages = {
            "privacy_policy": None,
            "return_policy": None,
            "faqs": [],
            "about": None
        }

        for link in links:
            if 'privacy' in link:
                policy_pages['privacy_policy'] = store_url.rstrip('/') + link if link.startswith('/') else link
            if 'return' in link or 'refund' in link:
                policy_pages['return_policy'] = store_url.rstrip('/') + link if link.startswith('/') else link
            if 'faq' in link:
                policy_pages['faqs'].append(store_url.rstrip('/') + link if link.startswith('/') else link)
            if 'about' in link:
                policy_pages['about'] = store_url.rstrip('/') + link if link.startswith('/') else link

        return BrandData(
            brand_name=store_url.split("//")[-1],
            about=policy_pages["about"],
            privacy_policy=policy_pages["privacy_policy"],
            return_policy=policy_pages["return_policy"],
            hero_products=all_products[:5],
            all_products=all_products,
            faqs=policy_pages["faqs"],
            social_handles=socials,
            contact_details=contact_details,
            important_links=list(set(links))
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/fetch-brand", response_model=BrandData)
def fetch_brand_insights(url: str = Query(..., description="Shopify website URL")):
    return fetch_shopify_data(url)

