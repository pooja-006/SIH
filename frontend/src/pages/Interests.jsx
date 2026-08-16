import { useNavigate } from 'react-router-dom'
import ProgressSteps from '../components/ProgressSteps'
import InterestSelector from '../components/InterestSelector'
import { useProfile } from '../context/ProfileContext'

export default function Interests() {
  const navigate = useNavigate()
  const { profile, updateProfile } = useProfile()
  const ready = profile.interests.length > 0
  return (
    <section className="page-shell">
      <div className="panel mx-auto max-w-3xl">
        <ProgressSteps current={3} />
        <h1 className="text-2xl font-extrabold text-navy sm:text-3xl">What type of work interests you?</h1>
        <p className="mt-2 text-slate-600">Choose one or more.</p>
        <div className="mt-5">
          <InterestSelector
            selected={profile.interests}
            onChange={(interests) => updateProfile({ interests, preferred_sectors: interests })}
          />
        </div>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          <button className="secondary-button" onClick={() => navigate('/skills')}>Back</button>
          <button disabled={!ready} className="primary-button" onClick={() => navigate('/preferences')}>Next: Preferences</button>
        </div>
      </div>
    </section>
  )
}
