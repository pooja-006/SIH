import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'

export default function SignIn() {
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSignIn = (e) => {
    e.preventDefault()
    // For the prototype, we simply redirect to the profile creation matching step
    navigate('/profile')
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
            Sign in
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Or{' '}
            <Link to="/" className="font-medium text-[#2349B8] hover:text-blue-800 transition-colors">
              return to home
            </Link>
          </p>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSignIn}>
          <div className="space-y-4 rounded-md">
            <div>
              <label htmlFor="email-address" className="sr-only">Email address</label>
              <input
                id="email-address"
                name="email"
                type="email"
                autoComplete="email"
                required
                className="relative block w-full appearance-none rounded-xl border border-gray-300 px-4 py-3.5 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-[#2349B8] focus:outline-none focus:ring-1 focus:ring-[#2349B8] sm:text-sm transition-shadow"
                placeholder="Email address"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">Password</label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                className="relative block w-full appearance-none rounded-xl border border-gray-300 px-4 py-3.5 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-[#2349B8] focus:outline-none focus:ring-1 focus:ring-[#2349B8] sm:text-sm transition-shadow"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <input
                id="remember-me"
                name="remember-me"
                type="checkbox"
                className="h-4 w-4 rounded border-gray-300 text-[#2349B8] focus:ring-[#2349B8]"
              />
              <label htmlFor="remember-me" className="ml-2 block text-sm text-gray-600">
                Remember me
              </label>
            </div>

            <div className="text-sm">
              <a href="#" className="font-medium text-[#2349B8] hover:text-blue-800 transition-colors">
                Forgot your password?
              </a>
            </div>
          </div>

          <div>
            <button
              type="submit"
              className="group relative flex w-full justify-center rounded-xl border border-transparent bg-[#2349B8] px-4 py-3.5 text-sm font-bold text-white hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-[#2349B8] focus:ring-offset-2 transition-all shadow-md shadow-blue-200"
            >
              Sign in
            </button>
          </div>
          
          <div className="mt-6 text-center text-sm text-gray-600">
            Don't have an account?{' '}
            <a href="#" className="font-semibold text-[#2349B8] hover:text-blue-800 transition-colors">
              Create account
            </a>
          </div>
        </form>
      </div>
    </div>
  )
}
