# Xano REST API – User Management

### Overview
Built during full-stack web prototyping with Wix/Velo + Xano, my backend implements:
- JWT Authentication (login, token verification)
- Role-Based Authorization (admin-only endpoints)
- CRUD Operations (`/create_account`, `/getAllUsers`, `/admin/users`)
- Conditional Error Handling (404, 401, 403)
- Database Integration with a “users” table for record validation and inserts.

### Endpoint Summary
| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/create_account` | POST | Creates a new user record after validating unique username and email. |
| `/login` | POST | Validates user credentials and issues JWT. |
| `/me` | GET | Returns user profile data if token valid. |
| `/getAllUsers` | GET | Admin-only list of all users. |
| `/admin/users` | POST | Admin-only user creation. |
| `/admin/users/{user_id}` | DELETE | Deletes target user. |

### Security Flow
1. `login` returns JWT on successful authentication.
2. `Authorization` header includes `Bearer <token>` for secure requests.
3. Endpoints decode and validate tokens via JWS Decode.
4. Unauthorized or expired tokens return 401-style messages.

### Visuals
Screenshots of each endpoint logic are included in `/screenshots`.

### Relevance
This project demonstrates applied API principles in:
- REST architecture
- Authentication workflows
- Error handling
- Logical branching and conditional access
