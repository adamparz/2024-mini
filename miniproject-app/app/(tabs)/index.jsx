import { Button } from "react-native";
import auth from "@react-native-firebase/auth";

export default function HomeScreen() {
  return (
    <div>
      <div>
        <Button
          title="Sign in with email"
          onPress={() =>
            onGoogleButtonPress().then(() =>
              console.log("Signed in with Google!")
            )
          }
        />
      </div>
      Test
    </div>
  );
}
