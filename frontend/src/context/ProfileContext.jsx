import { createContext, useContext, useState } from 'react'

const ProfileContext = createContext(null)
const initialProfile = {
  education: '', branch: '', skills: [], interests: [], preferred_sectors: [],
  preferred_states: [], preferred_cities: [], preferred_location_type: 'On-site',
  preferred_duration: 3, experience_level: 'No prior experience'
}

export function ProfileProvider({ children }) {
  const [profile, setProfile] = useState(initialProfile)
  const [recommendations, setRecommendations] = useState([])
  const [candidateId, setCandidateId] = useState(null)
  const updateProfile = (changes) => {
    setProfile((current) => ({ ...current, ...changes }))
    setCandidateId(null)
    setRecommendations([])
  }
  return <ProfileContext.Provider value={{ profile, updateProfile, recommendations, setRecommendations, candidateId, setCandidateId }}>{children}</ProfileContext.Provider>
}

export function useProfile() {
  const context = useContext(ProfileContext)
  if (!context) throw new Error('useProfile must be used inside ProfileProvider')
  return context
}
