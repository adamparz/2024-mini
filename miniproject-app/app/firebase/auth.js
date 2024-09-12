import {auth} from "./firebase";
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

export const createUser = async (email, pass) => {
    return createUserWithEmailAndPassword(auth, email, pass)
}

export const signIn = (email, pass) => {
    return signInWithEmailAndPassword(auth, email, pass);
}