import React from 'react'
import DataEntry from './DataEntry'

function Favourite() {

  
  return (
   <div className="container">
  <div className="card bg-light rounded-pill py-3 px-4">
    <ul className="d-flex justify-content-around align-items-center m-0 p-0 list-unstyled w-auto">
      <li className="text-center mx-3">
        <a >
          <div>
            <i className="bi bi-airplane fs-3"  />
          </div>
          <h5 className="mb-0  ">Flight</h5>
        </a>
      </li>
      <li className="text-center mx-3">
        <a>
          <div>
            <i className="bi bi-bus-front fs-3" />
          </div>
          <h5 className="mb-0">Bus</h5>
        </a>
      </li>
      <li className="text-center mx-3">
        <a>
          <div>
            <i className="bi bi-hospital fs-3" />
          </div>
          <h5 className="mb-0">Hotel</h5>
        </a>
      </li>
      <li className="text-center mx-3">
        <a>
          <div>
            <i className="bi bi-train-front-fill fs-3" />
          </div>
          <h5 className="mb-0">Trains</h5>
        </a>
      </li>
      <li className="text-center mx-3">
        <a>
          <div>
            <i className="bi bi-car-front-fill fs-3" />
          </div>
          <h5 className="mb-0">Cabs</h5>
        </a>
      </li>
      <li className="text-center mx-3">
        <a>
          <div>
            <i className="bi bi-film fs-3" />
          </div>
          <h5 className="mb-0">Movies</h5>
        </a>
      </li>
    </ul>
  </div>

  <div className="text-center mt-4">
    <DataEntry />
  </div>
</div>

  )
}

export default Favourite