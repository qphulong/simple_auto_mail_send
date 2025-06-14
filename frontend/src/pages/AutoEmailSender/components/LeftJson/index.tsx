import React from 'react';
import AceEditor from 'react-ace';
import 'ace-builds/src-noconflict/mode-json';
import 'ace-builds/src-noconflict/theme-dracula';
import styles from './LeftJson.module.css';

interface Student {
  student_name: string;
  email: string;
  marks: { [key: string]: number };
}

interface EmailRequest {
  gmail: string;
  app_password: string;
  template: string;
  template_vars: { [key: string]: string };
  scores: Student[];
}

interface LeftJsonProps {
  jsonInput: string;
  onJsonChange: (newValue: string) => void;
  onSendEmails: () => void;
  isLoading: boolean;
  parsedData: EmailRequest | null;
  status: string;
  error: string;
}

const LeftJson: React.FC<LeftJsonProps> = ({
  jsonInput,
  onJsonChange,
  onSendEmails,
  isLoading,
  parsedData,
  status,
  error,
}) => {
  return (
    <div className={styles.leftPanel}>
      <div className={styles.headerSection}>
        <h2>
          Paste JSON Here
        </h2>
      </div>
      <div className={styles.editorSection}>
        <AceEditor
          mode="json"
          theme="dracula"
          value={jsonInput}
          onChange={onJsonChange}
          width="70%"
          height="100%"
          setOptions={{ useWorker: false }}
          className={styles.aceEditor}
        />
      </div>
      <div className={styles.footerSection}>
        <button
          onClick={onSendEmails}
          disabled={isLoading || !parsedData}
          className={`${styles.button} ${isLoading || !parsedData ? styles.buttonDisabled : styles.buttonEnabled}`}
        >
          {isLoading ? 'Sending...' : 'Send Emails'}
        </button>
        {status && <div className={styles.successMessage}>{status}</div>}
        {error && <div className={styles.errorMessage}>{error}</div>}
      </div>
    </div>
  );
};

export default LeftJson;