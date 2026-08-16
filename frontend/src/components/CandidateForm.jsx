import ProgressSteps from './ProgressSteps'
import { useTranslation } from 'react-i18next'

const educationOptions = ['Diploma', 'B.Tech', 'BCA', 'B.Sc.', 'B.Com', 'BBA', 'BA', 'MBA']
const branchOptions = ['Computer Science', 'Information Technology', 'Data Science', 'Mechanical Engineering', 'Electronics and Communication', 'Electrical Engineering', 'Commerce', 'Business Administration', 'Agriculture', 'Civil Engineering', 'Public Administration', 'Social Work', 'Nursing', 'Tourism']

export default function CandidateForm({ profile, onChange, onNext }) {
  const { t } = useTranslation()
  const ready = profile.education && profile.branch
  return <section className="page-shell"><div className="panel mx-auto max-w-2xl">
    <ProgressSteps current={1} />
    <p className="mb-2 text-sm font-bold text-leaf">{t('profile.start')}</p><h1 className="text-2xl font-extrabold text-navy sm:text-3xl">{t('profile.educationTitle')}</h1><p className="mt-2 text-slate-600">{t('profile.chooseFit')}</p><h2 className="mt-7 text-base font-bold">{t('profile.course')}</h2>
    <div className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-4">{educationOptions.map((item) => <button type="button" key={item} onClick={() => onChange({ education: item })} className={`chip ${profile.education === item ? 'chip-selected' : ''}`}>{item}</button>)}</div>
    <h2 className="mt-7 text-base font-bold">{t('profile.subject')}</h2>
    <select value={profile.branch} onChange={(event) => onChange({ branch: event.target.value })} className="mt-3 min-h-12 w-full rounded-xl border-2 border-slate-300 bg-white px-3 text-base">
      <option value="">{t('profile.chooseSubject')}</option>{branchOptions.map((item) => <option key={item}>{item}</option>)}
    </select>
    <button type="button" disabled={!ready} onClick={onNext} className="primary-button mt-8">{t('nav.nextSkills')}</button>
  </div></section>
}
