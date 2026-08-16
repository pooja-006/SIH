import { useTranslation } from 'react-i18next'

const stepKeys = ['education', 'skills', 'interest', 'preferences']

export default function ProgressSteps({ current }) {
  const { t } = useTranslation()
  return (
    <div className="mb-7" aria-label={`Step ${current} of 4`}>
      <div className="mb-2 text-xs font-bold uppercase tracking-wider text-slate-500">
        {t('progress.step', { current })}
      </div>
      <div className="mb-4 h-1.5 overflow-hidden rounded-full bg-slate-200" aria-hidden="true">
        <div
          className="h-full rounded-full bg-[#2349B8] transition-all"
          style={{ width: `${(current / 4) * 100}%` }}
        />
      </div>
      <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
        {stepKeys.map((key, index) => {
          const step = index + 1
          const active = step === current
          const done = step < current
          return (
            <div
              key={key}
              className={`rounded-xl border px-3 py-2.5 text-sm font-semibold ${
                active
                  ? 'border-[#2349B8] bg-blue-50 text-[#2349B8]'
                  : done
                    ? 'border-slate-200 bg-white text-slate-700'
                    : 'border-slate-200 bg-white text-slate-400'
              }`}
            >
              <span className="mr-1.5">{step}</span>
              {t(`progress.${key}`)}
            </div>
          )
        })}
      </div>
    </div>
  )
}
