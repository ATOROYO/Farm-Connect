# FarmConnect Platform

FarmConnect is a comprehensive platform designed to bridge the gap between farmers, suppliers, buyers, and investors. This project empowers agricultural stakeholders by providing tools for networking, collaboration, and market engagement. Built with **Python Django**, this platform aims to revolutionize the agricultural ecosystem with modern technology.

---

## Features

### 1. Farmer Registration and Profiles

- Farmers can create profiles to showcase their farm produce, farming techniques, and available resources.
- Profiles include photo galleries, certifications, and descriptions of farm products.

### 2. Supplier Directory

- Suppliers can register and list products (seeds, fertilizers, equipment, etc.).
- Includes product categories, pricing, and delivery options.

### 3. Marketplace for Buyers

- Buyers can browse available farm produce and make inquiries or purchases.
- Includes filtering by product type, region, and price.

### 4. Investment Opportunities

- Investors can view and fund farming projects.
- Farmers can propose projects requiring financial support.

### 5. Forums and Discussions (Planned)

- A dedicated space for farmers, suppliers, and buyers to share insights and discuss trends in agriculture.

### 6. Real-Time Market Analytics (Planned)

- Visual dashboards for market price trends, weather updates, and regional demands.

### 7. Mobile App Integration (Planned)

- A companion mobile application for on-the-go access to the platform's features.

---

## Technologies Used

- **Backend**: Python Django Framework
- **Frontend**: HTML, CSS, JavaScript (Django templates for now; future plans for React.js integration)
- **Database**: PostgreSQL
- **Hosting**: To be decided (Options include AWS, Heroku, or DigitalOcean)

---

## Project Structure

Below is the directory structure of the project:

```plaintext
FarmConnect/
│
├── farmconnect/                # Django project settings and configurations
│   ├── settings.py             # Main settings file
│   ├── urls.py                 # Project-level URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── apps/                       # Django applications folder
│   ├── users/                  # Handles user registration and profiles
│   ├── marketplace/            # Marketplace functionality
│   ├── investments/            # Investor-farmer collaboration
│   └── forums/                 # Planned forums for discussions
│
├── static/                     # Static files (CSS, JavaScript, images)
├── templates/                  # HTML templates
├── manage.py                   # Django's management script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Installation

**1. Clone this repository**

```bash
   git clone https://github.com/ATOROYO/Farm-Connect.git
```

**2. Navigate to the project directory**

```bash
   cd Farm-Connect
```

**3. Create and activate a virtual environment**

```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
```

**4. Install dependencies**

```bash
   pip install -r requirements.txt
```

**5. Apply migrations**

```bash
   python manage.py migrate
```

**6. Run the server**

```bash
   python manage.py runserver
```

Here's the **Project Pages** section in plain text format:

---

## Project Pages (Implemented and Planned)

### Home Page

**Status**: Implemented  
 **Description**: Overview of the platform with navigation links.

### About Page

**Status**: Implemented  
 **Description**: Explain the vision and mission of the platform of the platform with navigation links.

### Market Page

**Status**: Implemented  
 **Description**: Is where the buyer page is situated and other sub pages

### Investment page

**Status**: Pending  
 **Description**: Is where opportunities for investment can be found and application for funding

### User Registration

**Status**: Pending  
 **Description**: Signup forms for farmers, suppliers, buyers, and investors.

### Dashboard

**Status**: Implemented/Pending  
 **Description**: User-specific dashboards for managing accounts and activities.

### Marketplace

**Status**: Pending  
 **Description**: Product listings with search and filter functionalities.

### Projects

**Status**: Planned  
 **Description**: Farmers can create and showcase their proposed projects for funding.

### Investors Dashboard

**Status**: Planned  
 **Description**: A dedicated section for investors to browse and fund projects.

### Proposal Submissions

**Status**: Planned  
 **Description**: Page for farmers to submit detailed funding proposals.

### Project Tracking

**Status**: Planned  
 **Description**: Real-time updates for funded projects, showing progress reports.

### Forum

**Status**: Planned  
 **Description**: Community discussions on agriculture-related topics.

### Analytics

**Status**: Planned  
 **Description**: Real-time market insights with charts and reports.

### Help Center

**Status**: Planned
**Description**: FAQs, contact support, and guides for using the platform.

## Pitch Deck

To learn more about the vision and details of the FarmConnect platform, please refer to our Pitch

### Deck

[View the Pitch Deck](#)

## Team

This project is a collaborative effort by:

**[David Atoroyo Sika - Lead Developer](mailto:davidatoroyosika@gmail.com)**
**[Patricia Akumu - Developer](mailto:akumupatricia25@gmail.com)**
**[Ritah Wanyiri - Developer](mailto:ritahwanyiri@gmail.com)**
**[Daniel Mule - Developer](mailto:danielmule638@gmail.com)**

## Contributing

We welcome contributions from the community! If you would like to contribute:

### 1.Fork this repository.

### 2.Create a feature branch

```bash
    git checkout -b feature/your-feature-name
```

### 3.Commit your changes and push

```bash
    git push origin feature/your-feature-name
```

### Open a pull request and describe your changes.

## Conclusion

Let me know if you need any further additions or modifications!

### THANKS!!!
