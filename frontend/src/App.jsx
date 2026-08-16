import { Route, Routes } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import Welcome from './pages/Welcome'
import SignIn from './pages/SignIn'
import CandidateProfile from './pages/CandidateProfile'
import SkillsInterests from './pages/SkillsInterests'
import Interests from './pages/Interests'
import LocationPreferences from './pages/LocationPreferences'
import RecommendationResults from './pages/RecommendationResults'
import InternshipDetails from './pages/InternshipDetails'

export default function App() {
  return <div className="flex min-h-screen flex-col">
    <Header />
    <main className="flex-1">
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/profile" element={<CandidateProfile />} />
        <Route path="/skills" element={<SkillsInterests />} />
        <Route path="/interests" element={<Interests />} />
        <Route path="/preferences" element={<LocationPreferences />} />
        <Route path="/location" element={<LocationPreferences />} />
        <Route path="/results" element={<RecommendationResults />} />
        <Route path="/internships/:internshipId" element={<InternshipDetails />} />
      </Routes>
    </main>
    <Footer />
  </div>
}
