# Manual Testing Documentation

[Go to README](README.md)

## Form Validation Testing

### User Profile Form
| Test Case | Input | Expected Result | Actual Result | Status |
|-----------|-------|-----------------|---------------|---------|
| First Name with Numbers | "John123" | Form shows error message | Form validation prevents submission | ✅ PASS |
| Last Name with Special Characters | "Smith#@" | Form shows error message | Form validation prevents submission | ✅ PASS |
| Bio exceeding character limit | [Text > 500 chars] | Form shows character limit error | Form shows validation message | ✅ PASS |

### Post Form Testing
| Test Case | Steps | Expected Result | Actual Result | Status |
|-----------|-------|-----------------|---------------|---------|
| Title Length | Enter 2-character title | Show error: "Title must be at least 3 characters long" | Shows error | ✅ PASS |
| Empty Title | Submit with no title | Show error: "Title must be at least 3 characters long" | Shows error | ✅ PASS |
| Invalid Slug | Enter "my blog!" | Show error: "Please use only letters, numbers, underscores or hyphens" | Shows error | ✅ PASS |
| Empty Content | Submit with no content | Show error: "Please fill out this form" | Shows error | ✅ PASS |
| Short Content | Enter 5-character content | Show error: "Content must be at least 10 characters long" | Shows error | ✅ PASS |

### Comment Form Testing
| Test Case | Steps | Expected Result | Actual Result | Status |
|-----------|-------|-----------------|---------------|---------|
| Empty Comment | Submit empty comment | Show error: "Please fill out this form" | Shows error | ✅ PASS |
| Short Comment | Enter 1-character comment | Show error: "Comment must be at least 2 characters long" | Shows error | ✅ PASS |
| Long Comment | Enter >1000 character comment | Show error: "Comment cannot be longer than 1000 characters" | Shows error | ✅ PASS |

## User Story Testing

### Visitor User Stories
| User Story | Test Steps | Expected Result | Status |
|------------|------------|-----------------|---------|
| "As a website user, I can view a paginated list of posts" | 1. Navigate to blog page<br>2. Scroll through posts<br>3. Click pagination | Posts display in pages of 6 | ✅ PASS |
| "As a website user, I can click on a post" | 1. Visit blog page<br>2. Click post title | Full post content displays | ✅ PASS |
| "As a website user, I can register an account" | 1. Click Register<br>2. Fill form<br>3. Submit | Account created successfully | ✅ PASS |

### Authenticated User Stories
| User Story | Test Steps | Expected Result | Status |
|------------|------------|-----------------|---------|
| "As an authenticated user, I can comment on posts" | 1. Log in<br>2. View post<br>3. Add comment | Comment awaits approval | ✅ PASS |
| "As an authenticated user, I can create posts" | 1. Log in<br>2. Create post<br>3. Submit | Post awaits approval | ✅ PASS |

### Admin User Stories
| User Story | Test Steps | Expected Result | Status |
|------------|------------|-----------------|---------|
| "As a superuser, I can approve comments" | 1. Access admin<br>2. Approve comment | Comment appears on post | ✅ PASS |
| "As a superuser, I can manage posts" | 1. Access admin<br>2. Edit/delete posts | Changes reflect on site | ✅ PASS |

## Unauthorized Access Testing
| Test Case | Steps | Expected Result | Status |
|-----------|-------|-----------------|---------|
| Admin Area (Regular User) | Access admin URL | Asked to login | ✅ PASS |
