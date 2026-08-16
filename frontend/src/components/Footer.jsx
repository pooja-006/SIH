import { useTranslation } from 'react-i18next'
export default function Footer() { const { t } = useTranslation(); return <footer className="bg-navy px-4 py-5 text-center text-sm text-blue-100">{t('privacy')}</footer> }
