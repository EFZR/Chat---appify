export const getContacts = async (token) => {
  const response = await fetch(
    `${import.meta.env.VITE_CHATAPPIFY_URL}/api/contactManagement/contacts`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    }
  )
  const contacts = await response.json();
  return contacts;
};
