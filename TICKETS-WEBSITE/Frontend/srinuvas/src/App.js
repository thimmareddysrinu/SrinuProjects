

import {Routes,Route} from "react-router-dom"
import Home from './components/HomePages/Home';
import Navbar from './components/HomePages/Navbar';


function App() {
  return (
    <>
    <Navbar/>
    <Routes>


      <Route path='/' element={<Home/>}/>
    </Routes>
  </>
  );
}

export default App;
