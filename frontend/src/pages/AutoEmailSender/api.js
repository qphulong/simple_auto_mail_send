export const sendEmails = async (data) => {
  const API_URL = "https://simple-auto-mail-send-backend.onrender.com/send-emails";
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.detail || 'Failed to send emails');
    }

    return result;
  } catch (err) {
    throw err;
  }
};