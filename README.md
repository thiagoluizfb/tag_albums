# TAG ALBUMS

The live version of this game can be viewed [here](https://tag-albums.herokuapp.com/)

![image](https://user-images.githubusercontent.com/62474197/110554863-7c150680-8133-11eb-8982-157af82f69c1.png)


This is my first Full Stack Frameworks with Django Project submitted in completion of the Code Institute’s Diploma in Software Development.

The project was developed based on the View-Model-Controller architecture with multiple apps according to the usability of each part of the web application.

The focus of Tag Albums is to provide a website able to categorize photos according to labels provided by the user. A single album can be created by just uploading photos and labeling them.

Users can register and create an account to save their photos and albums.

----------------------------------------------------------------------------------------------------------------------------------------

# USER EXPERIENCE - UX 


## Main Goals

  The users for this web-page would be people who love photos and make albums. When navigating through the website, users will be able to:
  
  - Upload photos and create albums.
  - Organize photos according to categories created by them.
  - Tag and “un-tag” photos.
  - Save different albums.
  
  The site owner will have the opportunity to receive donations made by the users who are willing to help with the website or just want to get rid of add pop ups.


## User Stories

  - As a user, I would like to create albums with the photos uploaded, so that I can organize my photos as I was making a physical album;
  - As a user, I would like to view all my albums created, so that I can quick switch between albums;
  - As a user, I would like to register for an account, so that I can save my details and upload my photos pravitely and storage photos in a different place than my phone/computer/camera memory;
  - As a user, I would like to tag photos uploaded by categories, location and dates, so that I can categorize photos by tag;
  - As a user, I would like to untag photos, so that I can recategorize my photos and albums;
  - As a user, I would like to easliy remove photos from the webpage, so that I can control the photos that I have storaged in the webpage;

  ### User Authentication
    - As a user, I would like to log in and log out, so that I can access my photos from any device;
    - As a user, I would like to recover my password in case I forget it, so that I can recover access to my account;
    - As a user, I would like to receive an email confirmation after registering, so that I can be assured that my contact is not being used by another user
    - As a user, I would like to have my personalized user profile, so taht I can save my albums privetely.

  ### New User
    -  As a new user, I would like to see how te website works without saving my photos or registering
    
## Site Owner and Admin
  As a site owner, I would like to be able to maintain the page through donations and/or publicity adds;

 
## Design

  ### Colours

     ![tag_albums](https://user-images.githubusercontent.com/62474197/110557157-eb8cf500-8137-11eb-87c7-c59a7486923a.png)
     
    - The main background colour throughout the website is Eire Black, intentionally to contrast colorful photos;
    - Photos wrappers are plain white, resembling printed photos borders;
    - Fonts throughthout the website is grey also to help to highlight photos;
    - Alert messages for errors in forms have their font colour dark red, a nice touch over the background.
    

  ### Typography
     - The font chosen for this web site was Open Sans, also for its simplicity and well aceptance.


  ### Wireframes
     - Initial wireframes for this project can be found in pdf as [here](https://github.com/thiagoluizfb/tag_albums/files/6112229/Tagalbums_wireframes.pdf)


---------------------------------------------------------------------------------------------------------------------------------------


# FEATURES

  ## Landing page
    - The landing page is already interactive, it has a blinking tab which tempts the user to already starting tagging, which is the main goal of the page
    - Each time that the user writes and press enter, a new tag is created and is placed in one of the original tags;
    - It has a loop that after the third time, the new tag replaces the first one.
    
  ## Anonymous Users
    - Anonymous users cannot save photos uploaded. They are cached in the session instead;
    - Each time that the home page is accessed, all the photos uploaded and their tags are deleted.
  
  ## Add popup
    - A add pops in the screen every 15 seconds after the last upload;
    - The add pop up advises the users that are logged into their account and donation placed with the same email will not see the pop up again.

  ## Buy me a snack
    - Users willing to contribuite with the page maintanance can make a donation buying some snacks to the site owner;
    - Once the user register an account and buy a snack, will not see the popup add again.
  
  
----------------------------------------------------------------------------------------------------------------------------------------


# TECHNOLOGY USED

  ## Languages Used

  -   [HTML5](https://en.wikipedia.org/wiki/HTML5);
  -   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets).
  -   [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript).
  -   [Python](https://www.python.org/)
  -   [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

  ## Frameworks, Libraries & Programs Used

  1.[Django](https://www.djangoproject.com/)
    - Python framework used to build the project  
  2.[Jquery](https://jquery.com/)
    - Used to simplify JavaScript usage and trigger Bootstrap and Stripe functions
  3.[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to simplify, style and validate forms
  4. [Bootstrap 4.5:](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
    - Bootstrap was used to assist with positioning.
  5. [Stripe]
    - Used validate credit card information to buy snacks and handle financial transactions
  5. [Google Fonts:](https://fonts.google.com/)
    - Google fonts was used to import the 'Open Sans' into the style.css file which is used on all pages throughout the project.
  6. [Font Awesome 5.6.3:](https://fontawesome.com/)
    - Font Awesome was used to add icons to nav icons and links
  7. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  8. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
  9. [Balsamiq](https://www.adobe.com/products/xd.html)  
    - Balsamiq was used to create the initial [wireframes](https://github.com/thiagoluizfb/tag_albums/files/6112229/Tagalbums_wireframes.pdf) for this project
  10. [Coolors.co](https://coolors.co/)
    - Used to create colour palette.
     
     
  
  ## Databases
  
  1. SQlite3 - database used during development
  2. PostgreSQL - database used for production

---------------------------------------------------------------------------------------------------------------------------------------
# TESTING
---------------------------------------------------------------------------------------------------------------------------------------

# DEPLOYEMENT

The IDE platform used to develop this project was GitPod and GitHub used for version control. The project is hosted on the Heroku platform. To host Media and Static Files, it was used AWS S3 Bucket. Please find the steps followed to deploy this project.


## Heroku Deployment

### Basic steps in the terminal

  1.	Install gunicorn
  2.	Install psycog2-binary
  3.	Install dj-database-url
  4.	Add to requirements (Pip3 freeze –local > requirements.txt)
  5.	Create a Procfile and add the command web: gunicorn tag_albums.wsgi:application)

### Heroku Configuration

  1.	Create new app
  2.	Set Region (the most close to you)
  3.	Select Postgres as database in the Add-ons section
  4.	Go to settings and in Config Vars, add all necessary variables to access and run the app, for this project it was used the following:
  1.	AWS_ACCESS_KEY_ID
  2.	AWS_SECRET_ACCESS_KEY
  3.	DATABASE_URL (Postgres)
  4.	EMAIL_HOST_PASS
  5.	EMAIL_HOST_USER
  6.	SECRET_KEY
  7.	STRIPE_PUBLIC_KEY
  8.	STRIPE_SECRET_KEY
  9.	STRIPE_WH_SECRET
  10.	USE_AWS

### App Settings

In setting in your main app add use os.getenv() and/or os.environ.get() commands to set all the keys. But before, data must be loaded to Postgres. For example: 

DATABASES = {
        'default': dj_database_url.parse(os.environ.get(<postgres_database_link>))
    }
 
  1.	Add Heruko to your ALLOWED_HOSTS 
  2.	Once it is configured, set your database to Postgres temporarily
  3.	Log in into Heroku and migrate your models and data to Postgres
  4.	Create a superuser to access the data in Postgres
  5.	Export data to Postgres using python3 manage.py loaddata command or export = “database_link” whenever it is necessary
  6.	After exported, remove the postgres_database_link and change it to the variable set in Heroku.
  7.	To enable automatic deployment from Gitpod to Heroku, the function must be set in the Automatic Deployment section.
  8.	When enabled, every git push command in the terminal will automatically deploy to Heroku.

### Amazon Web Services (AWS)

To host media and static files in S3 Bucket in AWS:

  1.	Create an account in AWS
  2.	Create your S3 Bucket with public access
  3.	After completing configuration it will generate a AWS_ACCESS_KEY_ID and a AWS_SECRET_ACCESS_KEY, variables to be added in your Config Vars in Heroku. Also set USE_AWS key to True
  4.	The necessary variables need to be also added to settings in your app
  5.	More information in steps and documentation can be found **HERE**

### Email validation
 
  Gmail was used to validate new users in the platform. After creating an account in the website, the user will receive a link to validate.
  
  1. In settings in Gmail account, set up an app request
  2. An app password will be generated
  3. EMAIL_HOST_USER and EMAIL_HOST_PASS must be added to Config Vars in Heroku as well as in settings in your main app in the EDI
  4. Once configured, real emails can be sent.

## Cloning this repository

  1. To clone this repository, type the command git clone https://github.com/thiagoluizfb/tag_albums
  2. This can also be done via GitHub by clicking the green button Clone or download , then Download Zip button. Once the files are extracted, it can accessed by linking its location in your terminal directory.

## Stripe Keys
  1. For more information about how to install and set up Stripe Keys and WebHooks please access **Stripe Documentation


---------------------------------------------------------------------------------------------------------------------------------------

# CREDITS

-   This ReadMe file was based on a sample available on [Code Institute Solutions repositories](https://github.com/Code-Institute-Solutions)

-   Quick information of "how to" was promplty found on [W3Schools](https://www.w3schools.com/)

-   To all comunity present in stackoverflow, where quick questions were easily found.

-   The game rules were based on this [post](https://howdoyouplayit.com/parcheesi-rules-play-parcheesi/) (rules can slightly vary)

---------------------------------------------------------------------------------------------------------------------------------------- 

# AKNOWLEDGEMENTS

-   My Mentor for continuous helpful feedback.

-   Code Institute video classes with its helpful content.

-   My wife, Cristina, who supported me pantiently in the long hours spent coding
