import React, { useState } from 'react';

function AnotherSearch() {
  const containerStyle = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '16px',
    padding: '20px',
    background: '#f5f5f5',
    borderRadius: '10px',
    boxShadow: '0 4px 10px rgba(0,0,0,0.1)',
    maxWidth: '1000px',
    margin: 'auto',
  };

  const inputGroupStyle = {
    display: 'flex',
    flexDirection: 'column',
    flex: '1 1 200px',
    minWidth: '200px',
  };

  const inputStyle = {
    padding: '8px',
    marginTop: '4px',
    border: '1px solid #ccc',
    borderRadius: '5px',
  };

  const fareTypesStyle = {
    flex: '1 1 100%',
    display: 'flex',
    flexDirection: 'column',
    marginTop: '10px',
  };

  const checkboxStyle = {
    flex: '1 1 100%',
    marginTop: '10px',
  };

  const buttonStyle = {
    padding: '10px 20px',
    backgroundColor: '#008cff',
    color: 'white',
    border: 'none',
    borderRadius: '6px',
    cursor: 'pointer',
    marginTop: '10px',
    fontSize: '16px',
  };

  const [from, setFrom] = useState('');
  const [to, setTo] = useState('');
  const [departureDate, setDepartureDate] = useState('');
  const [fareType, setFareType] = useState('Regular');
  const [zeroCancellation, setZeroCancellation] = useState(false);
  const [travellerClass, setTravellerClass] = useState('1 Traveller, Economy');

  const handleSearch = () => {
    alert(`Searching flight from ${from} to ${to} on ${departureDate}`);
  };

  return (
    <div>
      <div style={containerStyle}>
        <div style={inputGroupStyle}>
          <label>From</label>
          <input
            style={inputStyle}
            type="text"
            placeholder="Delhi"
            value={from}
            onChange={(e) => setFrom(e.target.value)}
          />
        </div>

        <div style={inputGroupStyle}>
          <label>To</label>
          <input
            style={inputStyle}
            type="text"
            placeholder="Bengaluru"
            value={to}
            onChange={(e) => setTo(e.target.value)}
          />
        </div>

        <div style={inputGroupStyle}>
          <label>Departure</label>
          <input
            style={inputStyle}
            type="date"
            value={departureDate}
            onChange={(e) => setDepartureDate(e.target.value)}
          />
        </div>

        <div style={inputGroupStyle}>
          <label>Travellers & Class</label>
          <select
            style={inputStyle}
            value={travellerClass}
            onChange={(e) => setTravellerClass(e.target.value)}
          >
            <option value="1 Traveller, Economy">1 Traveller, Economy</option>
            <option value="2 Travellers, Business">2 Travellers, Business</option>
          </select>
        </div>

        <div style={fareTypesStyle}>
          <label>Select Fare Type:</label>
          {['Regular', 'Student', 'Senior Citizen', 'Armed Forces', 'Doctor and Nurses'].map((type) => (
            <label key={type}>
              <input
                type="radio"
                name="fareType"
                value={type}
                checked={fareType === type}
                onChange={(e) => setFareType(e.target.value)}
              />
              {type}
            </label>
          ))}
        </div>

        <div style={checkboxStyle}>
          <label>
            <input
              type="checkbox"
              checked={zeroCancellation}
              onChange={(e) => setZeroCancellation(e.target.checked)}
            />
            Add Zero Cancellation
          </label>
        </div>

        <button style={buttonStyle} onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
}

export default AnotherSearch;
