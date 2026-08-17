import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import RecommendationList from '../components/RecommendationList'
import LoadingState from '../components/LoadingState'
import ErrorState from '../components/ErrorState'
import { useProfile } from '../context/ProfileContext'
import { fetchRecommendations, submitCandidate, validateCandidateProfile } from '../services/api'

export default function RecommendationResults() {
  const { profile, recommendations, setRecommendations, candidateId, setCandidateId } = useProfile()
  const { t } = useTranslation()
  const [status, setStatus] = useState(recommendations.length ? 'ready' : 'loading')
  const [validationMessage, setValidationMessage] = useState('')
  const load = useCallback(async () => {
    const validationError = validateCandidateProfile(profile)
    if (validationError) { setValidationMessage(validationError); setStatus('invalid'); return }
    setStatus('loading')
    try {
      if (!candidateId) {
        const savedCandidate = await submitCandidate(profile)
        setCandidateId(savedCandidate.candidate_id)
      }
      const result = await fetchRecommendations(profile)
      const matches = Array.isArray(result?.recommendations) ? result.recommendations.slice(0, 5) : []
      setRecommendations(matches)
      setStatus(matches.length ? 'ready' : 'empty')
    } catch (error) {
      const detail = error?.response?.data?.detail
      setValidationMessage(typeof detail === 'string' ? detail : '')
      setStatus('error')
    }
  }, [candidateId, profile, setCandidateId, setRecommendations])
  useEffect(() => { if (!recommendations.length) load() }, [load, recommendations.length])
  return <section className="page-shell">
    {status === 'loading' && <LoadingState />}
    {status === 'error' && <ErrorState onRetry={load} message={validationMessage || undefined} />}
    {status === 'invalid' && <ErrorState message={validationMessage} onRetry={() => window.history.back()} />}
    {status === 'empty' && <div className="panel mx-auto max-w-md text-center"><div className="text-4xl">🔎</div><h1 className="mt-4 text-2xl font-extrabold text-navy">{t('results.noneTitle')}</h1><p className="mt-2 text-slate-600">{t('results.noneText')}</p><Link to="/preferences" className="primary-button mt-6 block">{t('nav.updateChoices')}</Link></div>}
    {status === 'ready' && <div className="mx-auto max-w-3xl"><div className="mb-6"><p className="text-sm font-bold text-leaf">{t('results.label')}</p><h1 className="text-3xl font-extrabold text-navy">{t('results.heading')}</h1><p className="mt-2 text-slate-600">{t('results.instruction')}</p></div><RecommendationList recommendations={recommendations} /><Link to="/preferences" className="secondary-button mt-6 block">{t('nav.changeChoices')}</Link></div>}
  </section>
}
