import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import ProgressSteps from '../components/ProgressSteps'
import InterestSelector from '../components/InterestSelector'
import { useProfile } from '../context/ProfileContext'

export default function Interests() {
  const navigate = useNavigate()
  const { profile, updateProfile } = useProfile()
  const { t } = useTranslation()
  const ready = profile.interests.length > 0
  return (
    <section className="page-shell">
      <div className="panel mx-auto max-w-3xl">
        <ProgressSteps current={3} />
        <h1 className="text-2xl font-extrabold text-navy sm:text-3xl">{t('interests.title')}</h1>
        <p className="mt-2 text-slate-600">{t('interests.instruction')}</p>
        <div className="mt-5">
          <InterestSelector
            selected={profile.interests}
            onChange={(interests) => updateProfile({ interests, preferred_sectors: interests })}
          />
        </div>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          <button className="secondary-button" onClick={() => navigate('/skills')}>{t('nav.back')}</button>
          <button disabled={!ready} className="primary-button" onClick={() => navigate('/preferences')}>{t('nav.nextPreferences')}</button>
        </div>
      </div>
    </section>
  )
}
