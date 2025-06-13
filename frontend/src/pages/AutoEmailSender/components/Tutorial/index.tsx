import React from 'react';
import styles from './Tutorial.module.css';

interface TutorialProps {
  isVisible: boolean;
  onMouseLeave: () => void;
}

const Tutorial: React.FC<TutorialProps> = ({ isVisible, onMouseLeave }) => {
  return (
    <div
      className={`${styles.tutorial} ${isVisible ? styles.tutorialVisible : ''}`}
      onMouseLeave={onMouseLeave}
    >
      <div className={styles.headerSection}>
        <h2>
          Tutorial
        </h2>
      </div>
      <div className={styles.p1}>
        A
      </div>
      <div className={styles.p2}>
        B
      </div>

    </div>
  );
};

export default Tutorial;