import { useTranslation } from 'react-i18next'
export default function MatchBadge({ percentage }) { const { t } = useTranslation(); return <span className="inline-flex rounded-full bg-green-100 px-3 py-1 text-sm font-extrabold text-leaf">{t('card.match', { percentage: Math.round(percentage) })}</span> }
