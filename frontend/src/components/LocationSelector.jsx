import { useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'
import { fetchStates } from '../services/api'

const modes = ['On-site', 'Hybrid', 'Remote']
const cities = ['Bengaluru', 'Hyderabad', 'Pune', 'Mumbai', 'Chennai', 'New Delhi', 'Noida', 'Jaipur', 'Ahmedabad', 'Kolkata', 'Bhubaneswar', 'Patna', 'Ranchi', 'Kochi', 'Guwahati']
export default function LocationSelector({ profile, onChange }) {
  const { t } = useTranslation()
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
    <h2 className="mt-7 text-base font-bold">{t('location.state')}</h2><p className="mt-1 text-sm text-slate-600">{t('location.many')}</p>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{states.map((state) => <button key={state} type="button" onClick={() => toggleState(state)} className={`chip ${profile.preferred_states.includes(state) ? 'chip-selected' : ''}`}>{t('options.'+state, {defaultValue: state})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.city')} <span className="font-normal text-slate-500">({t('location.optional')})</span></h2>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{cities.map((city) => <button key={city} type="button" onClick={() => toggleCity(city)} className={`chip ${profile.preferred_cities.includes(city) ? 'chip-selected' : ''}`}>{t('options.'+city, {defaultValue: city})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.workStyle')}</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{modes.map((mode) => <button type="button" key={mode} onClick={() => onChange({ preferred_location_type: mode })} className={`chip text-center ${profile.preferred_location_type === mode ? 'chip-selected' : ''}`}>{t('modes.'+mode, {defaultValue: mode})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.duration')}</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{[2, 3, 6].map((duration) => <button type="button" key={duration} onClick={() => onChange({ preferred_duration: duration })} className={`chip text-center ${profile.preferred_duration === duration ? 'chip-selected' : ''}`}>{t('location.months', { count: duration })}</button>)}</div>
  </>
}
