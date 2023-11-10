
# Login Application


The Project Name is a Django web application designed to provide user authentication and basic profile management functionalities. Users can sign up for accounts, log in, update their profiles, and log out. The application follows best practices for handling forms, user authentication, and views in a Django project. 

## Key Features

- **User Authentication:** Allows users to sign up, log in, and log out securely.
- **Profile Update:** Provides a user-friendly interface for updating user profiles, including the ability to change passwords.
- **Responsive Design:** The application is designed with responsiveness in mind, ensuring a seamless experience across various devices.






## Installation
To install and run the project locally, follow the steps:

1. Clone the repository:


```bash
git clone https://github.com/casonova/Login-Application.git
```
    
2. Install dependencies:

```bash
pip install -r requirements.txt
```    
3. Apply database migrations:
```bash
python manage.py makemigrations
```  

```bash
python manage.py migrate
```    
## Usage
1. Create a superuser:

```javascript
python manage.py createsuperuser
```

2. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and recipes.

3. Visit `http://127.0.0.1:8000/signup/` to register yourself as a user on project.

4. Visit `http://127.0.0.1:8000/login/` to log in and access the application functionality.




## Credits

- [Django Framework](https://www.djangoproject.com/)



