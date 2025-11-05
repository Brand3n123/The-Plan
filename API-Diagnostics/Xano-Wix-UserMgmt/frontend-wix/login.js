// login.js – simplified version for demonstration

export async function performLogin(email, password) {
  try {
    const response = await fetch("https://x8ki-letl-twmt.n7.xano.io/api:P5dJ-WST/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    const data = await response.json();

    if (response.ok && data.authToken) {
      localStorage.setItem("authToken", data.authToken);
      console.log("Login success:", data);
      // redirect to dashboard
    } else {
      console.error("Login failed:", data.message);
    }
  } catch (err) {
    console.error("Network or server error:", err);
  }
}
