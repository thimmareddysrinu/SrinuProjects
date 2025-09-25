import { useState } from 'react'
import {Route,Routes} from 'react-router'
import Navbar from './Pages/Home/Navbar/Navbar'
import Home from './Pages/Home/Home'


function App() {
  const [count, setCount] = useState(0)

  return (
   <>
   <Routes>
    
    
    <Route path='/' Component={<Home/>}  />
    
   
   
   
   </Routes>
   
   
   </>
  )
}

export default App
