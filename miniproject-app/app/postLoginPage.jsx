import { getAuth, signOut } from "firebase/auth";

export default postLoginPage = () => {
  return (
    <div>
      <div>postLoginPage test</div>
    </div>
  );
};

const auth = getAuth();
signOut(auth)
  .then(() => {
    // Sign-out successful.
  })
  .catch((error) => {
    // An error happened.
  });
