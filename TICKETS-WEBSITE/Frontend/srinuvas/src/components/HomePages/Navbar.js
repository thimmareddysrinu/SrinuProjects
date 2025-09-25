import React from 'react'
import {Link} from 'react-router-dom'
function Navbar() {
  return (
    <div>


        <nav className="navbar navbar-expand-lg  " style={{"backgroundColor":"#5cda0eff" ,"text":"white"}}>
  <div className="container-fluid">
    <Link className="navbar-brand" to='/' style={{"fontSize":"30px","color":"#28029cff"}} >JusTickets</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0 text-center">
        <li className="nav-item  ">
          <Link to='/' className="nav-link " style={{"fontSize":"20px","color":"#efe4e7ff"}} aria-current="page" href="#">About</Link>
        </li>
        <li className="nav-item  ">
          <a className="nav-link  " style={{"fontSize":"20px","color":"#28029cff"}} href="#">
            Profile

           
          </a>
        </li>
      
       
      </ul>
      <form className="d-flex pe-5" role="search" style={{}}>
        <input className=" form-control w-auto me-3" style={{"width":"200px"}} type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
    </div>
  )
}

export default Navbar