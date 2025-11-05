```markdown
# Xano ↔ Wix/Velo User Management APIs (Auth, RBAC, CRUD)

This showcase documents a small backend built with **Xano** and consumed from a **Wix/Velo** front end. It demonstrates:
- **JWT authentication** and `Authorization: Bearer <token>` usage
- **Role-based access control (RBAC)** for admin routes
- **RESTful CRUD** on users (GET/POST/PATCH/DELETE)
- **Practical diagnostics** with **Postman** (status codes, headers, JSON bodies)

> Relevance: mirrors the troubleshooting flow used in real-time support—verify auth, reproduce API calls, inspect response codes/payloads, and correlate app behavior with backend state.

---

## Architecture (high level)

**Client (Wix/Velo JS)** → `fetch()` → **Xano REST Endpoints** → DB  
- Client stores JWT after `/login` and includes it in headers for protected routes.
- Admin-only operations are guarded both **client-side** (role checks) and **server-side** (JWT claims).

---

## Key Endpoints (examples)

| Method | Path                       | Purpose                              |
|-------:|----------------------------|--------------------------------------|
| POST   | `/login`                   | Authenticate, return JWT, role       | 
| GET    | `/me`                      | Validate token, return user profile  |
| GET    | `/admin/users`             | List all users (admin)               |
| POST   | `/admin/users`             | Create user (admin)                  |
| PATCH  | `/admin/users/{user_id}`   | Update user (admin)                  |
| DELETE | `/admin/users/{user_id}`   | Delete user (admin)                  |

**Common status codes:**  
`200 OK`, `201 Created`, `401 Unauthorized` (missing/invalid token), `403 Forbidden` (role not sufficient), `404 Not Found`, `422/400` (validation).

---

## Front-End Snippets (Wix/Velo)

Minimal, redacted examples live in `frontend-wix/`:

- **`login.js`** – `performLogin(email, password)`  
  - POST `/login`, parse JSON, store `authToken` (e.g., `localStorage`), redirect on success.
- **`signup.js`** – `createAccount(email, password, name)`  
  - POST `/create_account` (or your named route), handle validation errors.
- **`admin_panel.js`** – `loadUsers()`, `addUser()`, `deleteUser(id)`  
  - Uses `Authorization: Bearer <token>` header for admin routes.

> These snippets are shortened from the original code to highlight request/response shape, headers, and error handling.

---

## Postman Diagnostics

See `client-tests/postman_notes.md` for transcribed requests and annotated screenshots:

- **/me 500 (Invalid or Expired Token)** — Demonstrates handling of authentication errors and token validation issues.  
- **/me 200 (Valid Token)** — Confirms successful authorization using a valid Bearer token.  
- **Admin PATCH /admin/users/{id} 200** — Verifies role-based access and successful update of user data.  

These tests demonstrate a full diagnostic workflow:  
1. **Auth validation:** Compare success vs. failure under different token states.  
2. **Role-based access:** Confirm admin-only endpoints reject unauthorized users.  
3. **API integrity:** Verify correct status codes and response behavior across CRUD operations.

Together, they illustrate practical troubleshooting and log-analysis reasoning directly relevant to real-time support workflows.

This pair (successful + failing) demonstrates diagnostic reasoning:
1. Confirm endpoint reachability.
2. Verify auth flows (token present/valid).
3. Interpret status codes and response payloads.