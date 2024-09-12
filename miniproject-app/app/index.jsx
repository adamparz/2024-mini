import { Button } from "react-native";
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

var firebase = require("firebase");
var firebaseui = require("firebaseui");

// Initialize the FirebaseUI Widget using Firebase.
var ui = new firebaseui.auth.AuthUI(firebase.auth());

export default function HomeScreen() {
  return (
    <div>
      <head>
        <script src="https://www.gstatic.com/firebasejs/ui/6.1.0/firebase-ui-auth.js"></script>
        <link
          type="text/css"
          rel="stylesheet"
          href="https://www.gstatic.com/firebasejs/ui/6.1.0/firebase-ui-auth.css"
        />
      </head>
      <script src="bower_components/firebaseui/dist/firebaseui.js"></script>
      <link
        type="text/css"
        rel="stylesheet"
        href="bower_components/firebaseui/dist/firebaseui.css"
      />
      Test
    </div>
  );
}

const auth = getAuth();
signInWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed in
    const user = userCredential.user;
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
  });
