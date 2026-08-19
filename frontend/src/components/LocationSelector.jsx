import { useState } from 'react'
import { useTranslation } from 'react-i18next'

const modes = ['On-site', 'Hybrid', 'Remote']

const ALL_INDIAN_STATES = [
  'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
  'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
  'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka',
  'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
  'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab',
  'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
  'Uttarakhand', 'West Bengal'
]

const stateCityMap = {
  'Andaman and Nicobar Islands': ['Port Blair', 'Garacharma', 'Bambooflat'],
  'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Tirupati', 'Rajahmundry', 'Kakinada'],
  'Arunachal Pradesh': ['Itanagar', 'Naharlagun', 'Pasighat', 'Tawang', 'Ziro'],
  'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon', 'Tezpur'],
  'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia', 'Darbhanga', 'Arrah'],
  'Chandigarh': ['Chandigarh'],
  'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Korba', 'Durg', 'Rajnandgaon'],
  'Dadra and Nagar Haveli and Daman and Diu': ['Daman', 'Diu', 'Silvassa'],
  'Delhi': ['New Delhi', 'North Delhi', 'South Delhi', 'East Delhi', 'West Delhi', 'Noida', 'Gurugram'],
  'Goa': ['Panaji', 'Vasco da Gama', 'Margao', 'Mapusa', 'Ponda'],
  'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Gandhinagar', 'Bhavnagar', 'Jamnagar', 'Junagadh', 'Anand'],
  'Haryana': ['Gurugram', 'Faridabad', 'Panipat', 'Ambala', 'Karnal', 'Hisar', 'Rohtak'],
  'Himachal Pradesh': ['Shimla', 'Dharamshala', 'Mandi', 'Solan', 'Kullu', 'Hamirpur'],
  'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Anantnag', 'Baramulla', 'Kathua', 'Udhampur'],
  'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro', 'Deoghar', 'Hazaribagh'],
  'Karnataka': ['Bengaluru', 'Mysuru', 'Mangaluru', 'Hubli', 'Belagavi', 'Davangere', 'Ballari'],
  'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur', 'Kollam', 'Kannur', 'Alappuzha'],
  'Ladakh': ['Leh', 'Kargil'],
  'Lakshadweep': ['Kavaratti', 'Agatti', 'Amini'],
  'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar', 'Rewa', 'Satna'],
  'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Aurangabad', 'Solapur', 'Thane', 'Kolhapur', 'Navi Mumbai'],
  'Manipur': ['Imphal', 'Thoubal', 'Bishnupur', 'Churachandpur', 'Kakching'],
  'Meghalaya': ['Shillong', 'Tura', 'Nongstoin', 'Jowai', 'Baghmara'],
  'Mizoram': ['Aizawl', 'Lunglei', 'Champhai', 'Serchhip'],
  'Nagaland': ['Kohima', 'Dimapur', 'Mokokchung', 'Tuensang'],
  'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Brahmapur', 'Puri', 'Sambalpur', 'Balasore'],
  'Puducherry': ['Puducherry', 'Karaikal', 'Mahe', 'Yanam'],
  'Punjab': ['Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda', 'Mohali'],
  'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Ajmer', 'Bikaner', 'Bhilwara'],
  'Sikkim': ['Gangtok', 'Namchi', 'Gyalshing', 'Mangan'],
  'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli', 'Erode', 'Vellore'],
  'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar', 'Ramagundam', 'Khammam'],
  'Tripura': ['Agartala', 'Dharmanagar', 'Udaipur', 'Kailashahar', 'Bishalgarh'],
  'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Noida', 'Greater Noida', 'Agra', 'Varanasi', 'Meerut', 'Ghaziabad', 'Prayagraj', 'Gorakhpur'],
  'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Haldwani', 'Rudrapur', 'Rishikesh'],
  'West Bengal': ['Kolkata', 'Howrah', 'Darjeeling', 'Siliguri', 'Asansol', 'Durgapur', 'Kharagpur']
}

export default function LocationSelector({ profile, onChange }) {
  const { t } = useTranslation()
  const [searchTerm, setSearchTerm] = useState('')

  const selectedStates = profile.preferred_states || []
  const selectedCities = profile.preferred_cities || []

  const toggleState = (state) => {
    let nextStates
    let nextCities = [...selectedCities]
    if (selectedStates.includes(state)) {
      nextStates = selectedStates.filter((item) => item !== state)
      const citiesToRemove = stateCityMap[state] || []
      nextCities = nextCities.filter((city) => !citiesToRemove.includes(city))
    } else {
      nextStates = [...selectedStates, state]
    }
    onChange({ preferred_states: nextStates, preferred_cities: nextCities })
  }

  const toggleCity = (city) => {
    const nextCities = selectedCities.includes(city)
      ? selectedCities.filter((item) => item !== city)
      : [...selectedCities, city]
    onChange({ preferred_cities: nextCities })
  }

  const filteredStates = ALL_INDIAN_STATES.filter((state) => {
    const localized = t('options.' + state, { defaultValue: state }).toLowerCase()
    return state.toLowerCase().includes(searchTerm.toLowerCase()) || localized.includes(searchTerm.toLowerCase())
  })

  return (
    <div className="space-y-7 mt-6">
      {/* State Selection */}
      <div>
        <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
          <h2 className="text-base font-bold text-navy">{t('location.state')}</h2>
          {selectedStates.length > 0 && (
            <button
              type="button"
              onClick={() => onChange({ preferred_states: [], preferred_cities: [] })}
              className="text-xs font-semibold text-red-600 hover:text-red-800"
            >
              {t('location.clearStates', { defaultValue: 'Clear selected states' })} ({selectedStates.length})
            </button>
          )}
        </div>
        <p className="text-sm text-slate-600 mb-3">{t('location.many')}</p>

        {/* State Search Bar */}
        <div className="relative mb-3">
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder={t('location.searchState', { defaultValue: 'Search state...' })}
            className="w-full rounded-xl border-2 border-slate-200 bg-white py-2 px-4 text-sm focus:border-blue-500 focus:outline-none"
          />
          {searchTerm && (
            <button
              type="button"
              onClick={() => setSearchTerm('')}
              aria-label="Clear search term"
              className="absolute right-3 top-2.5 text-xs text-slate-400 hover:text-slate-600"
            >
              ✕
            </button>
          )}
        </div>

        {/* State Chips Grid */}
        <div className="grid grid-cols-2 gap-2.5 sm:grid-cols-3 max-h-64 overflow-y-auto p-1.5 border border-slate-200 rounded-xl bg-slate-50/50">
          {filteredStates.map((state) => {
            const isSelected = selectedStates.includes(state)
            return (
              <button
                key={state}
                type="button"
                aria-pressed={isSelected}
                onClick={() => toggleState(state)}
                className={`chip ${isSelected ? 'chip-selected' : 'bg-white hover:bg-slate-100'}`}
              >
                {t('options.' + state, { defaultValue: state })}
              </button>
            )
          })}
        </div>
      </div>

      {/* City Selection Based on Selected States */}
      <div>
        <h2 className="text-base font-bold text-navy">
          {t('location.city')} <span className="font-normal text-slate-500">({t('location.optional')})</span>
        </h2>

        {selectedStates.length === 0 ? (
          <div className="mt-3 rounded-xl border border-blue-100 bg-blue-50/50 p-4 text-center text-sm text-blue-800">
            💡 {t('location.selectStateFirst', { defaultValue: 'Select one or more states above to view and choose cities.' })}
          </div>
        ) : (
          <div className="mt-3 space-y-4">
            {selectedStates.map((state) => {
              const cities = stateCityMap[state] || []
              if (cities.length === 0) return null
              const stateName = t('options.' + state, { defaultValue: state })
              return (
                <div key={state} className="rounded-xl border border-slate-200 bg-white p-3.5 shadow-sm">
                  <div className="mb-2.5 flex items-center gap-2">
                    <span className="h-2 w-2 rounded-full bg-blue-600"></span>
                    <h3 className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                      {t('location.citiesFor', { state: stateName, defaultValue: `Cities in ${stateName}` })}
                    </h3>
                  </div>
                  <div className="grid grid-cols-2 gap-2 sm:grid-cols-3">
                    {cities.map((city) => {
                      const isSelected = selectedCities.includes(city)
                      return (
                        <button
                          key={city}
                          type="button"
                          aria-pressed={isSelected}
                          onClick={() => toggleCity(city)}
                          className={`chip ${isSelected ? 'chip-selected' : ''}`}
                        >
                          {t('options.' + city, { defaultValue: city })}
                        </button>
                      )
                    })}
                  </div>
                </div>
              )
            })}
          </div>
        )}
      </div>

      {/* Work Style Section */}
      <div>
        <h2 className="text-base font-bold text-navy">{t('location.workStyle')}</h2>
        <div className="mt-3 grid grid-cols-3 gap-3">
          {modes.map((mode) => (
            <button
              type="button"
              key={mode}
              onClick={() => onChange({ preferred_location_type: mode })}
              className={`chip text-center ${profile.preferred_location_type === mode ? 'chip-selected' : ''}`}
            >
              {t('modes.' + mode, { defaultValue: mode })}
            </button>
          ))}
        </div>
      </div>

      {/* Duration Section */}
      <div>
        <h2 className="text-base font-bold text-navy">{t('location.duration')}</h2>
        <div className="mt-3 grid grid-cols-3 gap-3">
          {[2, 3, 6].map((duration) => (
            <button
              type="button"
              key={duration}
              onClick={() => onChange({ preferred_duration: duration })}
              className={`chip text-center ${profile.preferred_duration === duration ? 'chip-selected' : ''}`}
            >
              {t('location.months', { count: duration })}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
