import "./App.css";
import Header from "./components/Header";
import Main from "./components/Main";
import Sidebar from "./components/Sidebar";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme";
import { BrowserRouter as Router } from "react-router-dom";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className='App'>
        <Router>
          <Header />
          <div className='general-content'>
            <Sidebar />
            <Main />
          </div>
        </Router>
      </div>
    </ThemeProvider>
  );
}

export default App;
