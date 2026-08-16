import { useNavigate } from 'react-router-dom'
import ProgressSteps from '../components/ProgressSteps'
import LocationSelector from '../components/LocationSelector'
import { useProfile } from '../context/ProfileContext'

export default function LocationPreferences() {
  const navigate = useNavigate()
  const { profile, updateProfile } = useProfile()
  return (
    <section className="page-shell">
      <div className="panel mx-auto max-w-3xl">
        <ProgressSteps current={4} />
        <h1 className="text-2xl font-extrabold text-navy sm:text-3xl">Your preferences</h1>
        <p className="mt-2 text-slate-600">Choose places and work style that fit you.</p>
        <LocationSelector profile={profile} onChange={updateProfile} />
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          <button className="secondary-button" onClick={() => navigate('/interests')}>Back</button>
          <button className="primary-button" onClick={() => navigate('/results')}>Find my internships</button>
        </div>
      </div>
    </section>
  )
}
