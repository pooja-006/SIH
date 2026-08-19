import { useTranslation } from 'react-i18next'

const subjectSkillMap = {
  'Computer Science': ['Python', 'JavaScript', 'React', 'SQL', 'Git', 'Linux', 'Data Analysis', 'Troubleshooting'],
  'Information Technology': ['Python', 'SQL', 'Networking', 'Linux', 'IT Support', 'JavaScript', 'Cybersecurity', 'Troubleshooting'],
  'Data Science': ['Python', 'SQL', 'Data Analysis', 'MS Excel', 'Power BI', 'Machine Learning'],
  'Mechanical Engineering': ['AutoCAD', 'MS Excel', 'Quality Control', 'Lean Manufacturing', 'Documentation'],
  'Electronics and Communication': ['Embedded C', 'Microcontrollers', 'PCB Design', 'Arduino', 'Networking', 'Solar Energy'],
  'Electrical Engineering': ['Solar Energy', 'AutoCAD', 'Microcontrollers', 'MS Excel', 'Networking'],
  'Commerce': ['Accounting', 'Tally', 'MS Excel', 'Financial Analysis', 'Communication', 'KYC'],
  'Business Administration': ['Communication', 'MS Excel', 'Digital Marketing', 'Financial Analysis', 'Accounting', 'Recruitment', 'Content Writing', 'Documentation'],
  'Agriculture': ['Agriculture', 'Field Survey', 'MS Excel', 'Communication', 'Data Collection'],
  'Civil Engineering': ['AutoCAD', 'Site Survey', 'MS Excel', 'Documentation', 'Project Management'],
  'Public Administration': ['Communication', 'Documentation', 'MS Excel', 'Research', 'Data Entry'],
  'Social Work': ['Communication', 'Field Survey', 'Data Collection', 'Community Engagement', 'Documentation'],
  'Nursing': ['Patient Support', 'Communication', 'MS Excel', 'Documentation', 'Data Entry'],
  'Tourism': ['Customer Service', 'Communication', 'Tourism Operations', 'Content Writing', 'MS Excel'],
}

const allSkills = [
  'Python', 'SQL', 'JavaScript', 'React', 'Git', 'Linux', 'Data Analysis', 'Power BI', 'Machine Learning',
  'MS Excel', 'Accounting', 'Tally', 'Financial Analysis', 'Digital Marketing', 'Content Writing', 'Communication', 'Recruitment', 'Customer Service', 'Documentation',
  'AutoCAD', 'Embedded C', 'Microcontrollers', 'PCB Design', 'Arduino', 'Solar Energy', 'Quality Control', 'Lean Manufacturing', 'Site Survey', 'Project Management',
  'Agriculture', 'Field Survey', 'Data Collection', 'Community Engagement', 'Patient Support', 'Tourism Operations', 'Data Entry', 'Networking', 'IT Support', 'Cybersecurity', 'Troubleshooting', 'KYC'
]

export default function SkillSelector({ selected, branch, onChange }) {
  const { t } = useTranslation()

  const recommendedSkills = branch && subjectSkillMap[branch] ? subjectSkillMap[branch] : []
  const otherSkills = recommendedSkills.length > 0
    ? allSkills.filter((skill) => !recommendedSkills.includes(skill))
    : allSkills

  const toggle = (skill) => {
    onChange(selected.includes(skill) ? selected.filter((item) => item !== skill) : [...selected, skill])
  }

  const subjectLabel = branch ? t(`options.${branch}`, { defaultValue: branch }) : ''

  return (
    <div className="space-y-6">
      {recommendedSkills.length > 0 && (
        <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 sm:p-5 shadow-sm">
          <div className="mb-3 flex items-center justify-between flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="flex h-6 w-6 items-center justify-center rounded-full bg-blue-600 text-xs font-bold text-white">✨</span>
              <h3 className="text-sm font-bold text-[#0B1527]">
                {t('skills.recommended', { subject: subjectLabel, defaultValue: `Recommended skills for ${subjectLabel}` })}
              </h3>
            </div>
            <span className="text-xs font-semibold text-blue-700 bg-blue-100 px-3 py-1 rounded-full border border-blue-200">
              {subjectLabel}
            </span>
          </div>

          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {recommendedSkills.map((skill) => {
              const isSelected = selected.includes(skill)
              return (
                <button
                  key={skill}
                  type="button"
                  aria-pressed={isSelected}
                  onClick={() => toggle(skill)}
                  className={`chip ${isSelected ? 'chip-selected' : 'bg-white hover:bg-blue-100/60 border-blue-200 text-slate-800'}`}
                >
                  {t('options.' + skill, { defaultValue: skill })}
                </button>
              )
            })}
          </div>
        </div>
      )}

      <div>
        {recommendedSkills.length > 0 && (
          <h3 className="mb-3 text-sm font-bold text-slate-700">
            {t('skills.other', { defaultValue: 'Other available skills' })}
          </h3>
        )}
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          {otherSkills.map((skill) => {
            const isSelected = selected.includes(skill)
            return (
              <button
                key={skill}
                type="button"
                aria-pressed={isSelected}
                onClick={() => toggle(skill)}
                className={`chip ${isSelected ? 'chip-selected' : ''}`}
              >
                {t('options.' + skill, { defaultValue: skill })}
              </button>
            )
          })}
        </div>
      </div>
    </div>
  )
}
