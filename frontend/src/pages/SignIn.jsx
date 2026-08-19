import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { registerAPI, loginAPI } from '../services/api'
import { useProfile } from '../context/ProfileContext'

export default function SignIn() {
  const navigate = useNavigate()
  const { t } = useTranslation()
  const { loginUser } = useProfile()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isRegister, setIsRegister] = useState(false)
  const [errorMsg, setErrorMsg] = useState('')
  const [successMsg, setSuccessMsg] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setErrorMsg('')
    setSuccessMsg('')
    
    if (!email.includes('@')) {
      setErrorMsg(t('signin.invalid_email', { defaultValue: 'Invalid email' }))
      return
    }

    setLoading(true)

    if (isRegister) {
      try {
        await registerAPI({ email, password })
        setSuccessMsg(t('signin.success', { defaultValue: 'Account created successfully' }))
        setTimeout(() => setIsRegister(false), 2000)
      } catch (err) {
        if (err.response && err.response.status === 409) {
          setErrorMsg(t('signin.account_exists', { defaultValue: 'Account already exists' }))
        } else if (err.response && err.response.status === 422) {
          setErrorMsg(t('signin.invalid_email', { defaultValue: 'Invalid email' }))
        } else if (err.message && err.message.toLowerCase().includes('network')) {
          setErrorMsg(t('signin.network_error', { defaultValue: 'Network error' }))
        } else {
          setErrorMsg(t('signin.server_error', { defaultValue: 'Unable to create account' }))
        }
      }
    } else {
      try {
        const data = await loginAPI({ email, password })
        loginUser({ user_id: data.user_id, email: data.email })
        setSuccessMsg(t('signin.login_success', { defaultValue: 'Logged in successfully!' }))
        setTimeout(() => navigate('/profile'), 800)
      } catch (err) {
        if (err.response && err.response.status === 404) {
          setErrorMsg(t('signin.no_account_found', { defaultValue: 'Account does not exist. Please create an account first.' }))
        } else if (err.response && err.response.status === 401) {
          setErrorMsg(t('signin.wrong_password', { defaultValue: 'Incorrect password. Please try again.' }))
        } else if (err.message && err.message.toLowerCase().includes('network')) {
          setErrorMsg(t('signin.network_error', { defaultValue: 'Network error' }))
        } else {
          setErrorMsg(t('signin.server_error', { defaultValue: 'Server error' }))
        }
      }
    }
    setLoading(false)
  }

  return (
    <div className="flex min-h-[80vh] items-center justify-center px-4 py-12 sm:px-6 lg:px-8">
      <div className="w-full max-w-md space-y-8 rounded-[2rem] bg-white p-10 shadow-2xl border border-gray-100">
        <div>
          <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-[#2349B8] shadow-lg shadow-blue-200">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" className="h-8 w-8">
              <path d="M12 2l2.4 7.6H22l-6.2 4.5 2.4 7.6-6.2-4.5-6.2 4.5 2.4-7.6-6.2-4.5h7.6z" />
            </svg>
          </div>
          <h2 className="mt-8 text-center text-3xl font-extrabold tracking-tight text-[#0B1527]">
            {isRegister ? t('signin.create_account', { defaultValue: 'Create Account' }) : t('signin.signin')}
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            {t('signin.or')}{' '}
            <Link to="/" className="font-medium text-[#2349B8] hover:text-blue-800 transition-colors">
              {t('nav.home') || 'return to home'}
            </Link>
          </p>
        </div>
        {errorMsg && <div className="mt-2 text-center text-sm font-medium text-red-600">{errorMsg}</div>}
        {successMsg && <div className="mt-2 text-center text-sm font-medium text-green-600">{successMsg}</div>}
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md">
            <div>
              <label htmlFor="email-address" className="sr-only">{t('signin.email')}</label>
              <input
                id="email-address"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="relative block w-full appearance-none rounded-xl border border-gray-300 px-4 py-3.5 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-[#2349B8] focus:outline-none focus:ring-1 focus:ring-[#2349B8] sm:text-sm transition-shadow"
                placeholder={t('signin.email')}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">{t('signin.password')}</label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="relative block w-full appearance-none rounded-xl border border-gray-300 px-4 py-3.5 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-[#2349B8] focus:outline-none focus:ring-1 focus:ring-[#2349B8] sm:text-sm transition-shadow"
                placeholder={t('signin.password')}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          {!isRegister && (
            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <input
                  id="remember-me"
                  name="remember-me"
                  type="checkbox"
                  className="h-4 w-4 rounded border-gray-300 text-[#2349B8] focus:ring-[#2349B8]"
                />
                <label htmlFor="remember-me" className="ml-2 block text-sm text-gray-600">
                  {t('signin.remember')}
                </label>
              </div>

              <div className="text-sm">
                <a href="#" className="font-medium text-[#2349B8] hover:text-blue-800 transition-colors">
                  {t('signin.forgot')}
                </a>
              </div>
            </div>
          )}

          <div>
            <button
              type="submit"
              disabled={loading}
              className="group relative flex w-full justify-center rounded-xl border border-transparent bg-[#2349B8] px-4 py-3.5 text-sm font-bold text-white hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-[#2349B8] focus:ring-offset-2 transition-all shadow-md shadow-blue-200 disabled:opacity-60 disabled:cursor-not-allowed"
            >
              {loading ? '...' : isRegister ? t('signin.register_button', { defaultValue: 'Register' }) : t('signin.signin')}
            </button>
          </div>
          
          <div className="mt-6 text-center text-sm text-gray-600">
            {isRegister ? (
              <button type="button" onClick={() => { setIsRegister(false); setErrorMsg(''); setSuccessMsg(''); }} className="font-semibold text-[#2349B8] hover:text-blue-800 transition-colors">
                {t('signin.back_to_login', { defaultValue: 'Back to Sign In' })}
              </button>
            ) : (
              <>
                {t('signin.no_account')}{' '}
                <button type="button" onClick={() => { setIsRegister(true); setErrorMsg(''); setSuccessMsg(''); }} className="font-semibold text-[#2349B8] hover:text-blue-800 transition-colors">
                  {t('signin.create')}
                </button>
              </>
            )}
          </div>
        </form>
      </div>
    </div>
  )
}
