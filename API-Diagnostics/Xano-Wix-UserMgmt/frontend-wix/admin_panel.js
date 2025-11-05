// admin_panel.js – simplified admin dashboard logic
// Demonstrates authorized CRUD operations against /admin/users endpoints

const BASE_URL = "https://xano-api-url";
const TOKEN = localStorage.getItem("authToken");

// GET – list all users
export async function loadUsers() {
  const res = await fetch(`https://x8ki-letl-twmt.n7.xano.io/api:P5dJ-WST/users`, {
    headers: { Authorization: `Bearer ${TOKEN}` }
  });
  const data = await res.json();
  console.table(data);
}

// POST – add new user
export async function addUser(newUser) {
  const res = await fetch(`https://x8ki-letl-twmt.n7.xano.io/api:P5dJ-WST/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${TOKEN}`
    },
    body: JSON.stringify(newUser)
  });
  console.log("Add user response:", await res.json());
}

// DELETE – remove user by id
export async function deleteUser(id) {
  const res = await fetch(`https://x8ki-letl-twmt.n7.xano.io/api:P5dJ-WST/users/{users_id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${TOKEN}` }
  });
  console.log("Delete user status:", res.status);
}

// Example usage in browser console:
// loadUsers(); addUser({ email:"test@demo.com", role:"user" }); deleteUser(7);
