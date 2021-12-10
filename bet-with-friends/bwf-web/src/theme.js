import { createTheme } from "@mui/material/styles";
import { red, lightBlue } from "@mui/material/colors";

const theme = createTheme({
  palette: {
    primary: red,
    secondary: lightBlue,
  },
  colors: {
    bgColor: "#3e3e3e",
    bgLightColor: "#888",
    mainAccentColor: "#fecc01",
  },
});

export default theme;
