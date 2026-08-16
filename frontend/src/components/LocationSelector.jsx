import { useEffect, useState } from 'react'
import { fetchStates } from '../services/api'

const modes = ['On-site', 'Hybrid', 'Remote']
const cities = ['Bengaluru', 'Hyderabad', 'Pune', 'Mumbai', 'Chennai', 'New Delhi', 'Noida', 'Jaipur', 'Ahmedabad', 'Kolkata', 'Bhubaneswar', 'Patna', 'Ranchi', 'Kochi', 'Guwahati']
export default function LocationSelector({ profile, onChange }) {
  const [states, setStates] = useState(['Karnataka', 'Maharashtra', 'Tamil Nadu', 'Delhi', 'Uttar Pradesh', 'Rajasthan', 'Gujarat', 'West Bengal', 'Bihar', 'Telangana'])
  useEffect(() => {
    fetchStates()
      .then((values) => {
        if (Array.isArray(values) && values.length) setStates(values)
      })
      .catch(() => {})
  }, [])
  const toggleState = (state) => onChange({ preferred_states: profile.preferred_states.includes(state) ? profile.preferred_states.filter((item) => item !== state) : [...profile.preferred_states, state] })
  const toggleCity = (city) => onChange({ preferred_cities: profile.preferred_cities.includes(city) ? profile.preferred_cities.filter((item) => item !== city) : [...profile.preferred_cities, city] })
  return <>
    <h2 className="mt-7 text-base font-bold">Choose a state</h2><p className="mt-1 text-sm text-slate-600">You can choose more than one.</p>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{states.map((state) => <button key={state} type="button" onClick={() => toggleState(state)} className={`chip ${profile.preferred_states.includes(state) ? 'chip-selected' : ''}`}>{state}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">Choose a city <span className="font-normal text-slate-500">(optional)</span></h2>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{cities.map((city) => <button key={city} type="button" onClick={() => toggleCity(city)} className={`chip ${profile.preferred_cities.includes(city) ? 'chip-selected' : ''}`}>{city}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">Work style</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{modes.map((mode) => <button type="button" key={mode} onClick={() => onChange({ preferred_location_type: mode })} className={`chip text-center ${profile.preferred_location_type === mode ? 'chip-selected' : ''}`}>{mode}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">How long?</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{[2, 3, 6].map((duration) => <button type="button" key={duration} onClick={() => onChange({ preferred_duration: duration })} className={`chip text-center ${profile.preferred_duration === duration ? 'chip-selected' : ''}`}>{duration} months</button>)}</div>
  </>
}
