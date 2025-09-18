import { useState } from 'react'



function App() {
  const [count, setCount] = useState(0)

  return (
   <>
   <div className="container">
     <h1>Welcome to the Travel App</h1>
     <p>Explore the world with us!</p>
   </div>
   </>
  )
}

export default App
