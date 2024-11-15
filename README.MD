
# **My Portfolio Website**

A simple portfolio website built with Django and **Bootstrap 5**.

---

## **Features**
- **Contact Form**: visitors can submit their quieries by filling out their name, email, phone, and a message.
  - It has a validation logic for the form fields.
  - It also displays error messages for invalid inputs.
  - Shows a success message after form submission.
- **Responsive Design**: The site is fully responsive and works across devices.
- **Scalable Structure**: Designed for easy integration of additional features like projects or blogs.
- **Superadmin login**: Created a super admin account to login and view submissions.

---

## **Project Structure**
```plaintext
my_portfolio/
├── contacts/                    # Django app for contact functionality
│   ├── templates/contacts/      # Contact-specific templates
│   ├── urls.py                  # URLs for the contact app
│   ├── views.py                 # Views handling contact logic
│   ├── forms.py                 # Form for validating user input
│   └── models.py                # Contact model definition
├── templates/                   # Project-wide templates
│   ├── base.html                # Base template for consistent layout
│   ├── index.html               # Homepage template
├── static/                      # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css           # Custom styles
├── my_portfolio/                # Django project configuration
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Root URL configuration
└── manage.py                    # Django project management
```

---

## **Technologies used**
- **Backend**: Django (Python)
- **Frontend**: HTML and Bootstrap 5
- **Database**: SQLite

---

## **Future Enhancements**
- Add a **Projects** section to showcase work.
- Integrate an email-sending feature for the contact form submissions.
---