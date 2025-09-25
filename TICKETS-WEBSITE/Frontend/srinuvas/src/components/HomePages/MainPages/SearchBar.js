import React from 'react'
import "../MainPages/Serach.css"
import { Button } from 'bootstrap'

import AnthoerSerach from './AnthoerSerach'
import Favourite from './Favourite'

import DataEntry from './DataEntry'


function SearchBar() {
  return (
    <div className="backgrounded">
      <div className="container pb-4 pt-5">
        <div className="card ">
          <div className="card-body container">
            <Favourite />
          </div>
        </div>
      </div>

      <div className="container text-center py-3 ps-4">
        <button
          className="btn btn-primary px-5 py-2 rounded-pill fw-bold"
          type="submit"
        >
          Search
        </button>
      </div>
    </div>
  );
}


export default SearchBar