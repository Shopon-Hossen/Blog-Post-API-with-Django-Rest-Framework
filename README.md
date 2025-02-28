# **📝 Blog-Post-Backend-in-DRF**  
A **blog platform** built with **Django REST Framework (DRF)**. Users can create, read, update, and delete blog posts, leave comments, and search for posts.  

---

## **🚀 Features**  
✔ Create & Manage Blog Posts  
✔ Comment on Blogs  
✔ Search Functionality  
✔ User Authentication  
✔ API Ready for Postman  

---

## **🛠 Installation**  

```bash
# Clone the repository
git clone https://github.com/Shopon-Hossen/Blog-Post-Backend-in-DRF.git
cd Blog-Post-Backend-in-DRF

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r .rqmt

# Set up environment variables
echo "SECRET_KEY=your-secret-key" > .env

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

📂 **Postman Collection:** `Blog Post back-end DRF.postman_collection.json`  

---
## **📃 List of URLs**
```
api/account/register/
api/account/login/
api/account/user/
api/account/update-user/
api/account/change-password/
api/account/user/<int:pk>/ # pk: user id
api/account/user/<int:pk>/blogs/ # pk: user id
api/blog/create/
api/blog/list/
api/blog/update/<int:pk>/ # pk: blog id
api/blog/detail/<int:pk>/ # pk: blog id
api/blog/delete/<int:pk>/ # pk: blog id
api/search/
api/search/suggestion/
api/comment/list/
api/comment/create/
api/comment/delete/<int:pk>/ # pk: comment id
```

---

## **📜 License**  
This is a **showcase project**, and no specific license is applied.  

---

## **👤 Author**  
**[Shopon Hossen](https://github.com/Shopon-Hossen)**  
🔗 GitHub: [Shopon-Hossen/Blog-Post-Backend-in-DRF](https://github.com/Shopon-Hossen/Blog-Post-Backend-in-DRF)  # Blog-Post-API-with-Django-Rest-Framework
