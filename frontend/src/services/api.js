import axios from 'axios'

const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE_URL || '/api', timeout: 15000 })

export function validateCandidateProfile(profile) {
  if (!profile.education?.trim()) return 'Choose your course.'
  if (!profile.branch?.trim()) return 'Choose your subject.'
  if (!Array.isArray(profile.skills) || profile.skills.length === 0) return 'Choose at least one skill.'
  if (!Array.isArray(profile.interests) || profile.interests.length === 0) return 'Choose at least one work interest.'
  if (!Number.isInteger(Number(profile.preferred_duration)) || Number(profile.preferred_duration) < 1 || Number(profile.preferred_duration) > 12) return 'Choose an internship duration.'
  return null
}

export function profilePayload(profile) {
  return {
    ...profile,
    education: profile.education.trim(),
    branch: profile.branch.trim(),
    skills: profile.skills.map((value) => value.trim()).filter(Boolean),
    interests: profile.interests.map((value) => value.trim()).filter(Boolean),
    preferred_sectors: profile.preferred_sectors.map((value) => value.trim()).filter(Boolean),
    preferred_states: profile.preferred_states.map((value) => value.trim()).filter(Boolean),
    preferred_cities: profile.preferred_cities.map((value) => value.trim()).filter(Boolean),
    preferred_duration: Number(profile.preferred_duration)
  }
}

export const submitCandidate = (profile) => api.post('/candidates', profilePayload(profile)).then((response) => response.data)
export const fetchSectors = () => api.get('/sectors').then((response) => response.data.values)
export const fetchStates = () => api.get('/states').then((response) => response.data.values)
export const fetchRecommendations = (profile) => api.post('/recommendations', profilePayload(profile)).then((response) => response.data)
export const fetchInternship = (id) => api.get(`/internships/${id}`).then((response) => response.data)
