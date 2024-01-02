import { BrowserRouter, Route, Routes } from "react-router-dom";
import Register from "./component/Register";
import Login from "./component/Login";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
            <Routes>
                <Route path='/' element={<Login />} />
                <Route path='/register' element={<Register />} />
            </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
