import { useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'
import { fetchStates } from '../services/api'

const modes = ['On-site', 'Hybrid', 'Remote']
const stateCityMap = {
  'Andaman and Nicobar Islands': ['Port Blair', 'Garacharma', 'Bambooflat'],
  'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Tirupati'],
  'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon'],
  'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia'],
  'Chandigarh': ['Chandigarh'],
  'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Durg'],
  'Delhi': ['New Delhi', 'North Delhi', 'South Delhi', 'East Delhi', 'West Delhi'],
  'Goa': ['Panaji', 'Vasco da Gama', 'Margao', 'Mapusa', 'Ponda'],
  'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Gandhinagar', 'Bhavnagar'],
  'Himachal Pradesh': ['Shimla', 'Dharamshala', 'Mandi', 'Solan', 'Kullu'],
  'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Kathua'],
  'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro', 'Deoghar'],
  'Karnataka': ['Bengaluru', 'Mysuru', 'Mangaluru', 'Hubli', 'Belagavi'],
  'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Kollam'],
  'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar', 'Rewa'],
  'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Aurangabad', 'Solapur'],
  'Manipur': ['Imphal', 'Thoubal', 'Bishnupur', 'Churachandpur', 'Kakching'],
  'Meghalaya': ['Shillong', 'Tura', 'Nongstoin', 'Jowai', 'Baghmara'],
  'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Brahmapur', 'Puri'],
  'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Ajmer'],
  'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem'],
  'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar', 'Ramagundam'],
  'Tripura': ['Agartala', 'Dharmanagar', 'Udaipur', 'Kailashahar', 'Bishalgarh'],
  'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Noida', 'Agra', 'Varanasi', 'Meerut'],
  'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Haldwani', 'Rudrapur'],
  'West Bengal': ['Kolkata', 'Howrah', 'Darjeeling', 'Siliguri', 'Asansol', 'Durgapur']
}

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
  
  const availableCities = profile.preferred_states.reduce((acc, state) => acc.concat(stateCityMap[state] || []), [])
  
  return <>
    <h2 className="mt-7 text-base font-bold">{t('location.state')}</h2><p className="mt-1 text-sm text-slate-600">{t('location.many')}</p>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{states.map((state) => <button key={state} type="button" onClick={() => toggleState(state)} className={`chip ${profile.preferred_states.includes(state) ? 'chip-selected' : ''}`}>{t('options.'+state, {defaultValue: state})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.city')} <span className="font-normal text-slate-500">({t('location.optional')})</span></h2>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">{availableCities.map((city) => <button key={city} type="button" onClick={() => toggleCity(city)} className={`chip ${profile.preferred_cities.includes(city) ? 'chip-selected' : ''}`}>{t('options.'+city, {defaultValue: city})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.workStyle')}</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{modes.map((mode) => <button type="button" key={mode} onClick={() => onChange({ preferred_location_type: mode })} className={`chip text-center ${profile.preferred_location_type === mode ? 'chip-selected' : ''}`}>{t('modes.'+mode, {defaultValue: mode})}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('location.duration')}</h2>
    <div className="mt-3 grid grid-cols-3 gap-3">{[2, 3, 6].map((duration) => <button type="button" key={duration} onClick={() => onChange({ preferred_duration: duration })} className={`chip text-center ${profile.preferred_duration === duration ? 'chip-selected' : ''}`}>{t('location.months', { count: duration })}</button>)}</div>
  </>
}
