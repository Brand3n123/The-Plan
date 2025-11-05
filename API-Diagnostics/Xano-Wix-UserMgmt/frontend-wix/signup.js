// signup.js – simplified version for demo purposes
// Handles user registration via Xano REST endpoint

export async function createAccount(email, password, name) {
  try {
    const response = await fetch("https://x8ki-letl-twmt.n7.xano.io/api:P5dJ-WST/create_account", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password, name })
    });

    const data = await response.json();

    if (response.ok) {
      console.log("Account created successfully:", data);
      // Optionally redirect to login or confirmation page
    } else {
      console.error("Account creation failed:", data.message);
    }
  } catch (err) {
    console.error("Network or server error during signup:", err);
  }
}
