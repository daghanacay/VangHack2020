import React from 'react';
import logo from './etf-logo.png';
import Amplify from 'aws-amplify';
import { AmplifyAuthenticator, AmplifySignOut } from '@aws-amplify/ui-react';
import { AuthState, onAuthUIStateChange } from '@aws-amplify/ui-components';
import './App.css';
import awsconfig from './aws-exports';
import { ThemeProvider } from '@material-ui/core'
import { createMuiTheme } from '@material-ui/core/styles';
import Portfolio from './components/Portfolio'

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#96151d'
    },
    secondary: {
      main: '#1a1a1a',
    },
  },
});

const MyAmpTheme = {
  signInButtonIcon: { 'backgroundColor': theme.palette.primary.main }
}

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
    <ThemeProvider theme={theme}>
      <div className="App">
        <div className="header-bar">
          <div className="left">
            <img src={logo} className="App-logo" alt="logo" />
          </div>
          <div className="right">
            <div className="username">Hello, {user.username}</div>
            <AmplifySignOut theme={MyAmpTheme} />
          </div>
        </div>

        <div className="content">
          <Portfolio username={user.username}></Portfolio>
        </div>
      </div>
    </ThemeProvider>
  ) : (
      <ThemeProvider theme={theme}>
        <div className="App">
          <img src={logo} className="App-logo" alt="logo" />
          <AmplifyAuthenticator theme={MyAmpTheme} />
        </div>
      </ThemeProvider>
    );
}

export default AuthStateApp;
