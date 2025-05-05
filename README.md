# Exam Results Emailer

This guide will help you set up and run the “Exam Results Emailer” on your computer. Follow each step in order. If you get stuck, please ask for help.

---

## 1. Prepare your Python environment (Prerequisite: Ubuntu)
1. **Create a virtual environment (Optional but recommend)**  
   - Open the Terminal
   - Navigate to the folder where you saved the project.  
     ```bash
     cd path/to/your/project
     ```  
   - Create and activate a “venv” (virtual environment):  
     - **macOS/Linux**  
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       ```

2. **Install required packages**  
   - Once your prompt shows `(venv)`, run:  
     ```bash
     pip install -r requirements.txt
     ```  
   - This installs all the Python tools the script needs.

---

## 2. Enable 2‑Factor Authentication on your Gmail account

To send emails securely, Gmail requires you to turn on 2‑Factor Authentication (2FA):

1. Go to your Google Account Settings:  
   https://myaccount.google.com/security  
2. Under **“Signing in to Google”**, find **“2-Step Verification”** and click **“Get started”**.  
3. Follow the on‑screen instructions to set up your second factor (e.g. phone, Authenticator app).

---

## 3. Create a Gmail App Password

After enabling 2FA, you need an “App Password” for the script:

1. In the same **Security** page, under **“Signing in to Google”**, click **“App passwords”**.  
2. It will ask you to sign in again.  
3. Under **“Select app”**, choose **“Other (Custom name)”**, then enter something like `ExamMailer`.  
4. Click **“Generate”**.  
5. Copy the 16‑character password that Google shows you.  
6. **Keep this window open** or copy it now—you will need it in Step 6.

---

## 4. Prepare your CSV file

- **Encoding**: Save your CSV as **UTF‑8**.  
- **Required columns**:  
  - `Names` – the student’s full name  
  - `gmail` – the student’s Gmail address  
- **Grade columns**: Any other column (unless explicitly excluded in `config.yaml`) will be treated as a grade.  
- **Example CSV**:
  ```csv
  No.,Names,S1,S2,S6,Total,Out of 10,Điểm tham gia lớp - 5%,gmail
  1,Nguyen Van A,8.5,7.0,9.0,24.5,10.0,5,nva.student@gmail.com
  2,Tran Thi B,9.0,8.5,8.0,25.5,10.0,4,ttb.student@gmail.com

## 5. Config the config.yaml
The config file is quite self-explain :).

## 6. Prepare the .env file
Due to security reasons, you MUST create this .env file on your own
Your .env file will look something like this
```env
SENDER_EMAIL=example@gmail.com
SENDER_PASSWORD= <the 16‑character password in step 3>
```

## 7. Run the script
```
python3 main.py
```

## 8. Results
If you done correctly it should print something like this.
```bash
Email sent to ****** <******@dlu.edu.vn>
Email sent to ****** <******@dlu.edu.vn>
Email sent to ****** <******@dlu.edu.vn>
```
