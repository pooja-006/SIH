import { useNavigate } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import ProgressSteps from '../components/ProgressSteps'
import SkillSelector from '../components/SkillSelector'
import { useProfile } from '../context/ProfileContext'

export default function SkillsInterests() {
  const navigate = useNavigate()
  const { profile, updateProfile } = useProfile()
  const { t } = useTranslation()
  const ready = profile.skills.length > 0
  return (
    <section className="page-shell">
      <div className="panel mx-auto max-w-3xl">
        <ProgressSteps current={2} />
        <h1 className="text-2xl font-extrabold text-navy sm:text-3xl">{t('skills.title')}</h1>
        <p className="mt-2 text-slate-600">{t('skills.instruction')}</p>
        <div className="mt-5">
          <SkillSelector selected={profile.skills} branch={profile.branch} onChange={(skills) => updateProfile({ skills })} />
        </div>
        <div className="mt-8 grid gap-3 sm:grid-cols-2">
          <button className="secondary-button" onClick={() => navigate('/profile')}>{t('nav.back')}</button>
          <button disabled={!ready} className="primary-button" onClick={() => navigate('/interests')}>{t('nav.nextInterests')}</button>
        </div>
      </div>
    </section>
  )
}
