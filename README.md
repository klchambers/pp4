![RecipeMe Logo](documentation/recipeme-logo.png)

**Table of contents:**

- [Introduction](#introduction)
- [Deployed Site](#deployed-site)
- [User Experience](#user-experience)
  - [Design](#design)
  - [Workflow Logic Charts](#workflow-logic-charts)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owner's Goals](#site-owners-goals)
- [Features](#features)
  - [Data Model](#data-model)
  - [Further Development and Future Features](#further-development-and-future-features)
- [Testing and Validation](#testing-and-validation)
  - [W3C HTML and CSS Validation](#w3c-html-and-css-validation)
  - [JSHint Code Analysis](#jshint-code-analysis)
  - [Manual Testing Methodology](#manual-testing-methodology)
  - [Bugs and Challenges](#bugs-and-challenges)
  - [Development](#development)
  - [Contributing](#contributing)
  - [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Acknowledgements](#acknowledgements)

<a id=introduction></a>

## Introduction

![Recipe Responsiveness Mockup](/documentation/responsiveness-mockup.png)

RecipeMe is designed to be a user-friendly, responsive, and social recipe-sharing site.

Recipes are shown on the homepage in a chronological order (newest first) so that return users can see the latest recipes posted.

Logged-in users can submit a recipe to be published, and leave comments on existing recipes. 

<a id=deployed-site></a>

## Deployed Site

The program has been deployed to Heroku and can be accessed [here](https://pp4assignment-81282f23e92d.herokuapp.com/).

<a id=user-experience></a>

## User Experience

<a id=design></a>

### Design

#### Colour
RecipeMe is designed to have a simple user interface and a minimalist colour palette to provide a distraction-free experience to the user, allowing them to focus on browsing, commenting, and reading recipes and viewing images.

The background is an off-white shade (#f0f0f0), chosen to be slightly less intense than pure white, with accents in a distinctive shade of orange ![Placeholder image for colour block](https://placehold.co/15/d28b49/png) to draw the users attention with these elemenst.

#### Typography

Default Bootstrap sans serif typefaces were used throughout the site for their legibility across devices, screen/font sizes, with the exception of the RecipeMe logo in the page headers. For this, the serif font [Merriweather](https://fonts.google.com/specimen/Merriweather) by [Sorkin Type](https://fonts.google.com/?query=Sorkin+Type) was chosen from Google Fonts as it is easily legible while distinct enough to establish an identity for the site.

<a id="workflow-logic-charts"></a>

### Workflow Logic Chart
As shown in the workflow logic chart below, the actions permitted to users vary depending on the user permissions and whether or not they are logged in.

Superusers can access the Django admin panel and approve comments & recipes, as well as create new superusers and carry out other site administraion tasks.

Any site visitor can use the basic functionality of the site (e.g. view recipes and approved comments, register for an account, or view the about page).

Only users who are logged in are able to leave comments or submit recipes, and these must be approved by site administrators before being visible to all, in order to prevent spam or other unsuitable content from being posted to the site.

![Application database schematic](documentation/pp4-logic.png)

<a id=user-goals></a>

### User Goals

* I would like to find recipes with ingredients and instructions listed in a way that is easy to read

* I would like to leave comments and feedback to recipe authors

* I would like to submit my own recipes to be posted

<a id=user-stories></a>

### User Stories

#### As a user I can register for an account so that I can access user-only features

* Acceptance criteria 1: Registering for an account should be straightforward, and I should be able to create a username and password with my email address

* Acceptance criteria 2: With an account I should be able to log in

* Acceptance criteria 3: Data that I create and submit to the site should be saved and accessible by me the next time that I log in

#### As a Site Admin I can create, read, update and delete recipes so that I can manage the site's content

* Acceptance Criteria 1: Users logged in a a Site Administrator can create recipes

* Acceptance Criteria 2: Users logged in a a Site Administrator can view recipes

* Acceptance Criteria 3: Users logged in a a Site Administrator can edit recipes

* Acceptance Criteria 4: Users logged in a a Site Administrator can delete recipes

#### As a user I can create a recipe so that I can share it with other site users.

* Acceptance Criteria 1: Option to save a draft so as not to lose progress

* Acceptance Criteria 2: Upload my recipe with an ingredients section, cooking instructions, and photo

* Acceptance Criteria 3: Be able to edit or delete my existing recipes

* Acceptance Criteria 4:  Recipes should be approved by a site administrator before being published

#### As a user I want to comment on a recipe to leave feedback and recommendations to other users

* Acceptance Criteria 1: Comments should include an automatically created 'date created' (and 'date edited', if applicable) field

* Acceptance Criteria 2: Comments should have CRUD (Create, Read, Update, Delete) functionality

* Acceptance Criteria 3: Comments should first be approved by a site administrator before being made public, in order to prevent spam or irrelevant links from being posted to the site

#### As a user I would like to view a list of posted recipes so that I can see and choose posted recipes to interact with.

* Acceptance Criteria 1: Given more than one post is in the database, these multiple posts are listed.

* Acceptance Criteria 2: When a user opens the main page a list of posts is seen

* Acceptance Criteria 3: Then the user sees all post titles with pagination to choose what to read

#### As a user I would like to open a recipe from the homepage so that I can read the ingredients, method, and interact with it

* Acceptance Criteria 1: When a recipe link is clicked on the homepage the relevant recipe page should open

* Acceptance Criteria 2: The resulting page should be laid out in an intuitive, navigable style

#### As a user I would like to visit an 'About' page in order to learn more about the site

* Acceptance Criteria 1: The About page should contain relevant and up to date information
* Acceptance Criteria 2: The page should be easily accessible with a link in the nav bar

#### As a Site Administrator I would like to add and update information on an 'About' page in order to inform visitors of the site and its purpose

* Acceptance Criteria 1: I should be able to add and update information on the about page through Django's admin panel

#### As a user I want to be able to upload images with my recipe to provide readers with a visual representation of the dish

* Acceptance Criteria 1: Images should be stored persistently

* Acceptance Criteria 2: I should be able to submit images in common, expected image file formats

<a id=site-owners-goals></a>

### Site Owner's Goals

* I need to approve comments and recipes before they are posted and made visible to all users

* I would like to manage recipes, ctegories, and ingredients through Django's administration panel

* I would like to be easily update the site's 'About' page to keep visitors informed of the site and its purpose

<a id=features></a>

## Features

A logged out user has a number of options available to them from the homepage. From the navbar menu, they can click on a recipe to see the full recipe and instructions, register for an account, log in, or view the 'About' page.

![Logged out homepage screenshot](/documentation/pp4_screenshots/homepage-logged-out.png)

When a registered user selects 'Login' and correctly enters their username and password, a message pops up confirming their login, and the elements in the navbar change. A 'Hello, *User*' message indicates that the user is logged in and indicates the username that they are logged in with. From the navbar, they can now choose to Submit a Recipe, or Logout


![Logged in successfully screenshot](/documentation/pp4_screenshots/homepage-logged-in.png)

The app's sign in page is the Django AllAuth signin page with custom styling. Registered users can sign in with their username and password, and have the option to choose 'remember me' to streamline their experience on subsequent visits.

![signin page screenshot](/documentation/pp4_screenshots/signin.png)

By clicking on a recipe, a user can see a comment count (clicking the comment count icon skips the user to comments on all screen sizes), with the ingredients below the Total Cooking time. A user-uploaded image is prominently displayed, or a placeholder image if no image is provided. On the right hand side of the screen are instructions, with the comments below. The comment text field invites the user to log in to comment, if they are not logged in. 

![recipe_page.html screenshot](/documentation/pp4_screenshots/recipe_page.png)

On mobile-sized devices, the page content is displayed to the user in one column instead of two. Here, the comment count link is particularly helpful in allowing the user to skip to this content instead of scrolling through long recipes.

![recipe_page.html mobile screenshot](/documentation/pp4_screenshots/recipe_page-mobile.png)

When a logged in user posts a comment, it is pending approval by a site administrator. A message indicates this to the user, and is not displayed when the comment gets approved. This comment is not viewable by anyone but its author on the recipe page until the comment is approved.

The below screenshot illustrates the functionality of the 'edit' button. The user is taken down to the comment field, and the text field is prepopulated with the comment to edit, with the button text updated to read 'Update'. In this screenshot, the user is using the 'edit' comment functionality to correct typos in their message.

![Edit comment field screenshot](/documentation/pp4_screenshots/edit-comment.png)

After making their changes and pressing 'Update', a message is printed on screen to inform the user that their edit has been made successfully. All edits revert approved comments to unapproved to prevent the posting of spam.

![Comment edit confirmation screenshot](/documentation/pp4_screenshots/comment-edited.png)

When a user presses the button to delete their comment, they are asked to confirm this choice via a modal displayed on screen. The 'Delete' button to confirm deletion is displayed in red.

![Comment deletion modal screenshot](/documentation/pp4_screenshots/delete-comment.png)

![Comment deletion modal mobile screenshot](/documentation/pp4_screenshots/comment-delete-modal.png)

Choosing 'Submit a Recipe' in the navbar takes the user to a form to provide a title, ingredients, ingredient quantities, and instructions to be posted. Upon successful input of valid data, the user is presented with the below message.

![Recipe submission message screenshot](/documentation/pp4_screenshots/recipe-submitted.png)

Once a recipe is successfully submitted the data will be available to site admins and superusers in the Django Administration panel. This method allows site admins to confirm the validity and authenticity of recipes, and make any necessary formatting changes or edits before publishing.

![approving/publishing recipe screenshot](/documentation/pp4_screenshots/recipe-submissionapproval.png)

The About page features a prominent image on the right hand side of the screen with data from the 'About' model displayed on the left. An 'updated on' field automatically updates when this data is changed and lets visitors know how recently this data was posted or edited.

![about.html screenshot](/documentation/pp4_screenshots/about.png)

<a id=data-model></a>

### Data Model

![Application database schematic](documentation/database_schema.png)

A brief description of the entities in the above schematic diagram:

* **User:** Represents a user of the platform who can share recipes, comment on recipes, and favourite recipes.

* **Recipe** Represents a recipe shared by a user. It includes details like title, description, ingredients, directions, etc.

* **RecipeCategory:** Represents a cuisine, category, or type of recipe e.g. ‘Italian’, ‘vegetarian’, or ‘simple’. A Many-to-Many relationship i.e. recipes can be assigned to a number of different categories. In order to maintain valid, appropriate categories, they are added to recipes by site administrators through the Django admin panel.

* **Comment:** Represents a comment made by a user on a recipe, has a One-to-One relationship with the Recipe entity and includes comment_text and a date_created attribute.

* **Ingredient:** Representing an ingredient. Can be added by the user via the 'Submit a Recipe' form or through the Django administration panel.

* **IngredientQuantity:** This model facilitates the management of ingredient quantities within recipes, forming a link between specific recipes and their ingredients with respective amounts.


<a id=further-development-and-future-features></a>

### Further Development and Future Features

Ideas for future development of RecipeMe include the following:

* Export recipes in PDF format for easy sharing/printing

* URL share buttons/Share on social media buttons to share recipes with friends and family across a range of social media networks

* 'Favourites': Create a 'favourite' or 'like' button which increments with clicks from logged in users to indicate popular recipes

* User profiles: Create user profile pages displaying posted recipes & comments, favourited recipes, and a bio and profile photograph to increase the social aspect of the site

<a id=testing-and-validation></a>

## Testing and Validation

<a id=w3c-html-and-css-validation></a>

### W3C HTML and CSS Validation

#### HTML

HTML validation of individual pages can be viewed in the drop down boxes below:

<details>
<summary>Homepage</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/homepage-html-Validation.png'>
</details>

<details>
<summary>Recipe Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/recipe_page-validation.png'>
</details>

<details>
<summary>About Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/about.html-validation.png'>
</details>

<details>
<summary>Submit Recipe Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/recipe_upload-validation.png'>
</details>

<details>
<summary>Login Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/signin-validation.png'>
</details>

<details>
<summary>Logout Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/logout-validation.png'>
</details>

<details>
<summary>Signup Page</summary>
<br>
<img src='./documentation/validation_screenshots/html-validation-screenshots/signup-validation.png'>
<br>
<p>Some errors were presented when the rendered HTML from this page was passed into W3C's HTML text input validator. In the HTML pasted from the page source (shown below), the Span tag and P tag from Django Allauth appear to raise errors, but on manual inspection no errors were found, and the page functions as expected.
<img src='./documentation/validation_screenshots/html-validation-screenshots/signup-html.png'>
</details>

#### CSS

RecipeMe's CSS passed the validation with no errors. Some warnings were presented, relating to styles applied through the use of Bootstrap CSS. The CSS validation results can be viewed [here](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fpp4assignment-81282f23e92d.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1).


<a id=jshint-code-analysis></a>

### JSHint Code Analysis

script.js passed through the JSHint Code Analysis tool with no errors reported. The full screenshot can be viewed in the dropdown menu below.

<details>
<summary>JSHint Code Analysis Screenshot</summary>
<br>
<img src='./documentation/validation_screenshots/script.js-validation.png'>
</details>


<a id=manual-testing-methodology></a>

### Manual Testing Methodology

#### Manual Testing Methodology for Django Models

| Test Case ID | Model | Test Case Description| Steps to Perform| Expected Result|
|--------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| 1        | Category           | Verify that a category can be created with a unique name                                                                                                | 1. Create a category with a unique name.                                                                         | Category is created successfully                                                                |
| 2        | Category           | Verify that creating a category with a duplicate name fails                                                                                             | 1. Create a category with an existing name.                                                                      | Error is raised indicating the name must be unique                                              |
| 3        | Category           | Verify that categories are retained when the creating user is deleted                                                                                   | 1. Create a user. 2. Create a category with this user. 3. Delete the user.                                       | Category is retained with `created_by` set to null                                              |
| 4        | Ingredient         | Verify that an ingredient can be created with a unique name                                                                                             | 1. Create an ingredient with a unique name.                                                                      | Ingredient is created successfully                                                              |
| 5        | Ingredient         | Verify that creating an ingredient with a duplicate name fails                                                                                          | 1. Create an ingredient with an existing name.                                                                   | Error is raised indicating the name must be unique                                              |
| 6        | Recipe             | Verify that a recipe can be created with a unique title                                                                                                 | 1. Create a recipe with a unique title.                                                                          | Recipe is created successfully                                                                  |
| 7        | Recipe             | Verify that creating a recipe with a duplicate title fails                                                                                              | 1. Create a recipe with an existing title.                                                                       | Error is raised indicating the title must be unique                                             |
| 8        | Recipe             | Verify that the slug field is automatically generated based on the title                                                                                | 1. Create a recipe with a specific title.                                                                        | Slug is generated based on the title                                                            |
| 9        | Recipe             | Verify that the recipe can have multiple categories                                                                                                     | 1. Create multiple categories. 2. Assign these categories to a recipe.                                           | Recipe is associated with multiple categories                                                   |
| 10        | Recipe             | Verify the default status of a new recipe is 'Draft'                                                                                                    | 1. Create a new recipe.                                                                                          | Recipe status is set to 'Draft'                                                                 |
| 11        | Recipe             | Verify the total cook time can be entered in HH:MM:SS format                                                                                            | 1. Create a recipe with a specific cook time in HH:MM:SS format.                                                 | Total cook time is saved correctly                                                             |
| 12        | Recipe             | Verify the instructions field can handle multiline text                                                                                                 | 1. Enter multiline instructions while creating a recipe.                                                        | Instructions are saved and displayed correctly                                                  |
| 13        | Recipe             | Verify the created_on field is automatically populated with the current date and time                                                                   | 1. Create a new recipe.                                                                                          | created_on field is populated with the current date and time                                    |
| 14        | IngredientQuantity | Verify that an IngredientQuantity can link an ingredient and a recipe                                                                                   | 1. Create an ingredient. 2. Create a recipe. 3. Create an IngredientQuantity linking the ingredient and recipe. | IngredientQuantity is created successfully                                                      |
| 15        | IngredientQuantity | Verify the quantity field in IngredientQuantity accepts valid data                                                                                      | 1. Create an IngredientQuantity with a specific quantity.                                                        | Quantity is saved correctly                                                                    |
| 16        | Comment            | Verify that a comment can be created for a recipe                                                                                                       | 1. Create a recipe. 2. Add a comment to the recipe.                                                              | Comment is created and linked to the recipe                                                     |
| 17        | Comment            | Verify the default status of a new comment is 'not approved'                                                                                            | 1. Create a new comment for a recipe.                                                                            | Comment is created with approved status set to 'False'                                          |
| 18        | Comment            | Verify that only approved comments are counted in the comment_count property of a recipe                                                               | 1. Add approved and unapproved comments to a recipe.                                                             | comment_count returns the count of only approved comments                                       |
| 19        | Comment            | Verify that the created_on field in Comment is automatically populated with the current date and time                                                   | 1. Create a new comment.                                                                                         | created_on field is populated with the current date and time                                    |
| 20        | Recipe             | Verify the ordering of recipes is by created_on date in descending order (newest first)                                                                 | 1. Create multiple recipes with different created_on dates.                                                      | Recipes are ordered by created_on date in descending order                                      |

#### Manual Testing Methodology for `base.html`

| Test Case ID | Section         | Test Case Description                                             | Steps to Perform                                                                                          | Expected Result                                                                                 |
|--------------|-----------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| 21        | Page Structure  | Verify the base structure of the HTML document                    | 1. Open any page that extends `base.html`.                                                                | The structure includes correct DOCTYPE, head, and body elements.                               |
| 22        | Head Title      | Verify the title block is rendered correctly                      | 1. Set a title in a child template.                                                                       | The title is displayed correctly in the browser tab.                                           |
| 23        | Extra Head      | Verify the `extra_head` block is rendered correctly               | 1. Add content to the `extra_head` block in a child template.                                             | The content is included within the head section of the HTML document.                          |
| 24        | Messages        | Verify that user messages are displayed correctly                 | 1. Trigger messages in the application (e.g., form validation errors).                                    | Messages are displayed in a list format at the top of the page.                                |
| 25        | Menu Display    | Verify that the menu changes based on user authentication state   | 1. Log in as a user. 2. Check the menu. 3. Log out. 4. Check the menu again.                              | The menu displays "Change Email" and "Sign Out" for authenticated users and "Sign In" and "Sign Up" for unauthenticated users. |
| 26        | Content Block   | Verify the `content` block is rendered correctly                  | 1. Add content to the `content` block in a child template.                                                | The content is displayed correctly within the body of the HTML document.                       |

#### Manual Testing Methodology for `recipe_page.html`

| Test Case ID | Section            | Test Case Description                                                                                                    | Steps to Perform                                                                                          | Expected Result                                                                                 |
|--------------|--------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| 27        | Image Display      | Verify the placeholder image is shown when no featured image is provided                                                 | 1. Create a recipe without a featured image.                                                              | Placeholder image is displayed.                                                                 |
| 28        | Image Display      | Verify the featured image is shown when provided                                                                         | 1. Create a recipe with a featured image.                                                                 | Featured image is displayed.                                                                    |
| 29        | Title Display      | Verify the recipe title is displayed correctly                                                                           | 1. Create a recipe with a specific title.                                                                 | Recipe title is displayed correctly.                                                            |
| 30        | Comment Count      | Verify the comment count link works correctly                                                                            | 1. Create a recipe with comments. 2. View the recipe page. 3. Click the comment count link.               | Page scrolls to the comments section.                                                           |
| 31        | Delete Recipe      | Verify the delete button for a recipe works correctly when user is the author                                            | 1. Create a recipe. 2. Log in as the author. 3. Click the delete button.                                   | Recipe is deleted and user is redirected to the appropriate page.                               |
| 32        | Cooking Time       | Verify the total cooking time is displayed correctly                                                                     | 1. Create a recipe with a specified cooking time.                                                         | Total cooking time is displayed in the format HH:MM:SS.                                        |
| 33        | Category Display   | Verify that multiple categories are displayed correctly                                                                  | 1. Create categories. 2. Create a recipe with multiple categories.                                        | All categories are displayed, separated by commas.                                             |
| 34        | Single Category    | Verify that a single category is displayed correctly                                                                     | 1. Create a category. 2. Create a recipe with a single category.                                          | The category is displayed correctly.                                                            |
| 35        | Author and Date    | Verify the author and created date are displayed correctly                                                               | 1. Create a recipe. 2. View the recipe page.                                                              | Author name and creation date are displayed correctly.                                          |
| 36        | Ingredients List   | Verify the list of ingredients and their quantities are displayed correctly                                              | 1. Create a recipe with ingredients and quantities.                                                       | Ingredients and quantities are displayed correctly.                                             |
| 37        | Method Display     | Verify the method (instructions) are displayed correctly                                                                 | 1. Create a recipe with instructions.                                                                     | Instructions are displayed with correct formatting.                                             |
| 38        | Comments Display   | Verify comments are displayed correctly and can be added by authenticated users                                          | 1. Create a recipe. 2. Add comments to the recipe. 3. Log in as a user. 4. Add a comment.                 | Comments are displayed correctly, and new comments can be added by authenticated users.         |
| 39        | Comment Approval   | Verify unapproved comments are displayed correctly to their authors and hidden from others                               | 1. Add a comment to a recipe as a user. 2. Check the comment visibility while logged in and logged out.   | Unapproved comments are visible to their authors and hidden from others.                        |
| 40        | Comment Actions    | Verify authenticated users can delete or edit their comments                                                             | 1. Add a comment as a user. 2. Log in as the same user. 3. Attempt to delete and edit the comment.        | User can delete or edit their own comments.                                                     |
| 41        | Delete Confirmation| Verify the delete confirmation modal for comments and recipes works correctly                                            | 1. Attempt to delete a comment or recipe.                                                                 | Confirmation modal appears asking for deletion confirmation.                                    |
| 42        | Leave Comment      | Verify that only authenticated users can leave comments                                                                  | 1. Log out. 2. Attempt to leave a comment on a recipe. 3. Log in. 4. Attempt to leave a comment again.    | Comment form is only available to authenticated users.                                          |


<a id=bugs-and-challenges></a>

### Bugs and Challenges

There are no known bugs in the current Heroku deployment of RecipeMe, following comprehensive and thorough testing of the site and it's features.

During development, the following bugs were identified which have since been amended:

* In an early deployment of the app, ingredient quantities were attributes of the Ingredient model. This resulted in it being impossible to have the same ingredient with different quantity amounts in more than one recipe. This was solved by creating an intermediate model (`IngredientQuantity`) which has a `CharField` named 'quantity', and links to both the `Ingredient` and the `Recipe` models via ForeignKeys

* Due to limitations of a Postgres service used, the `DATABASE_URL` variable stored in env.py was updated to a new [Neon](https://neon.tech/) database. This change was not immediately reflected in Heroku's Config Vars, resulting in server 500 errors and the application failing to load in the Heroku deployment. This was resolved by updated the DATABASE_URL configuration variable in the Heroku app settings. 

<a id=development-and-deployment></a>

## Development and Deployment

<a id=development></a>

### Development

Development was started by cloning Code Institute's project template (available [here](https://github.com/Code-Institute-Org/ci-full-template)), and development was carried out in VSCode with changes pushed to GitHub.

<a id=contributing></a>

### Contributing

To contribute, make a pull request from the [project repository](https://github.com/klchambers/pp4). When merged, any changes will be reflected following the next Heroku deployment of the project.
<a id=deployment></a>

### Deployment

#### Prerequisites
* Heroku Account: Ensure you have an active Heroku account. You can sign up at Heroku.
* Heroku CLI: Install the Heroku Command Line Interface (CLI) on your local machine. Instructions for installation can be found here.
* Git: Ensure Git is installed and configured on your local machine. Instructions for installation can be found here.
* PostgreSQL Database: The application uses a PostgreSQL database. You can use Heroku's PostgreSQL add-on or an external provider like Neon.

#### Steps to Deploy

1. Clone the Repository

`git clone https://github.com/klchambers/pp4.git`

`cd pp4`

2. Create a Virtual Environment and Install Dependencies

`python -m venv venv`

`source venv/bin/activate`, or on Windows use `venv\Scripts\activate`

`pip install -r requirements.txt`

3. Set Up Environment Variables

Create an env.py file in the root directory and add the following environment variables:

`import os`

`os.environ.setdefault('DATABASE_URL', <your_database_url>)`

`os.environ.setdefault('SECRET_KEY', <your_database_url>)`

(note: Add .env.py/env.py to .gitignore and save before pushing your code to Github. This will prevent sensitive information from being made publicly available)

In the project's settings.py file, import your database URL and secret key:

`if os.path.isfile('env.py'):
    import env`

`SECRET_KEY = os.environ.get('SECRET_KEY')`

Add `.herokuapp.com` to ALLOWED_HOSTS

4. Prepare Static Assets

`python manage.py collectstatic`

5. Initialize a Git Repository

`git init`

`git add .`

`git commit -m "Initial commit"`

6. Create a Heroku App

`heroku create recipeme-app`

7. Deploy to Heroku

`git push heroku main`

8. Apply DB migrations

`python3 manage.py makemigrations`

`python3 manage.py migrate`

9. Create a Superuser

`python manage.py createsuperuser`

Follow the instructions in your terminal to create your superuser account username and passwords

10. Open the application

`heroku open`

<a id=technologies-used></a>

## Technologies Used

* [**Django**](https://www.djangoproject.com): Python framework for templating, URL routing, admin interface, and more
* [**Visual Studio Code**](https://code.visualstudio.com/): Text editor for development
* [**Heroku**](https://www.heroku.com): Live deployment of web app
* [**Neon**](https://www.neon.tech): Serverless open-source alternative to ElephantSQL
* [**Gunicorn**](https://www.gunicorn.org): Python WSGI HTTP Server for UNIX
* [**Psycopg**](https://pypi.org/project/psycopg2/): PostgreSQL database adapter for Python
* [**Django Allauth**](https://docs.allauth.org/en/latest/): Integrated set of Django applications addressing authentication, registration, and account management
* [**Summernote**](https://summernote.org/): Bootstrap WYSIWYG Editor
* [**Whitenoise**](https://whitenoise.readthedocs.io/en/latest/): Static file serving for Python web apps
* [**Crispy Forms**](https://django-crispy-forms.readthedocs.io/en/latest/): Django form styling
* [**Lucidchart**](https://www.lucidchart.com/pages/): Creation of diagram schema and Entity Relationship Diagrams
* [**DBDiagram.io**](https://dbdiagram.io/): Database Relationship Diagrams design tool

<a id=acknowledgements></a>

## Acknowledgements

* Use of Slugify to generate and save slugs adapted from code posted by [Ikechukwu Henry Odoh](https://stackoverflow.com/users/2261257/ikechukwu-henry-odoh) in [this](https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4) Stack Overflow thread
* Code to register ModelAdmin classes and configure list views in recipes/admin.py adapted from [MDN Web Docs: *Django Tutorial Part 4: Django admin site*](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
* Use of InlineFormSet and inlineformset_factory adapted from code published here: [Django Documentation: *Creating forms from models*](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/)
* [Placeholder image](https://unsplash.com/photos/person-cutting-vegetables-with-knife-yWG-ndhxvqY) by [Alyson McPhee](https://unsplash.com/@alyson_jane) on Unsplash
* [Image](https://pixabay.com/photos/spices-kitchen-ingredients-flavor-4185324/) used on about.html was posted by [Matej Madar](https://pixabay.com/photos/spices-kitchen-ingredients-flavor-4185324/) on Pixabay
* Favicons generated using [favicon.io](https://favicon.io)
* Font family [Merriweather](https://fonts.google.com/specimen/Merriweather/about) by [Sorkin Type](https://fonts.google.com/?query=Sorkin+Type) was sourced from Google Fonts for page headers
* Images used in recipes generated using DeepAI's image generator available [here](https://deepai.org/machine-learning-model/text2img)
* Recipes adapted from recipes posted at [BBC Goodfood](https://www.bbcgoodfood.com)