const login = async (user_form) => {
  const token = await fetch(
    `http://127.0.0.1:5000/api/user/login`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: user_form,
    }
  )
    .then((response) => response.json())
    .catch((error) => console.log(error));
  return token;
};


token = login()