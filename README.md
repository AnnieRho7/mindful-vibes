# Mindful Vibes

Mindful Vibes is a wellness blog focused on mental health, balance, and stress management. It provides a space for users to read articles on various wellness topics and interact by commenting on posts. The blog aims to foster a supportive community where users can engage in meaningful discussions about mental well-being.

## Live Site

A live version of the site can be found [here](https://mindful-vibes-4dd2a43e1ec5.herokuapp.com/)  
![Mindful Vibes Responsivness](readme-images/amirespon.png)

## User Experience - UX

[Back to the top](#top)

### User Stories

* As a website user, I can:
  1. View a paginated list of blog posts to choose which post to read.
  2. Click on a post to read the full text.
  3. Create and register an account to comment on posts.
  4. View comments on individual posts to read conversations.
  5. Access the About page to learn more about the site.
  6. Filter posts by categories that interest me.

* As an authenticated website user, I can:
  1. Comment on posts to engage in discussions.
  2. Modify or delete my comments.
  3. View comments on individual posts.

* As a website superuser, I can:
  1. View and manage comments on posts.
  2. Create draft posts to complete later.
  3. Update the About page content.
  4. Create, read, update, and delete posts.
  5. Approve or disapprove comments to filter inappropriate content.

### Agile Methodology

The Agile Methodology was used to plan this project, utilizing GitHub’s Project Board. You can view the project board [here](https://github.com/).

### The Scope

* To create a user-friendly, visually appealing wellness blog.
* To enable user interaction through commenting on posts.

## Design

[Back to the top](#top)

## Wireframes

[Back to the top](#top)

Wireframes were created to visualize the layout and user interface of Mindful Vibes. They outline the structure of key pages and the overall user experience.

### Homepage

The homepage wireframe shows the layout of the blog’s main page, including the blog post feed, navigation, and footer.

![Homepage Wireframe](documentation/images/wireframe-homepage.png)

### Post Details Page

This wireframe represents the layout for individual blog posts, including the content area, comments section, and related posts.

![Post Details Wireframe](documentation/images/wireframe-post-details.png)

### About Page

The About page wireframe illustrates how the information about the blog and its mission will be presented.

![About Page Wireframe](documentation/images/wireframe-about.png)

### Admin Dashboard

The admin dashboard wireframe depicts the layout for managing posts and comments, providing an interface for content moderation.

![Admin Dashboard Wireframe](documentation/images/wireframe-admin-dashboard.png)

## Wireframe Details

1. **Homepage**: Features a top navigation bar, a feed of recent blog posts, and a footer with contact information and social media links.
2. **Post Details Page**: Includes the blog post title, content, author information, and a comments section with the ability to add and view comments.
3. **About Page**: Contains details about the blog’s purpose, mission, and team, with a clean layout for easy reading.
4. **Admin Dashboard**: Provides tools for content management, including post creation, editing, deletion, and comment moderation.

The wireframes helped in defining the layout and functionality of the site, ensuring a user-friendly experience.

### Colours

Mindful Vibes uses a calming color palette to promote a sense of tranquility and relaxation. The primary colors are soft and neutral tones to ensure a soothing user experience. The color scheme includes.

### Media

* All images used on the site are sourced from [Pexels](https://www.pexels.com/).

### Database Diagram

![Database Diagram](documentation/images/database-diagram.png)

## Features

[Back to the top](#top)

### Homepage

* Displays the latest blog posts in a paginated view.

![Homepage](documentation/images/homepage.png)

### Navigation Desktop

* The navigation bar at the top of each page is consistent and sticky, adapting based on user authentication and role.

![Navigation Desktop](documentation/images/navbar-desktop.png)

### Navigation Mobile

![Navigation Mobile](documentation/images/navbar-mobile.png)

### Post Details

* Users can view and read individual posts. Authenticated users can also comment, which requires admin approval before display.

![Post Details](documentation/images/post-comment-apr.png)

### All Posts

* Access all posts through a paginated view by clicking the blog logo or home button.

### Categories

* Filter posts by categories via a dropdown menu in the navigation bar.

### Admin Backend

* Superusers or staff users manage posts and categories through the admin panel.

![Admin Backend](documentation/images/admin-panel.png)

### Possible Future Features

* User profile management and enhanced frontend admin functionality.
* Social login options for Facebook or Google.
* Password reset functionality for user accounts.

## Technologies

[Back to the top](#top)

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

### Django Packages Used

* [Gunicorn](https://gunicorn.org/) - WSGI server for Heroku
* [Cloudinary](https://cloudinary.com/) - For hosting static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/) - Parses database URL from Heroku environment variables
* [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL adapter for Python
* [Summernote](https://summernote.org/) - WYSIWYG text editor
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Authentication and account management
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Form styling
* [Whitenoise](http://whitenoise.evans.io/en/stable/) - For static files on Heroku

### Frameworks - Libraries - Programs Used

* [Bootstrap](https://getbootstrap.com/)
* [JQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Heroku](https://id.heroku.com)
* [ElephantSQL](https://www.elephantsql.com/)
* [VSCode](https://code.visualstudio.com/)
* [Fontawesome](https://fontawesome.com/)
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

## Development & Testing

[Back to the top](#top)

### Manual Testing

For an overview of the manual tests conducted during the development of this project, please refer to the [Manual Testing Document](manual_testing.md).


## Deployment

[Back to the top](#top)

### Heroku

The project was deployed via [Heroku](https://www.heroku.com/). The live link can be found [here](https://your-deployment-link-here.com).

To deploy:
* Log in to Heroku CLI and create a new app.
* Add PostgreSQL database and set environment variables.
* Configure static files with Cloudinary.
* Push code to Heroku and enable automatic deploys.

### Forking the GitHub repo

To fork the repository:
1. Log in to your GitHub account.
2. Navigate to the repository [here](https://github.com/your-username/your-repo).
3. Click the 'Fork' button in the top right corner.

### Cloning the repo with GitPod

1. Log in to GitHub.
2. Navigate to the repository [here](https://github.com/your-username/your-repo).
3. Click 'Code' and copy the URL.
4. Open a new workspace in GitPod and clone the repo.

### GitHub Desktop

1. Log in to GitHub.
2. Navigate to the repository [here](https://github.com/your-username/your-repo).
3. Select 'Open with GitHub Desktop'.

### Download and extract the zip directly from GitHub

1. Log in to GitHub.
2. Navigate to the repository [here](https://github.com/your-username/your-repo).
3. Select 'Download Zip' and extract it.

## Credits

[Back to the top](#top)

* The project was inspired by Code Institute's walkthrough and tutorials.
* Blog content is 
* Images are from [Pexels](https://pexels.com/):

* The Database Diagram was created using [dbdiagram.io](https://dbdiagram.io/).

## Acknowledgments

Thanks to [Code Institute](https://codeinstitute.net) for their resources and guidance.