### Test 1: Validate Token – Unauthorized (500)
- **Method:** GET /me  
- **Auth:** Bearer Token (expired)  
- **Response:** 500 Internal Server Error  
- **Screenshot:** `screenshots/postman_me_500.png`

---

### Test 2: Validate Token – Authorized (200)
- **Method:** GET /me  
- **Auth:** Bearer Token (valid)  
- **Response:** 200 OK  
- **Screenshot:** `screenshots/postman_me_200.png`

---

### Test 3: Update User Record (Admin)
- **Method:** PATCH /admin/users/51  
- **Params:** email, first_name, last_name, username, property, user_id  
- **Response:** 200 OK → “User updated successfully”  
- **Screenshot:** `screenshots/postman_patch_user_200.png`