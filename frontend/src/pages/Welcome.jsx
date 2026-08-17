import { Link } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

export default function Welcome() {
  const { t, i18n } = useTranslation()
  
  return (
    <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        {/* Left Column */}
        <div className="flex flex-col items-start">
          <div className="inline-flex items-center gap-2 rounded-full border border-orange-200 bg-orange-50 px-3 py-1 text-[11px] font-bold tracking-widest text-[#e6811d] uppercase mb-8">
            <svg className="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2l2.4 7.6H22l-6.2 4.5 2.4 7.6-6.2-4.5-6.2 4.5 2.4-7.6-6.2-4.5h7.6z" />
            </svg>
            {t('welcome.scheme')}
          </div>
          
          <h1 className="text-[3.5rem] leading-[1.1] font-extrabold text-[#0B1527] tracking-tight mb-6 whitespace-pre-line">
            {t('welcome.hero_title')}
          </h1>
          
          <p className="text-lg text-gray-600 mb-10 max-w-md">
            {t('welcome.text')}
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mb-14">
            <Link to="/profile" className="inline-flex h-12 items-center justify-center rounded-full bg-[#2349B8] px-8 font-semibold text-white hover:bg-blue-800 transition-colors">
              {t('welcome.start')} <span className="ml-2">→</span>
            </Link>
            <Link to="/signin" className="inline-flex h-12 items-center justify-center rounded-full border border-gray-300 bg-white px-8 font-semibold text-gray-700 hover:bg-gray-50 transition-colors">
              {t('signin.signin')}
            </Link>
          </div>
          
          <div>
            <h3 className="text-[11px] font-bold tracking-widest text-gray-500 uppercase mb-4">{t('welcome.choose_lang')}</h3>
            <div className="flex flex-wrap gap-3">
              {[
                { code: 'en', label: 'English' },
                { code: 'hi', label: 'हिन्दी' },
                { code: 'gu', label: 'ગુજરાતી' }
              ].map((l) => (
                <button 
                  key={l.code}
                  onClick={() => i18n.changeLanguage(l.code)}
                  className={`rounded-full border px-6 py-2.5 text-sm font-semibold transition-colors ${
                    i18n.language.startsWith(l.code)
                      ? 'border-[#2349B8] text-[#2349B8] bg-blue-50' 
                      : 'border-gray-200 text-gray-600 hover:border-gray-300'
                  }`}
                >
                  {l.label}
                </button>
              ))}
            </div>
          </div>
        </div>
        
        {/* Right Column */}
        <div className="flex justify-center lg:justify-end">
          <div className="relative w-full max-w-[460px] aspect-square md:aspect-[4/5] rounded-[2rem] overflow-hidden shadow-2xl">
            <img 
              src="/student_laptop.png" 
              alt="Student working on laptop" 
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      </div>
      
      {/* Bottom Cards */}
      <div className="mt-16 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pb-20">
        {[
          { num: '01', title: t('progress.education'), icon: <path strokeLinecap="round" strokeLinejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" /> },
          { num: '02', title: t('progress.skills'), icon: <path strokeLinecap="round" strokeLinejoin="round" d="M11.42 15.17L17.25 21A2.652 2.652 0 0021 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.993-6.06c-1.387-1.682-3.83-2.029-5.63-1.002-1.921 1.096-2.5 3.523-1.258 5.376.621.92 1.625 1.48 2.705 1.53.518.024 1.034-.055 1.516-.231l4.44-1.61zM17.25 21L15 18.75m2.25 2.25l2.25-2.25" /> },
          { num: '03', title: t('progress.interest'), icon: <path strokeLinecap="round" strokeLinejoin="round" d="M15.042 21.672L13.684 16.6m0 0l-2.51 2.225.569-9.47 5.227 7.917-3.286-.672zm-7.518-.267A8.25 8.25 0 1120.25 10.5M8.288 14.212A5.25 5.25 0 1117.25 10.5" /> },
          { num: '04', title: t('progress.preferences'), icon: <><path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" /><path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" /></> }
        ].map((card) => (
          <div key={card.num} className="rounded-2xl border border-gray-100 bg-white p-6 shadow-sm hover:shadow-md transition-shadow">
            <div className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-[#f4f7fb] text-[#2349B8]">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="h-6 w-6">
                {card.icon}
              </svg>
            </div>
            <div className="text-xs font-bold text-gray-400 mb-1">{card.num}</div>
            <div className="text-lg font-bold text-[#0B1527]">{card.title}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
