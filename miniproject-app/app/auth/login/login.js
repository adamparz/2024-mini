import { useState } from "react";
import { signIn } from "../../firebase/auth";
import { useAuth } from "../authContext";
import { Navigate, Link } from "react-router-dom";

const Login = () => {
  const { userLoggedIn } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSigningIn, setIsSigningIn] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!isSigningIn) {
      setIsSigningIn(true);
      await signIn(email, password);
    }
  };

  return <div>{userLoggedIn && <Navigate to={"/home"} replace={true} />}</div>;
};
