import React from 'react';
import logo from './logo.svg';
import { AmplifyAuthenticator, AmplifySignOut } from '@aws-amplify/ui-react';
import './App.css';
import awsconfig from './aws-exports';

Amplify.configure(awsconfig);

const AuthStateApp = () => {
  const [authState, setAuthState] = React.useState();
  const [user, setUser] = React.useState();

  React.useEffect(() => {
      return onAuthUIStateChange((nextAuthState, authData) => {
          setAuthState(nextAuthState);
          setUser(authData)
      });
  }, []);

return authState === AuthState.SignedIn && user ? (
    <div className="App">
        <div>Hello, {user.username}</div>
        <AmplifySignOut />
    </div>
  ) : (
    <AmplifyAuthenticator />
);
}

export default AuthStateApp;
