// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC1RW7XCdgJlLuALNOdlmqWi7SMli7uDx0",
  authDomain: "miniproject-3f28f.firebaseapp.com",
  databaseURL: "https://miniproject-3f28f-default-rtdb.firebaseio.com",
  projectId: "miniproject-3f28f",
  storageBucket: "miniproject-3f28f.appspot.com",
  messagingSenderId: "653912233586",
  appId: "1:653912233586:web:6ace1039cdd948581254eb",
  measurementId: "G-41TRD157P2",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
