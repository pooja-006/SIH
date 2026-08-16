import { useNavigate } from 'react-router-dom'
import CandidateForm from '../components/CandidateForm'
import { useProfile } from '../context/ProfileContext'

export default function CandidateProfile() {
  const navigate = useNavigate()
  const { profile, updateProfile } = useProfile()
  return <CandidateForm profile={profile} onChange={updateProfile} onNext={() => navigate('/skills')} />
}
