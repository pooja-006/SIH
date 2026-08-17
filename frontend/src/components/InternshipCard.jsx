import { Link } from 'react-router-dom'
import MatchBadge from './MatchBadge'
import { useTranslation } from 'react-i18next'
import { translateReason } from '../utils/translateReason'

export default function InternshipCard({ internship }) {
  const { t } = useTranslation()
  return <article className="rounded-2xl border border-slate-200 bg-white p-5 shadow-card">
    <div className="flex items-start justify-between gap-3"><div><p className="text-sm font-bold text-leaf">{t('options.'+internship.sector, {defaultValue: internship.sector})}</p><h2 className="mt-1 text-xl font-extrabold text-navy">{internship.job_title}</h2><p className="mt-1 font-semibold text-slate-600">{internship.company_name}</p></div><MatchBadge percentage={internship.match_percentage} /></div>
    <div className="mt-5 grid grid-cols-2 gap-3 text-sm"><p>📍 {t('options.'+internship.city, {defaultValue: internship.city})}, {t('options.'+internship.state, {defaultValue: internship.state})}</p><p>₹{internship.stipend.toLocaleString('en-IN')} {t('card.perMonth')}</p><p>🗓 {t('card.months', { count: internship.duration })}</p></div>
    <ul className="mt-4 space-y-2 text-sm text-slate-700">{internship.reasons.slice(0, 3).map((reason) => <li key={reason} className="flex gap-2"><span className="text-leaf">✓</span>{translateReason(reason, t)}</li>)}</ul>
    <Link className="secondary-button mt-5 block" to={`/internships/${internship.internship_id}`}>{t('nav.details')}</Link>
  </article>
}
