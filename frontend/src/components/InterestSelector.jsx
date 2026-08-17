import { useTranslation } from 'react-i18next'
const interests = ['IT', 'Software Development', 'Data Science', 'AI/ML', 'Cybersecurity', 'Electronics', 'Finance', 'Banking', 'Manufacturing', 'Automobile', 'Agriculture', 'Healthcare', 'Renewable Energy', 'Education', 'Government', 'E-Governance', 'Tourism', 'Logistics', 'Marketing', 'HR', 'Rural Development', 'Infrastructure', 'Telecommunications']
export default function InterestSelector({ selected, onChange }) {
  const { t } = useTranslation()
  const toggle = (interest) => onChange(selected.includes(interest) ? selected.filter((item) => item !== interest) : [...selected, interest])
  return <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">{interests.map((interest) => <button key={interest} type="button" aria-pressed={selected.includes(interest)} onClick={() => toggle(interest)} className={`chip ${selected.includes(interest) ? 'chip-selected' : ''}`}>{t('options.'+interest, {defaultValue: interest})}</button>)}</div>
}
