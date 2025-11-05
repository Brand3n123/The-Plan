# Front-End (Wix/Velo) API Interaction Snippets

This folder contains trimmed **JavaScript examples** from a Wix/Velo front end that interfaces with a **Xano REST API** for authentication and user management.

## Files

| File | Purpose |
|------|----------|
| `login.js` | Authenticates a user, stores JWT locally, and verifies access to protected endpoints. |
| `signup.js` | Creates new accounts through Xano’s `/create_account` endpoint and handles validation errors. |
| `admin_panel.js` | Performs admin-only CRUD operations (list, add, delete users) using `Authorization: Bearer <token>` headers. |

## Key Concepts Illustrated
- Secure **JWT authentication** and token reuse.
- **Fetch API** usage for RESTful calls.
- **Role-based access control** validation via response codes.
- Error handling and logging for network or authorization failures.

These scripts are simplified to highlight **diagnostic reasoning**—how to reproduce client-server behavior and validate backend responses in an API support context.
