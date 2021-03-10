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

  ### New User
  -  As a new user, I would like to see how te website works without saving my photos or registering
    
  ## Site Owner and Admin
  As a site owner, I would like to be able to maintain the page through donations and/or publicity adds.

 
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

This project is made by the main app "tag_albums" and also by more four apps: "Home", "Profiles", "Photos" and "Subscription".


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

  1. [Django](https://www.djangoproject.com/)
      - Python framework used to build the project  
  2. [Jquery](https://jquery.com/)
      - Used to simplify JavaScript usage and trigger Bootstrap and Stripe functions
  3. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
      - Used to simplify, style and validate forms
  4. [Bootstrap 4.5:](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
      - Bootstrap was used to assist with positioning.
  5. [Stripe](https://stripe.com/)
      - Used validate credit card information to buy snacks and handle financial transactions
  6. [Google Fonts:](https://fonts.google.com/)
      - Google fonts was used to import the 'Open Sans' into the style.css file which is used on all pages throughout the project.
  7. [Font Awesome 5.6.3:](https://fontawesome.com/)
      - Font Awesome was used to add icons to nav icons and links
  8. [Git](https://git-scm.com/)
      - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  9. [GitHub:](https://github.com/)
      - GitHub is used to store the projects code after being pushed from Git.
  10. [Balsamiq](https://www.adobe.com/products/xd.html)  
     - Balsamiq was used to create the initial [wireframes](https://github.com/thiagoluizfb/tag_albums/files/6112229/Tagalbums_wireframes.pdf) for this project
  11. [Coolors.co](https://coolors.co/)
      - Used to create colour palette.


 ---------------------------------------------------------
 
 
 ## DATA ARCHITECTURE
  
  To store data in the development level, the database SQlite3 was installed when app was created with Django, while for production the website uses PostgreSQL (add-on provided by Heroku)
  
  
## Data Modeling

### Authentication Model

Users can create their account using authorization form created by django.
The model was instaled by typing the following commands in the terminal

      pip3 install django-allauth
      
      cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/


It is also necessary to add AUTHENTICATION_BACKENDS in settings in the main app

      AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
    ]

The complete guide to install all_auth can be found [here](https://django-allauth.readthedocs.io/en/latest/installation.html)


### Profiles App

#### UserProfile Model

| Name | Key | Field Type | Validation |
| --- | ----------- |-----|---- |
| User | user | OneToOneField (User) | on_delete=models.CASCADE |
| Nickname | display_name | CharField | max_length=20, null=True, blank=True |

UserProfile is created as via signals once a new account is set up. Nickname is set with the same username, this field can be edited by users once they access their account.
 
 
### Subsbscription App

#### Tiers Model

| Name | Key | Field Type | Validation |
| --- | ----------- |-----|---- |
| User | user | ForeignKey (UserProfile) | on_delete=models.SET_NULL,null=True, blank=True, related_name='tier' |
| Tier | tier | BooleanField | default=False |

Tiers are created as via signals once a new UserProfile is set up. Tier has default set to False and it is set to True once the same email used to create to open the account is also linked to a donation made by the user. When Tier is set to True, users will no longer see popup add.

#### Snack Model

| Name | Key | Field Type | Validation |
| --- | ----------- |-----|---- |
| First Name | f_name |CharField | max_length=50, null=False, blank=False|
| Last Name | l_name | CharField|max_length=50, null=True, blank=True|
| Email | email| EmailField| max_length=254, null=False, blank=False|
| Street Address 1 | street_address1|CharField | max_length=80, null=False, blank=False|
| Street Address 2 | street_address2|CharField | max_length=80, null=True, blank=True|
| Town or City | town_or_city| CharField| max_length=40, null=False, blank=False|
| County | county| CharField| max_length=80, null=True, blank=True|
| Postal Code | postcode|CharField | max_length=20, null=True, blank=True|
| Country | country|CountryField | blank_label='Country', null=False, blank=False, default='Country'|
| Date | date| DateTimeField| auto_now_add=True|
| Snack Quantity | sanck_qty| IntegerField| null=False, default=0|
| Total | total| IntegerField| null=False, default=0|
| Snack Data | snack_data | TextField| null=True, blank=True, default=''|
| Stripe PID | stripe_pid | CharField| max_length=254, null=True, blank=True, default='|


Snack data is created when the user decides to donate to the page. It is symbolically called "buy me a snack". Fields required are **First Name** , **Email**, **Street Address 1**, **Town or City**, **Country**, **Snack Quantity** and **Total** (These last two fields are set a page before the user is redirected to the payment screen)

Once the payment is processed, webhook handles the data to prevent payment being made without data being saved. Snack Data field is created with the quantity and total previously selected and Stripe PID is also saved in order to guarantee that the user will not donate and have this information lost.


### Photos App

#### Photos Model

| Name | Key | Field Type | Validation |
| --- | ----------- |-----|---- |
| Photo Owner | owner | ForeignKey (UserProfile) |on_delete=models.SET_NULL,null=True, blank=True, related_name='photos'|
| Upload Date | upload_date | DateTimeField | N/A |
| Uploaded Photo | image | FileField | null=False, blank=False |

Login is required to upload photos. FileField is set as image in html unput, the idea is to let users to update videos in future versions of this project, also based on their Tiers. Upload Date was not set to auto_date and data is generated when form is submited (this is not the best practice, this was the first model created in the project and modification in this field was left to future improvement due to time constraints)

#### Tags Model

| Name | Key | Field Type | Validation |
| --- | ----------- |-----|---- |
| Tag Name | tag_name | CharField | max_length=100, null=True, blank=True |
| Tag Photos | tag_photos | ManyToManyField (Photos) | Photos |

Tags are created when users edit photos. Before form is submited, the site look for duplicates and only unique tags are stored. Each Tag Name can be linked to many Photos, as well as many Photos can be linked to Many tags. The relationship is set after Tag Names are added to the model.


---------------------------------------------------------------------------------------------------------------------------------------


# TESTING

## Testing User Stories

### As a user, I would like to create albums with the photos uploaded, so that I can organize my photos as I was making a physical album
### As a user, I would like to tag photos uploaded by categories, location and dates, so that I can categorize photos by tag

Users can upload one photo at a time, the photos can be tagged at this points, each tag has to be separated by the tag **@**

![image](https://user-images.githubusercontent.com/62474197/110618187-697beb00-818e-11eb-864a-12f7d542386c.png)

Once the photo is uploaded, the user is redirected to all photos page

![image](https://user-images.githubusercontent.com/62474197/110618616-d1323600-818e-11eb-9341-3fed824e7a35.png)


### As a user, I would like to untag photos, so that I can recategorize my photos and albums;

By hovering over the tags section of each photo, a edit icon will show up. When the user click in this icon, he/she are redirected to the edit page where tags can be edited.
Users can also delete photos from from this screen

![image](https://user-images.githubusercontent.com/62474197/110619854-389cb580-8190-11eb-9bbc-f46de556ec9a.png)


### As a user, I would like to view all my albums created, so that I can quick switch between albums

After uploading photos and tag them. By clicking in the Albums the user is redirected to the albums page and can see all unique tags converted in albums

![image](https://user-images.githubusercontent.com/62474197/110619220-71885a80-818f-11eb-83c1-6d13c18ba090.png)

By clicking in one of the albums cover, the user is redirected to the album created with a specific tag, photos are displayed in a carousel mode

![image](https://user-images.githubusercontent.com/62474197/110619629-ecea0c00-818f-11eb-8f64-46e956514a13.png)


### As a user, I would like to easliy remove photos from the webpage, so that I can control the photos that I have storaged in the webpage;

By hovering over each photo in all photos screen, a delete icon will show up. When the user click in this icon, he/she are redirected to the delete page where photos can be deleted

![image](https://user-images.githubusercontent.com/62474197/110620135-95986b80-8190-11eb-9dcc-90ee63044616.png)


### As a user, I would like to log in and log out, so that I can access my photos from any device;
### As a user, I would like to register for an account, so that I can save my details and upload my photos pravitely and storage photos in a different place than my phone/computer/camera memory;

Users can register an account and after login they will be able to storage their photos. Photos will be always available, unless they are deleted by the users.

![image](https://user-images.githubusercontent.com/62474197/110620618-1f483900-8191-11eb-97b0-631a2a42971c.png)


### As a new user, I would like to see how te website works without saving my photos or registering

Unless the user have an account registered and upload photos when they are logged in, photos and data will be deleted everytime the home page is loaded

![image](https://user-images.githubusercontent.com/62474197/110620908-80700c80-8191-11eb-9556-8b076b9ac7a9.png)


### User Authentication
#### As a user, I would like to recover my password in case I forget it, so that I can recover access to my account;
#### As a user, I would like to receive an email confirmation after registering, so that I can be assured that my contact is not being used by another user

Users can reset their password. A link will be sent to the registered email and the user will be redirected to a page to change their password

![image](https://user-images.githubusercontent.com/62474197/110621459-27ed3f00-8192-11eb-872c-2ca54f58ff87.png)

    
## Site Owner and Admin

### As a site owner, I would like to be able to maintain the page through donations and/or publicity adds.

A popup add appears (set to be every 15 seconds, asking users to make a donnation and help to maintain the page, after donation made, users will no longer see the popup message

![image](https://user-images.githubusercontent.com/62474197/110621708-713d8e80-8192-11eb-9774-80049df135c5.png)



## Manual Testing

All functionalities (links, scripts, forms where tested throughout the project development and with pass result)

### Base Template

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
|Logo nav link | Click | Render home page screen | Pass |
|Buy me a snack nav link | Click | Render buy snack page | Pass |
|Register nav link| Click | Render register page screen | Pass |
|Log in nav link | Click | Render Login page screen | Pass |


### My Photos App

#### All Photos Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
|Albums Link | Click | Render albums page screen | Pass |
|Upload Link | Click | Render upload page screen | Pass |
|Photos Thumbnail | Hover | Show delete photo icon | Pass |
|Delete photo icon | Click | Render delete page screen | Pass |
|Photos Tags Section | Hover | Show edit tags icon | Pass |
|Edit tags icon | Click | Render edit page screen | Pass |

#### Albums Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
|Photos Link | Click | Render photos page screen | Pass |
|Upload Link | Click | Render upload page screen | Pass |
|Photos Thumbnail | Click | Render tag albums page screen | Pass |

#### Edit Tags Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
|Cancel button | Click | Render photos page screen | Pass |
|Done button | Click | Render all photos page screen with edited tags | Pass |
|Photos Thumbnail | Click | Render tag albums page screen | Pass |

#### Delete Photos Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
|Cancel button | Click | Render photos page screen | Pass |
|Confirm button | Click | Delete photos and tags from database and render all photos page screen | Pass |

#### Delete Photos Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
| Upload button | Click | Load photos | Pass |
| Change photo link button | Click | Change photo uploaded | Pass |
| Cancel button | Click | Render photos page screen | Pass |
| Done button | Click | Upload photos and tags to database and render all photos page screen | Pass |

#### My Profile Screen

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
| Update button | Click | Change Nickname entered | Pass |


#### Choose Snack quantity

| Function | Action | Expected Result | Result |
| --- | ----------- |-----|---- |
| Options buttons | Click | Change quantity of snacks | Pass |
| Buy button | Click | Render buy me a snack form page | Pass |

#### Buy me a Snack

Form was tested in the project through test_forms.py in 'Subscription' app

---------------------------------------------------------------------------------------------------------------------------------------


# DEPLOYEMENT

The IDE platform used to develop this project was GitPod and GitHub used for version control. The project is hosted on the Heroku platform. To host Media and Static Files, it was used AWS S3 Bucket. Please find the steps followed to deploy this project.


## Heroku Deployment

### Basic steps in the terminal

  1.	Install gunicorn
  2.	Install psycog2-binary
  3.	Install dj-database-url
  4.	Add to requirements
  
    pip3 freeze –local > requirements.txt
  
  6.	Create a Procfile and add the command
  
    web: gunicorn tag_albums.wsgi:application

### Heroku Configuration

  1.  Create new app
  2.	Set Region (the most close to you)
  3.	Select Postgres as database in the Add-ons section
  4.	Go to settings and in Config Vars, add all necessary variables to access and run the app, for this project it was used the following keys (and its respective keys as values):
        
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    DATABASE_URL (Postgres)
    EMAIL_HOST_PASS
    EMAIL_HOST_USER
    SECRET_KEY
    STRIPE_PUBLIC_KEY
    STRIPE_SECRET_KEY
    STRIPE_WH_SECRET
    USE_AWS

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

## Stripe Keys
  1. To install stripe, type the commands
      
    pip3 install stripe
    
    pip3 freeze –local > requirements.txt
     
  2. More information about how to install and set up Stripe Keys and WebHooks can be found [here](https://stripe.com/docs/keys)
 
### Amazon Web Services (AWS)

To host media and static files in S3 Bucket in AWS:

  1.	Create an account in AWS
  2.	Create your S3 Bucket with public access
  3.	After completing configuration it will generate a AWS_ACCESS_KEY_ID and a AWS_SECRET_ACCESS_KEY, variables to be added in your Config Vars in Heroku. Also set USE_AWS key to True
  4.	The necessary variables need to be also added to settings in your app
  5.	More information in steps and documentation can be found [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)

### Email validation
 
  Gmail was used to validate new users in the platform. After creating an account in the website, the user will receive a link to validate.
  
  1. In settings in Gmail account, set up an app request
  2. An app password will be generated
  3. EMAIL_HOST_USER and EMAIL_HOST_PASS must be added to Config Vars in Heroku as well as in settings in your main app in the EDI
  4. Once configured, real emails can be sent.

## Cloning this repository

  1. To clone this repository, type the command
  
    git clone https://github.com/thiagoluizfb/tag_albums
  
  2. This can also be done via GitHub by clicking the green button Clone or download , then Download Zip button. Once the files are extracted, it can accessed by linking its location in your terminal directory.

---------------------------------------------------------------------------------------------------------------------------------------


# CREDITS

-   This ReadMe file was based on a sample available on [Code Institute Solutions repositories](https://github.com/Code-Institute-Solutions)

-   Quick information of "how to" was promplty found on [W3Schools](https://www.w3schools.com/)

-   To all tutors that helped me debugging challenging errors during the entire project

-   To all present in [Code Institute Slack Community](https://slack.com/), colaboration makes difference.


---------------------------------------------------------------------------------------------------------------------------------------- 

# AKNOWLEDGEMENTS

-   My Mentor for continuous helpful feedback.

-   Code Institute video classes with its helpful content.

-   My wife, Cristina, who supported me pantiently in the long hours spent coding
