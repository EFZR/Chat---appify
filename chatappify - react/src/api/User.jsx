export const login = async (form) => {
  const response = await fetch(
    `${import.meta.env.VITE_CHATAPPIFY_URL}/api/user/login`,
    {
      method: "POST",
      body: form,
    }
  );
  const data = await response.json();
  return data;
};

export const register = async (form) => {
  const response = await fetch(
    `${import.meta.env.VITE_CHATAPPIFY_URL}/api/user/register`,
    {
      method: "POST",
      body: form,
    }
  );
  const data = await response.json();
  return data;
}
