# **📝 Blog-Post-Backend-in-DRF**

A **blog platform** built with **Django REST Framework (DRF)**. Users can create, read, update, and delete blog posts, leave comments, and search for posts.

---

## **🚀 Features**

✔ Create & Manage Blog Posts  
✔ Like and Comment on Blogs  
✔ Search Functionality  
✔ User Authentication  
✔ Tag System for Blog  
✔ API Ready for Postman

---

## **🛠 Installation**

```bash
# Clone the repository
git clone https://github.com/Shopon-Hossen/blog-post-api-drf.git blog_post
cd blog_post

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY=\"{get_random_secret_key()}\"')" > .env

# Apply database migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

---

## **📡 API Documentation**

You can test the API using **Postman**. Import the collection:

📂 **Postman Collection:** `blog_post.postman_collection.json`

---

## **📃 List of URLs**

```bash
python list_urls.py
```

---

## **📜 License**

This is a **showcase project**, and no specific license is applied.

---

## **👤 Author**

- **[Shopon Hossen](https://github.com/Shopon-Hossen)**
- **[Shopon-Hossen/Blog-Post-API](https://github.com/Shopon-Hossen/https://github.com/Shopon-Hossen/blog-post-api-drf)**
