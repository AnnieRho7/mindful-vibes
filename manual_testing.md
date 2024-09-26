# Manual Testing

[Go to README](README.md)

| Testcase                          | Expected Result                                                       | Test Result |
|-----------------------------------|-----------------------------------------------------------------------|-------------|
| Open the Homepage                 | Homepage loads with the correct template and featured blog posts      | ✅ PASS          |
| Register a user with valid data   | Request is successful, user is registered and logged in               | ✅ PASS          |
| Register a user with invalid data | Request fails, form loads again with data and errors                  | ✅ PASS          |
| Login a user with valid data      | Request is successful, user is logged in                              | ✅ PASS          |
| Login a user with invalid data    | Request fails, form loads again with data and errors                  | ✅ PASS          |
| View User Profile                 | User profile page loads with correct user information                 |        |
| Edit UserProfile with valid data  | Request is successful, user profile is updated, message is shown      | ✅ PASS          |
| Edit UserProfile with invalid data| Request fails, form loads again with data and errors                  |                   |
| Open a blog post                  | Blog post detail page loads with the correct template and data        | ✅ PASS          |
| Create a post with valid data     | Request is successful, blog post is created, and user is redirected   | ✅ PASS          |
| Create a post with invalid data   | Request fails, form loads again with data and errors                  |                  |
| Edit a blog post                  | Request is successful, blog post is updated, and user is redirected   | ✅ PASS          |
| Delete a blog post                | Request is successful, blog post is deleted, and user is redirected   | ✅ PASS          |
| **Commenting**                    |                                                                       |                   |
| Writing a comment                 | Request is successful, comment is added to the list, message is shown | ✅ PASS          |
| Editing a comment                 | Request is successful, comment content is edited, message is shown    | ✅ PASS          |
| Delete a comment                  | Request is successful, comment is deleted, message is shown           | ✅ PASS          |
| **Unauthorised requests**         |                                                                       |                   |
| Liking an post                    | User must be logged in to like a post                                 | ✅ PASS          |
| Writing a comment                 | User must be logged in to write a comment                             | ✅ PASS          |
| Editing a comment                 | User must be logged in to edit a comment                              | ✅ PASS          |
| Delete a comment                  | User must be logged in to ldelete a post                              | ✅ PASS          |
| View profile                      | User must be logged in to view a profile page                         | ✅ PASS          |
| Edit Profile page                 | User must be logged in to edit their profile page                     | ✅ PASS          |