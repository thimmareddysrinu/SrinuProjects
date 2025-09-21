import { useState } from 'react'
import {Route,Router} from 'react-router'
import Navbar from './Pages/Home/Navbar/Navbar'


function App() {
  const [count, setCount] = useState(0)

  return (
   <>
   <Navbar/>
   
   </>
  )
}

export default App
