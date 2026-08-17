import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import LoadingState from '../components/LoadingState'
import ErrorState from '../components/ErrorState'
import { fetchInternship } from '../services/api'

export default function InternshipDetails() {
  const { internshipId } = useParams()
  const { t } = useTranslation()
  const [internship, setInternship] = useState(null)
  const [error, setError] = useState(false)
  const load = () => { setError(false); setInternship(null); fetchInternship(internshipId).then(setInternship).catch(() => setError(true)) }
  useEffect(load, [internshipId])
  if (error) return <section className="page-shell"><ErrorState onRetry={load} /></section>
  if (!internship) return <section className="page-shell"><LoadingState /></section>
  return <section className="page-shell"><article className="panel mx-auto max-w-2xl"><p className="font-bold text-leaf">{internship.sector}</p><h1 className="mt-1 text-3xl font-extrabold text-navy">{internship.job_title}</h1><p className="mt-2 text-lg font-semibold text-slate-600">{internship.company_name}</p>
    <div className="mt-7 grid gap-4 rounded-xl bg-blue-50 p-4 sm:grid-cols-2"><p>📍 {internship.cities}, {internship.states}</p><p>₹{internship.stipend.toLocaleString('en-IN')} {t('card.perMonth')}</p><p>🗓 {t('location.months', { count: internship.duration_months })}</p><p>💼 {t('options.'+internship.work_mode, {defaultValue: internship.work_mode})}</p></div>
    <h2 className="mt-7 text-xl font-extrabold text-navy">{t('details.about')}</h2><p className="mt-2 leading-7 text-slate-700">{internship.description}</p>
    <h2 className="mt-7 text-xl font-extrabold text-navy">{t('details.skills')}</h2><div className="mt-3 flex flex-wrap gap-2">{internship.required_skills.map((skill) => <span key={skill} className="rounded-full bg-green-100 px-3 py-1 font-semibold text-leaf">{t('options.'+skill, {defaultValue: skill})}</span>)}</div>
    <h2 className="mt-7 text-xl font-extrabold text-navy">{t('details.apply')}</h2><p className="mt-2 text-slate-700">{internship.preferred_education} · {internship.eligible_branches.map(b => t('options.'+b, {defaultValue: b})).join(', ')}</p>
    <Link to="/results" className="secondary-button mt-8 block">{t('nav.backResults')}</Link>
  </article></section>
}
