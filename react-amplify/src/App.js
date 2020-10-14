import React from 'react';
import logo from './etf-logo.png';
import Amplify from 'aws-amplify';
import { AmplifyAuthenticator, AmplifySignOut } from '@aws-amplify/ui-react';
import { AuthState, onAuthUIStateChange } from '@aws-amplify/ui-components';
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
    <div className="header-bar">
    <div class="left">
      <img src={logo} className="App-logo" alt="logo" />
    </div>
    <div class="right">
        <div className="username">Hello, {user.username}</div>
        <AmplifySignOut />
        </div>
        </div>
    </div>
  ) : (
    <div className="App">
    <img src={logo} className="App-logo" alt="logo" />
    <AmplifyAuthenticator />
    </div>
);
}

export default AuthStateApp;
