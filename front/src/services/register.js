const register = ({ url }) => {
  try {
    const response = fetch(`${url}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userInput),
    });
    if (response.status) {
      const data = response.json();
      if (data.token.length > 0) {
        setToken(data.token);
        setIsLogin(true);
      }
    }
  } catch (err) {
    console.log(err);
  }
};
export default register;
