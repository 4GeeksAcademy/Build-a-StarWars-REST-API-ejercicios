const login = async ({ url }) => {
  try {
    const response = await fetch(`${url}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userInput),
    });

    if (response.status == 200) {
      const data = await response.json();
      if (data.token.length > 0) {
        setToken(data.token);

        setIsLogin(true);
      }
      console.log(data);
    }
  } catch (err) {
    console.log(err);
  }
};
export default login;
