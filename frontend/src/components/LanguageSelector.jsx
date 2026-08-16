import { useTranslation } from 'react-i18next'

export default function LanguageSelector() {
  const { i18n } = useTranslation()
  return <label className="flex items-center gap-1 text-sm font-semibold text-white"><span className="sr-only">Language</span>
    <span aria-hidden="true">🌐</span><select aria-label="Language" value={i18n.language} onChange={(event) => i18n.changeLanguage(event.target.value)} className="rounded-md bg-navy px-1 py-1 text-white">
      <option value="en">English</option><option value="hi">हिंदी</option><option value="gu">ગુજરાતી</option>
    </select>
  </label>
}
