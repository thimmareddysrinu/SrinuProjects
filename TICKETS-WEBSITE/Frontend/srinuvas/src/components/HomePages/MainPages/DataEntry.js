// import React from 'react'

// function DataEntry() {
//   return (
//     <div>
//       <form>
//   <div className="form-row">
//     <div className="col-sm-3">
//       <input type="text" className="form-control form-control-lg" placeholder="First name"/>
//     </div>
//     <div className="col-sm-3">
//       <input type="text" className="form-control form-control-lg" placeholder="Last name"/>
//     </div>
//   </div>
// </form>
    



//     </div>
//   )
// }

// export default DataEntry
function DataEntry() {
  return (
    <div className="container py-4">
      <form>
        <div className="row g-1">
          <div className="col-12 col-md-3 col-sm-12">
            <input
              type="text"
              className="form-control form-control-lg"
              style={{"height":"120px"}}
              placeholder="First name"
            />
          </div>
          <div className="col-12 col-md-3 col-sm-12">
            <input
              type="text"
              className="form-control"
              style={{"height":"120px"}}
              placeholder="Last name"
            />
          </div>
          <div className="col-12 col-md-3 col-sm-12">
            <input
              type="text"
              className="form-control form-control-lg"
              style={{"height":"120px"}}
              placeholder="Email"
            />
          </div>
          <div className="col-12 col-md-3 col-sm-12" style={{"border":"#d80e0e"}}>
            <input
              type="text"
              className="form-control form-control-lg text-bold"
              style={{"height":"120px","textAlign":'start',"fontSize":"30px black","fontFamily":"-moz-initial"}}
              placeholder="Phone"
            />
          </div>
        </div>
      </form>
    </div>
  );
}

export default DataEntry;

